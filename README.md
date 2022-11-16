# scoring-simulator
Simulate the scores of matches and get the best possible strategy during the game using the Monte Carlo method

Note that the current data is fake and doesn't reflect the actual robot because there is no data available right now.

It also doesn't include the bonuses that can be acheived during endgame.

The output as of 11/10/2022:
```
Best 10 auto strategies:
{'score': 42, 'strategy': ['low', 'low', 'medium', 'medium', 'medium', 'medium', 'park']}
{'score': 42, 'strategy': ['ground', 'medium', 'medium', 'medium', 'medium', 'medium', 'park']}
{'score': 41, 'strategy': ['ground', 'low', 'medium', 'medium', 'medium', 'medium', 'park']}
{'score': 41, 'strategy': ['medium', 'medium', 'medium', 'medium', 'medium', 'park', 'terminal']}
{'score': 41, 'strategy': ['ground', 'ground', 'low', 'low', 'low', 'medium', 'medium', 'park']}
{'score': 41, 'strategy': ['high', 'medium', 'medium', 'medium', 'medium', 'park']}
{'score': 41, 'strategy': ['low', 'low', 'low', 'medium', 'medium', 'medium', 'park']}
{'score': 41, 'strategy': ['ground', 'ground', 'ground', 'low', 'medium', 'medium', 'medium', 'park']}
{'score': 41, 'strategy': ['ground', 'low', 'low', 'low', 'low', 'low', 'medium', 'park']}
{'score': 40, 'strategy': ['ground', 'high', 'low', 'low', 'low', 'medium', 'park']}

Best 10 driver strategies:


{'score': 90, 'strategy': ['ground', 'ground', 'ground', 'high', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium']}

{'score': 90, 'strategy': ['ground', 'ground', 'high', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium']}

{'score': 89, 'strategy': ['ground', 'ground', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'terminal']}

{'score': 89, 'strategy': ['ground', 'ground', 'ground', 'ground', 'high', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'terminal']}

{'score': 89, 'strategy': ['ground', 'ground', 'ground', 'high', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'terminal', 'terminal']}

{'score': 89, 'strategy': ['ground', 'ground', 'ground', 'high', 'high', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium']}

{'score': 89, 'strategy': ['ground', 'ground', 'ground', 'ground', 'ground', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'terminal']}

{'score': 89, 'strategy': ['ground', 'ground', 'ground', 'ground', 'ground', 'ground', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'terminal']}

{'score': 89, 'strategy': ['ground', 'ground', 'high', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'terminal']}

{'score': 89, 'strategy': ['ground', 'ground', 'ground', 'high', 'high', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'low', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'medium', 'terminal']}
```
