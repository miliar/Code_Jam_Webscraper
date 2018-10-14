import sys
from collections import defaultdict
from math import ceil

MAX_PANCAKES = 1000


def solve(counts):
    max_moves = max(counts.keys())
    moves_to_split = defaultdict(int) # N -> moves to make all plates with at most N pancakes
    for n in range(1, max_moves):
        for k,v in counts.items():
            submoves = ceil(float(max(k-n, 0)) / n)
            moves_to_split[n] += submoves * v
    #print(moves_to_split)
    needed_moves = max_moves
    for n in range(1, max_moves):
        # try to solve in n "regular" minutes (m < max_moves)
        needed_moves = min(needed_moves, moves_to_split[n] + n)
    return needed_moves

def testcase():
    d = int(sys.stdin.readline())
    counts = defaultdict(int) # N -> num plates with N pancakes
    line = sys.stdin.readline().strip()
    plates = list(map(int, line.split()))
    assert(len(plates) == d)
    for plate in plates:
        counts[plate] += 1
    testcase.id += 1
    solution = solve(counts)
    print('Case #{}: {}'.format(testcase.id, solution))
testcase.id = 0
    
t = int(sys.stdin.readline())
for i in range(t):
    testcase()