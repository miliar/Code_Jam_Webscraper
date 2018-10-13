import itertools as it
import numpy as np
from sys import stdin

T = int(stdin.next())

lines = [list(line.strip()) for line in stdin]
puzzles = []
for i in range(T):
    puzzles.append(lines[5*i:5*i+4])

puzzles = np.array(puzzles)

def status(puzzle):
    for letter in ['X', 'O']:
        for p in [puzzle, puzzle.T, [np.diag(puzzle)], [np.diag(puzzle[::-1])]]:
            for row in p:
                if all((row == letter) | (row == 'T')):
                    return letter + ' won'
    if '.' in puzzle:
        return 'Game has not completed'
    return 'Draw'
                    

for i,puzzle in enumerate(puzzles):
    print('Case #%d: %s' % (i+1, status(puzzle)))
