# 3
# D 2525 N 1
# K1 2400 S1 5
# 300 2
# 120 60
# 60 90
# 100 2
# 80 100
# 70 10

n_tc = int(input())

for tc in range(1,n_tc+1):
    total_dist, N = list(map(int, input().split()))

    times = []
    for i in range(N):
        curr_dist, speed = list(map(int, input().split()))
        times.append( ( total_dist - curr_dist )/speed )
    
    longest = max(times)

    best_speed = ( total_dist / longest )
    print( "Case #%d: %.6f" % (tc, best_speed) )

