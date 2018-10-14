from __future__ import division

def count_replaces(xs,vs,k,b,t):
    too_slow = 0
    count = 0
    while k > 0 and len(xs) > 0:
        x = xs[-1]
        xs = xs[:-1]
        v = vs[-1]
        vs = vs[:-1]
        time_chick = (b - x) / v
        if time_chick <= t:
            count += too_slow
            k -= 1
        else:
            too_slow += 1
    if k > 0:
        return "IMPOSSIBLE"
    return count
        
    


with open("output2.txt", "w") as outf:
    with open("B-large.in") as f:
        k = int(f.readline().strip())
        for i in range(k):
            ts = [int(x) for x in f.readline().strip().split()]
            n = int(ts[0])
            k = int(ts[1])
            b = int(ts[2])
            t = int(ts[3])
            xs = [int(x) for x in f.readline().strip().split()]
            vs = [int(x) for x in f.readline().strip().split()]
            
            r = count_replaces(xs,vs,k,b,t)
            
            outf.write("Case #%d: %s\n" % (i+1, str(r)))