'''
Get the time and score values from the other files
Then check every possible combination in both the 30
second auto period and the 2 minute driver period to see which
strategy gives us the highest score.
'''

import score_values
import timing
import argparse
from random import choice
from multiprocessing import Process, cpu_count, Manager, Value, Array

# Get the score values from the other file
values = score_values.values
auto_period_only_values = score_values.auto_period_only_values

# Get the time values from the other file
times = timing.times
auto_period_only_times = timing.auto_period_only_times

# Get the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--fail-count", help="The number of consecutive duplicate strategies before finishing", type=int, default=500)
args = parser.parse_args()

# Get the value from the -c argument
fail_threshold = args.fail_count

all_auto_strategies = {**values, **auto_period_only_values}
time_for_auto_strategy = {**times, **auto_period_only_times}

def auto_calc_thread(auto_duplicate_count, auto_tried_strategies, fail_threshold):
    # Try every possible combination of strategies
    # Note that any point can be used infinitely many times
    # except for the auto only "park" point
    while (auto_duplicate_count.value < fail_threshold.value):
        available_strategies = all_auto_strategies.copy()
        # The strategy we're trying
        strategy = []
        # The score of the strategy
        score = 0
        # The time it takes to complete the strategy
        time = 0

        # Just add whatever strategy that has the highest point value to the strategy if there's time
        # If there's no time, then look at the next highest point value, and so on. Remember that park
        # can only be used once, so if we've already used it, then don't use it again.
        while (time < 30):
            # Get the a random point
            # If we've already used park, then don't use it again
            strategy_to_use = choice(list(available_strategies.keys()))
            if strategy_to_use == "park" and "park" in available_strategies.keys():
                available_strategies.pop("park")

            # If there's no time left, then leave the loop
            if (time + time_for_auto_strategy[strategy_to_use] > 30):
                break

            # Add the strategy to the list
            strategy.append(strategy_to_use)
            # Add the time it takes to complete the strategy to the total time
            time += time_for_auto_strategy[strategy_to_use]
            # Add the score of the strategy to the total score
            score += all_auto_strategies[strategy_to_use]
            strategy.sort()

        formatted_strategy = {
            "score": score,
            "strategy": strategy,
        }

        # If we've already tried this strategy
        # then increment the duplicate count
        if formatted_strategy in auto_tried_strategies:
            auto_duplicate_count.value += 1
        # Otherwise, reset the duplicate count
        else:
            auto_duplicate_count.value = 0
            # Add the strategy to the list of tried strategies
            auto_tried_strategies.append(formatted_strategy)

'''
Try every possible combination of strategies
in the auto period and see which one gives us the highest score.
'''
def calculate_auto(auto_duplicate_count, auto_tried_strategies, fail_threshold):
    processes = []
    for i in range(cpu_count()):
        p = Process(target=auto_calc_thread, args=(auto_duplicate_count, auto_tried_strategies, fail_threshold))
        p.start()
        processes.append(p)
    # Wait for every process to finish
    for p in processes:
        p.join()

all_driver_strategies = {**values}
time_for_driver_strategy = {**times}

def driver_calc_thread(duplicate_count, tried_strategies, fail_threshold):
    # Try every possible combination of strategies for the driver only period
    while (duplicate_count.value < fail_threshold.value):
        available_strategies = all_driver_strategies.copy()
        # The strategy we're trying
        strategy = []
        # The score of the strategy
        score = 0
        # The time it takes to complete the strategy
        time = 0

        # Just add whatever strategy that has the highest point value to the strategy if there's time
        # If there's no time, then look at the next highest point value, and so on. Remember that park
        # can only be used once, so if we've already used it, then don't use it again.
        while (time < 120):
            # Get the a random point
            # If we've already used park, then don't use it again
            strategy_to_use = choice(list(available_strategies.keys()))
            if strategy_to_use == "park" and "park" in available_strategies.keys():
                available_strategies.pop("park")

            # If there's no time left, then leave the loop
            if (time + time_for_driver_strategy[strategy_to_use] > 120):
                break

            # Add the strategy to the list
            strategy.append(strategy_to_use)
            # Add the time it takes to complete the strategy to the total time
            time += time_for_driver_strategy[strategy_to_use]
            # Add the score of the strategy to the total score
            score += all_driver_strategies[strategy_to_use]
            strategy.sort()

        formatted_strategy = {
            "score": score,
            "strategy": strategy,
        }

        # If we've already tried this strategy
        # then increment the duplicate count
        if formatted_strategy in tried_strategies:
            duplicate_count.value += 1
        # Otherwise, reset the duplicate count
        else:
            duplicate_count.value = 0
            # Add the strategy to the list of tried strategies
            tried_strategies.append(formatted_strategy)

'''
Try every possible combination of strategies
in the driver period and see which one gives us the highest score.
'''
def calculate_driver(driver_duplicate_count, driver_tried_strategies, fail_threshold):
    processes = []
    for i in range(cpu_count()):
        p = Process(target=driver_calc_thread, args=(driver_duplicate_count, driver_tried_strategies, fail_threshold))
        p.start()
        processes.append(p)
    # Wait for every process to finish
    for p in processes:
        p.join()

if __name__ == "__main__":
    manager = Manager()
    auto_tried_strategies = manager.list()
    fail_threshold = manager.Value('i', fail_threshold)
    auto_duplicate_count = manager.Value('i', 0)

    # Calculate the best strategy for the auto period
    calculate_auto(auto_duplicate_count, auto_tried_strategies, fail_threshold)
    tried_auto_strategies = list(auto_tried_strategies)

    # order the strategies by score
    tried_auto_strategies.sort(key=lambda strategy: strategy["score"], reverse=True)

    # print the list of the best 10 strategies, with each on a new line
    print("Best 10 auto strategies: ")
    for strategy in tried_auto_strategies[:10]:
        print(strategy)
    
    # Calculate the best strategy for the driver period
    driver_tried_strategies = manager.list()
    driver_duplicate_count = manager.Value('i', 0)
    calculate_driver(driver_duplicate_count, driver_tried_strategies, fail_threshold)
    tried_driver_strategies = list(driver_tried_strategies)

    # order the strategies by score
    tried_driver_strategies.sort(key=lambda strategy: strategy["score"], reverse=True)

    print("\n\n\n")

    # print the list of the best 10 strategies, with each on a new line
    print("Best 10 driver strategies: \n\n")
    for strategy in tried_driver_strategies[:10]:
        print(strategy, "\n")
    