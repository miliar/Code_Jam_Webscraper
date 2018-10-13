T = int(input())

for x in range(1, T+1):
        (D, N) = [int(a) for a in input().split()]
        times = []
        for i in range(N):
                (ki, si) = (int(a) for a in input().split())
                ni = (D-ki)/si
                times.append(ni)
        n = max(times)
        print("Case #%d: %f" % (x, D/n))
