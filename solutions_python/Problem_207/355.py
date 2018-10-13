import sys
import math
from bisect import bisect_left, bisect_right

name = "B-small-attempt1"
path = ""
sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def solvesmall(N, R, O, Y, G, B, V):
    d={'R': R, 'O':O, 'Y': Y, 'G':G, 'B':B, 'V':V}
    lst=[]
    a=''
    for w in sorted(d, key=d.get, reverse=True):
        lst.append((w, d[w]))
    if lst[0][1] > lst[1][1]+lst[2][1]:
        return 'IMPOSSIBLE'
    else:
        ans=''
        rem = lst[1][1]+lst[2][1] - lst[0][1]
        for i in range(rem):
            ans=ans+lst[0][0]+lst[1][0]+lst[2][0]
        for i in range(lst[1][1]-rem):
            ans=ans+lst[0][0]+lst[1][0]
        for i in range(lst[2][1]-rem):
            ans=ans+lst[0][0]+lst[2][0]
        return ans

for testCase in range(1, testCases + 1):
    N, R, O, Y, G, B, V=map(int, input().strip().split())
    ans=solvesmall(N, R, O, Y, G, B, V)
    print("Case #%s: %s" % (testCase, ans))