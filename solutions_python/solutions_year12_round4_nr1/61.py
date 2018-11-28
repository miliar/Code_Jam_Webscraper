import sys

f = open(sys.argv[1])
T = int(f.readline())
for t in range(T):
    N = int(f.readline())
    vines = []
    best_reach = []
    for vine in range(N):
        vine = map(int, f.readline().split())
        vines.append(vine)
        
    best_reach.append(vines[0][0])
    for ii in range(1,N):
        best_reach.append(0)
        for jj in range(0, ii):
            if best_reach[jj] + vines[jj][0] >= vines[ii][0]:
                best_reach[ii] = max(best_reach[ii], min(vines[ii][0]-vines[jj][0], vines[ii][1]))
    success = False
    
    D = int(f.readline())
    for ii in range(N):
        if vines[ii][0] + best_reach[ii] >= D:
            success = True
    
    print "Case #%d:" % (t + 1), "YES" if success else "NO"
