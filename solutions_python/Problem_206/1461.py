def read_int():
    return int(raw_input())

def read_tuple(t=int,sep=" "):
    return tuple(map(t,raw_input().split(sep)))

def solve():
    d, n = read_tuple()
    max_time = 0.0
    for i in xrange(n):
        ki, si = read_tuple()
        t = float(d-ki)/si
        max_time = max(t, max_time)
    return d/max_time

def main():
    t = read_int()
    for i in xrange(1,t+1):
        ans = solve()
        print "Case #%d: %.7f" % (i, ans)
if __name__ == "__main__":
    main()
