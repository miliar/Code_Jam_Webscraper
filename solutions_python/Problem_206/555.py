import sys
from itertools import *

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

T = int(input())

for test_case in range(T):
    slowest = 0
    d, n = (int(x) for x in input().strip().split())
    for i in range(n):
        k, s = (int(x) for x in input().strip().split())
        hours = (d - k) / s
        slowest = max(hours, slowest)


    print("Case #" + str(test_case + 1) + ": " + str(d / slowest))