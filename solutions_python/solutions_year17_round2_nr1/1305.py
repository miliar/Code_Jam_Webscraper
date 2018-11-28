def get_max_speed(D, N, k_s):
    times = map(lambda a: (D-a[0])/float(a[1]) ,k_s)
    max_t = max(times)
    return D/max_t

if __name__ == "__main__":
    t = int(raw_input().strip())
    for tno in range(0, t):
        D, N = [int(x) for x in raw_input().strip().split(' ')]
        k_s = []
        for _ in range(0, N):
            i, s = [int(x) for x in raw_input().strip().split(' ')]
            k_s.append((i, s))
        ans = get_max_speed(D, N, k_s)
        print "Case #%d: %f" % ( tno + 1, ans )
