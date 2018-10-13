def getPos (n , k):
    l = []
    l.append(n)
    while(k!=1):
        val = l[0]
        l.append(val/2)
        l.append((val-1)/2)
        l.remove(val)
        l.sort(reverse=True)
        k=k-1
    return (l[0]/2, (l[0]-1)/2)



import sys

name = "small"

sys.stdin = open(name + ".in")
sys.stdout = open(name + "py.out", "w")

testCases = int(input())

for testCase in range(1, testCases + 1):
    line = raw_input().split()
    n = int(line[0])
    k = int(line[1])
    res = getPos(n, k)
    print("Case #" + str(testCase) + ": " + str(res[0]) + " " + str(res[1]))
