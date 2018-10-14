import sys

#def dbg(s): sys.stderr.write(str(s) + "\n")
def dbg(s): None
def reads(t): return list(map(t, input().split(" ")))
def read(t): return t(input())

def time_to(cookies, csum, v):
    return (cookies - csum) / v

def optimal_time(c, f, x):
    v = 2
    csum = 0
    time = 0.0

    while True:
        if x == csum:
            return time

        dbg("time: %s" % time)
        dbg("csum: %f, v: %f" % (csum, v))

        current_t = time_to(x, csum, v) + time
        buy_fact_t = time_to(c, csum, v)

        dbg("current_t: %f" % current_t)

        v1 = v + f
        csum1 = csum - c if csum > c else 0
        fact_t = time_to(x, csum1, v1) + buy_fact_t + time
        dbg("buy_fact_t: %f, fact_t: %f, v1: %f, csum1: %f" % (buy_fact_t, fact_t, v1, csum1))
    
        if fact_t < current_t:
            v = v1
            csum = csum1
            time += buy_fact_t
        else:
            return current_t


T = read(int)

for t in range(1, T+1):
    (C, F, X) = reads(float)

    s = optimal_time(C, F, X)

    print("Case #%d: %0.7f" % (t, s))
