def countback(n):
    ns = str(n)
    nl = list(ns)
    while True:
        for i in xrange(1, len(nl)):
            if int(nl[i]) < int(nl[i-1]):
                nl[i-1] = str(int(nl[i-1])-1)
                for j in xrange(i, len(nl)):
                    nl[j] = "9"
                break
            if i == len(nl)-1:
                return int("".join(nl))


# get input
t = int(raw_input())

for i in xrange(1, t+1):
    n = int(raw_input())
    res = -1
    if n < 10:
        res = n
    else:
        res = countback(n)
    print "Case #{}: {}".format(i, res)
