for case in range(int(raw_input())):
    D, N = map(int,raw_input().split())
    max_time = -1
    for i in range(N):
        K, S = map(int, raw_input().split())
        time = (D - K) / float(S)
        max_time = max(max_time, time)
    ans = D / max_time
    print "Case #%d: %.6f" % (case+1,ans)
