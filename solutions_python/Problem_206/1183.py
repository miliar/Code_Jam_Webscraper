import sys
import math

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

name = sys.argv[1]
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

T = int(input())

for testCase in range(1, T + 1):
    eprint("Case #", testCase)
    d, n =  [int(x) for x in input().split()]
    time = 0
    for i in range(n):
        k, s =  [int(x) for x in input().split()]
        time = max(time, (d-k)/s)
        eprint(k, s, time)
    print("Case #" + str(testCase) + ": ", d/time)    

