import math

def same(l):
    if l == []:
        return True
    v = l[0]
    for e in l:
        if e != v:
            return False
    return True

def secval(l):
    for i,e in enumerate(l):
        if e != l[0]:
            return i

def do_case(i):
    N, K = map(int, raw_input().split())
    U = float(raw_input())
    P = sorted(map(float, raw_input().split()))

    while U>0:
        if same(P):
            P = [P[0]+U/K]*K
            U = 0.
            #print "+++", P, U
        else:
            f = P[0]
            si = secval(P)
            s = P[si]
            cnt = si
            pts = min( (s-f)*cnt, U )
            for j in xrange(cnt):
                P[j] += (pts / cnt)
            U -= pts
            #print "***", P, U

    res = reduce(lambda x,y:x*y, P)
    print "Case #{}: {:.8f}".format(i+1, res)

def main():
    N = int(raw_input())
    for i in xrange(N):
        do_case(i)

main()

