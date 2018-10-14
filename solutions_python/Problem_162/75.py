import sys
import math

dm = {
}

def digits(ln):
    if ln in dm:
        return dm[ln]
    if ln == 1:
        dm[ln] = 0
        return 0
    elif ln == 2:
        dm[ln] = 10
        return 10
    else:
        half1 = (ln-1)/2
        half2 = (ln)/2
        assert half1+half2 == ln-1
        out = digits(ln-1) + int("9"*half1) + 1 + int("9"*half2)
        dm[ln] = out
        return out

# for i in range(1,15):
#     print i,digits(i)
# assert False

T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    strN = str(N)
    ln = len(strN)
    if ln == 1:
        print "Case #%d: %d" % (i+1, N)
        continue
    c = digits(ln)
    half = ln/2
    if strN[half:] != "0"*(ln-half):
        try1 = int(strN[:half][::-1])
        # print "try1 half", try1
        try1 += int(strN[half:])-1
        try1 += 1
        # print "try1 second", int(strN[ln/2:])-1
        try2 = N-pow(10, ln-1)
        # print "try2", try2
        # print "c", c
    else:
        sub1 = int(strN[:half])-1
        if sub1 == 0:
            print "Case #%d: %d" % (i+1, c)
            continue
        try1 = int(str(sub1)[::-1])
        try1 += 1
        try1 += pow(10, ln-half)-1
        try2 = N-pow(10, ln-1)

    if try1 < try2:
        print "Case #%d: %d" % (i+1, c+try1)
    else:
        print "Case #%d: %d" % (i+1, c+try2)
