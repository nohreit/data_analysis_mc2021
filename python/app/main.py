import matplotlib.pyplot as plt
import numpy
from scipy import stats


def run():
    str_p1 = str_p2 = 0

    str_p1 = input('Player 1:\n[0]: \'rock\', [1]: \'paper\', [2]: \'scissors\'\n>>>')
    print(str_p1, switch(str_p1))
    str_p2 = input('Player 2:\n[0]: \'rock\', [1]: \'paper\', [2]: \'scissors\'\n>>>')
    # print(switch(str_p2))


def switch(i):
    cases = {0: 'rock', 1: 'paper', 2: 'scissors'}
    func = switch.get(i, lambda: 'invalid')
    return func()


def new_game(i):
    cases = {'Y': True, 'N': False}
    func = new_game.get(i, lambda: 'invalid')
    return func()


def try_it():
    trav_loc = ['paris', 'sydney', 'tokyo', 'guangzhou', 'hanoi']
    print(trav_loc)

    trav_loc.sort()
    print(trav_loc)


if __name__ == "__main__":
    # run()
    try_it()
