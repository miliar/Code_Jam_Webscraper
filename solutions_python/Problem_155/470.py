import sys
from collections import defaultdict
from math import ceil


def solve(s_max, counts):
    needed = 0
    standing = 0
    for s in range(s_max+1):
        x = max(s - standing, 0)
        needed += x
        standing += x + counts[s]
    return needed

def testcase():
    line = sys.stdin.readline().strip()
    s_max, digits = line.split()
    s_max = int(s_max)
    assert(len(digits) == s_max+1)
    counts = defaultdict(int) # N -> num people with shyness N
    for s in range(s_max+1):
        counts[s] = int(digits[s])
    solution = solve(s_max, counts)
    testcase.id += 1
    print('Case #{}: {}'.format(testcase.id, solution))
testcase.id = 0
    
t = int(sys.stdin.readline())
for i in range(t):
    testcase()