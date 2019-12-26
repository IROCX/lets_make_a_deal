# simulate the game N number of times

import game_config

N = 1000
s1 = 0
s2 = 0

for i in range(N):
    s1 += game_config.game(0)
    s2 += game_config.game(1)

print('Number of trials = ' + str(N))
print('Number of wins without switching = ' + str(s1))
print('Number of wins with switching = ' + str(s2))
print("% win without switching = " + str((s1/N)*100))
print("% win with switching = " + str((s2/N)*100))