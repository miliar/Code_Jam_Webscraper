import sys

def numberToList(n):
    l =  list(str(n))
    res = []
    for c in l:
        res = res + [int(c)]
    return res

def solve(n):
    l = numberToList(n)
    size = len(l)
    for i in range(size-1, 0, -1):
        if l[i] < l[i-1]: #trouble
            for j in range(i, size):
                l[j] = 9
            # decrement number
            j = i-1
            while l[j] == 0:
                l[j] = 9
                j = j-1
            l[j] = l[j] - 1
    res = 0
    for d in l:
        res = res*10+d
    return str(res)


def process(filenamein):
    f = open(filenamein, "r")
    size = int(f.readline())
    for line in xrange(size):
        s = f.readline()
        res = solve(int(s))
        out = "Case #" + str(line+1) + ": " + res
        print out
    f.close()

if len(sys.argv) == 2:
    process(sys.argv[1])