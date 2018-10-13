
def Welcome():
    seq = raw_input()
    sub = "welcome to code jam"
    seqLen = len(seq)
    subLen = len(sub)
    ss = [None] * seqLen
    for x in xrange(seqLen-1, -1, -1):
        ss[x] = [0] * subLen
        c = seq[x]
        i = 0
        while True:
            i = sub.find(c, i)
            if i < 0:
                break
            if i == subLen-1:
                ss[x][i] = 1
                break
            count = 0
            for y in xrange(x+1, seqLen):
                count += ss[y][i+1]
            ss[x][i] = count % 10000
            i += 1
    count = 0
    for x in xrange(seqLen):
        count += ss[x][0]
    print "%04d" % (count % 10000)

#---------------------------------------------------------------

N = int(raw_input())
for testcase in range(N):
    print "Case #%d:" % (testcase+1),
    Welcome()
