import sys
from pprint import pprint

n = int(sys.stdin.readline().rstrip("\n"))


for i in xrange(n):
    line = sys.stdin.readline().rstrip("\n")
    m,x = line.split(" ")
    m = int(m)

    answer = 0
    current = 0
    for j in xrange(m+1):
        val = int(x[j])
        if current < j:
            answer += abs(j - current)
            current += val  + (j - current)
        else:
            current += val

    print("Case #"+ str(i + 1) + ": " + str(answer))