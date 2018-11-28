import sys

name = sys.argv[1]
path = ""

sys.stdin = open(path + name + ".in")
sys.stdout = open(path + name + ".out", "w")

def flip(p, pos, k):
    r = p[:pos]
    for i in range(pos, pos + k):
        if p[i] == "-":
            r += "+"
        else:
            r += "-"
    r += p[pos+k:]
    return r

T = int(input())

for testCase in range(1, T + 1):
    p, k = input().split()
    k = int(k)
    f = 0
    for pos in range(len(p)-k+1):
        #print("a", p)
        if p[pos] == "-":
            p = flip(p, pos, k)
            f += 1
        #print("b", p)
    good = True
    #print("final", p)
    for pos in range(len(p)):
        if p[pos] == "-":
            good = False
    if good:
        print("Case #" + str(testCase) + ": " + ("%d" % f))
    else:
        print("Case #" + str(testCase) + ": IMPOSSIBLE")