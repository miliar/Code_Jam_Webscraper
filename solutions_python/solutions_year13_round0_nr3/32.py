import sys
import collections
import bisect

goods = set()

def ook(x):
    ct = collections.defaultdict(int)
    y = x
    offset = 0
    strs = [[ord(t)-ord('0') for t in str(y*i)[::-1]] for i in xrange(10)]
    while y > 0:
        s = strs[y % 10]
        for i in xrange(len(s)):
            ct[i+offset] += s[i]
            if ct[i+offset] > 9:
                return False
        y /= 10
        offset += 1
    return True
LIMIT = 10**50
QQ = 53 
def gen_even():
    z = 1
    inc = 1
    while z <= LIMIT:
        s = str(z)
        ss = s + s[::-1]
        if len(ss) > QQ:
            break
        p = int(ss)
        if ook(p):
            inc = 1
            z += 1
            qt = p**2
            sqt = str(qt)
            if sqt == sqt[::-1]:
                goods.add(qt)
        else:
            while z % (10*inc) != 0:
                z += inc
            inc *= 10

def gen_odd():
    z = 1
    inc = 1
    while z <= LIMIT:
        s = str(z)
        ss = s[:-1] + s[-1] + s[:-1][::-1]
        if(len(ss) > QQ):
            break
        p = int(ss)
        if ook(p):
            inc = 1
            z += 1
            #print "OK", p, p**2
            qt = p**2
            sqt = str(qt)
            if sqt == sqt[::-1]:
                goods.add(qt)
        else:
            while z % (10*inc) != 0:
                z += inc
            inc *= 10


def solve(A, B):
    #return sum(1 for i in goods if A <= i <= B)
    return bisect.bisect_right(goods, B) - bisect.bisect_left(goods, A)
    out = 0
    idx = 0
    N = len(goods)
    while idx < N and goods[idx] < A:
        idx += 1
    while idx < N and goods[idx] <= B:
        idx += 1
        out += 1
    return out




def main():
    global goods
    gen_even()
    print >>sys.stderr, "CALCD 1"
    gen_odd()
    print >>sys.stderr, "CALCD"
    goods = sorted(goods)
    print >>sys.stderr, len(str(goods[-1]))
    T = int(sys.stdin.readline())
    for cn in range(1, T+1):
        A, B = [int(x) for x in sys.stdin.readline().strip().split()]
        print "Case #%d: %s" % (cn, solve(A,B))

if __name__ == '__main__':
    main()
        
