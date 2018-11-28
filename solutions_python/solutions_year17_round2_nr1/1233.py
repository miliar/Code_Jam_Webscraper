def solve(D, N, horse_list):
    t = []
    for horse in horse_list:
        t.append( float(D - horse[0])/horse[1] )
    return D/max(t)

t = int(raw_input())
for i in xrange(1, t+1):
    D, N = [ int(j) for j in raw_input().split(" ") ]
    horse_list = []
    for n in range(1,N+1):
        horse_list.append([ int(j) for j in raw_input().split(" ") ])
    print "Case #{}: {}".format(i, solve(D, N, horse_list))