'''
 Write a program that simulates a risk/risiko fight using 6 dices.
  How does it work?
  When a player attacks another player he uses 3 dices, the red is always the attacker and the blue is the defender.
  You have to compare the dice with the highest number to simulate the fight.
  N = first highest number
  M = second highest number
  O = third highest number
  If the numbers are equal, the defensor (blue) wins.
  Output:
  Red dices:
  6 (N)
  3 (M)
  2 (O)
  Blue dices:
  5 (N)
  3 (M)
  1 (O)
    R    B
  N 6 vs 5 => red win
  M 3 vs 3 => blue win
  O 2 vs 1 => red win
'''

import random

def risiko() -> bool:
    russia : list[int] = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)] #red
    ukraine : list[int] = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)] #blue

    for i in range(3):
        if russia[i] > ukraine[i]:
            print("Red win, with " + str(russia[i]) + " vs " + str(ukraine[i]) + "!\n")
        else:
            print("Blue win, with " + str(ukraine[i]) + " vs " + str(russia[i]) + "!\n")
    return 1

if __name__ == "__main__":
    risiko()

#слава україні

