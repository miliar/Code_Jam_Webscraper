import sys
from collections import defaultdict as dd

def compute(searche, queries):
    a = 0
    available = set(searche)
    for q in queries:
        if q not in available:
            continue
        if len(available) == 1:
            a += 1
            available = set(searche)
        available.remove(q)
    return a


def main():
    f = open(sys.argv[1])
    if len(sys.argv) > 2:
        out = open(sys.argv[2], 'w')
    else:
        out = sys.stdout

    T = int(f.readline())   
    for test in range(1, T+1):
        X, S, R, rTime, N = map(int, f.readline().split())
        
        ranges = []
        for i in range(N):
            ranges.append(tuple(map(int, f.readline().split())))
        ranges.sort()
        #print ranges
        e0 = 0
        sranges = []
        time = 0
        for b, e, w in ranges:
            if e0 != b:
                d = float(b - e0)
                time += d / S
                sranges.append((0, d))
            d = float(e - b)
            time += d / (S + w)
            sranges.append((w, d))
            e0 = e
        if e0 != X:
            d = float(X - e0)
            time += d / S
            sranges.append((0, d))
        sranges.sort(reverse=True)
        delta = R - S
        rTime = float(rTime)
        #print sranges, time, rTime
        while rTime > 0 and sranges:
            w, d = sranges.pop()
            ti = min(rTime, d/(R+w))
            #print ti
            time -= delta * ti / (S+ w)
            rTime -= ti
            #print sranges, time, rTime

        print >>out, "Case #%d: %.9f" % (test, time)

if __name__ == "__main__":
    main()