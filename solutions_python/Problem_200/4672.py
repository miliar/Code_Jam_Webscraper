def isTidy(n):
    s = str(n)
    for k in range(len(s) - 1):
        if (s[k] > s[k+1]):
            return False
    return True

max_in = 1002
mem = []
for n in range(max_in):
    mem.append(isTidy(n))



sf = "B-small-attempt0.in"
f = open(sf, 'r')
t = int(f.readline())
for i in range(t):
    N = int(f.readline())
    while (mem[N] == False and N >= 1):
        N -= 1
    print "Case #%d: %d" % (i + 1, N)