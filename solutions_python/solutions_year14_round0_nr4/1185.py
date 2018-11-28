__author__ = 'dshgna'

import time


def war(count, naomi, kevin):
    kcount = 0
    y = 0
    for x in naomi:
        while (y < count):
            if (x < kevin[y]):
                #print x, kevin[y]
                kcount = kcount + 1
                y = y + 1
                break
            else:
                y = y + 1
    return (count - kcount)


def dwar(count, naomi, kevin):
    ncount = 0
    y = 0
    for x in naomi:
        while (y < count):
            if (x > kevin[y]):
                #print x, kevin[y]
                ncount = ncount + 1
                y = y + 1
                break
            else:
                break
    return ncount


if __name__ == "__main__":
    start = time.time()
    f = file("D-large.in")
    fout = file("D-large.out", "w+")
    T = int(f.readline())
    #print T
    for case in range(1, T+1):
        C = int(f.readline())
        N = [float(x) for x in f.readline().split()]
        K = [float(x) for x in f.readline().split()]
        N1 = sorted(N)
        K1 = sorted(K)
        warc = war(C, N1, K1)
        dwarc = dwar(C, N1, K1)
        out = "Case #%d: %d %d\n" % (case, dwarc, warc)
        #print out
        fout.write(out)
    fout.close()
    f.close()
    end = time.time()
    print "Time %s:%s (%s)" % (int((end-start) / 60), int((end-start) % 60), end-start)