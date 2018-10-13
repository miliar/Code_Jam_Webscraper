import sys
import math
from bisect import bisect_left, bisect_right

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    d, n = map(int, input().strip().split())
    speeds=[]
    for i in range(n):
        k, s = map(int, input().strip().split())
        t = (d-k)/s
        if t>0:
            speeds.append(d/t)
        ans=min(speeds)
    print("Case #%s: %s" % (testCase, ans))