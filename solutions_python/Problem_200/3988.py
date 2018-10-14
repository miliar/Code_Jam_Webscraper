# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def isTidy(n):
    #n = str(n)
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True

def lastTidy(N):
    N = [int(x) for x in list(str(N))]
    currIdx = len(N) - 1
    while(not isTidy(N)):
        if N[currIdx] > 1:
            N[currIdx] -= 1
        else:
            N[currIdx] = 9
        if N[currIdx] == 9:
            currIdx = currIdx - 1
            N[currIdx] = N[currIdx] - 1


    return int("".join([str(i) for i in N]))
t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    #n, m = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    n = int(raw_input())
    print "Case #{}: {}".format(i, lastTidy(n))
    # check out .format's specification for more formatting options

