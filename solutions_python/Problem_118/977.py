import math

def isPal(n):
    if n%1 != 0: return False
    sn = str(long(n))
    for i in xrange(0, len(sn)):
        if (sn[i] != sn[-i-1]): return False
    return True

if __name__ == "__main__":
    T = int(raw_input())
    for c in xrange(1,T+1):
        [A, B] = map(lambda x: long(x), raw_input().split())
        cnt = 0
        for i in xrange(A,B+1L):
            if (isPal(i) and isPal(math.sqrt(i))): cnt+=1

        print 'Case #%d: %d' % (c, cnt)

    

