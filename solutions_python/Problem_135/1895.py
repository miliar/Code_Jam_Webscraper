import sys

import numpy as np
from numpy.random import shuffle

readline = sys.stdin.readline

def random_grid():
    grid = np.random.arange(16)
    shuffle(grid)
    grid = grid.reshape((4,4))
    return grid

def read_grid():
    return [ 
        [int(i) for i in readline().split() ]
        for _ in range(4)
    ]

def get_available():
    y = int(readline())
    grid = read_grid()
    return set(grid[y - 1])

def test_case():
    first = get_available()
    second = get_available()
    possible = first.intersection(second)
    if not possible:
        return "Volunteer cheated!"
    elif len(possible) == 1:
        return possible.pop()
    else:
        return "Bad magician!"

def main():
    T = int(readline())
    for i in range(1,T+1):
        print("Case #{i}: {result}".format(
            i=i, result=test_case()
        ))

if __name__ == '__main__':
    main()

