
import sys
from math import pi

name = "A-large"
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

testCases = int(input())

def side(p):
    (r,h) = p
    return 2*pi*r*h

def solution(arr,count):
    arr.sort(reverse=True)

    arr2 = list(arr)
    arr2.sort(key=side,reverse=True)
    arr2 = arr2[:count]

    res = 0
    best = []
    # choose base
    for base in arr:
        (r1,h1) = base
        arr3 = list(arr2)
        if base in arr3:
            arr3.remove(base)
        else:
            arr3 = arr3[:-1]
        arr3 = [base] + arr3 + [(0,0)]
        rtmp = 0
        for i in range(len(arr3)-1):
            rtmp += 2 * pi * arr3[i][0] * arr3[i][1]
            rtmp += pi * (arr3[i][0]**2 - arr3[i+1][0]**2)
        res = max(res,rtmp)
        best = arr3
    return res

for testCase in range(1, testCases + 1):
    first = input()
    first = first.split()
    num = int(first[0])
    count = int(first[1])
    arr = []
    for i in range(num):
      inp = input().split()
      arr.append(  (int(inp[0]), int(inp[1]) ))
    res = solution(arr,count)

    print("Case #" + str(testCase) + ": " + ("%.10f" % res))
