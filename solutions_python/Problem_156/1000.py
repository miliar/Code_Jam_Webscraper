import sys

name = "B-small-attempt0"
path = ""

sys.stdin = open(path + name +  ".in", "r")
sys.stdout = open(path + name + ".out", "w")

cases = int(raw_input())

for t in range(1,cases+1):

    D = int(raw_input())
    P = list(map(int, raw_input().split()))
    answer = max(P)

    Z = 2
    while Z < answer:
        answer = min(answer, sum([(x - 1) // Z for x in P]) + Z)
        Z += 1

    print "Case #" + str(t) + ": " + str(answer)
