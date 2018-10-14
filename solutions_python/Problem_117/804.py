'''
if there's ao or tu in some row, then for the ao or tu point, the other line must all be lower than this
'''
T = int(raw_input())
for t in range(1, T + 1):
    N, M = map(int, raw_input().split())
    heights = []
    for r in range(N):
        heights.append(map(int, raw_input().split()))
    hor_max = [0 for i in range(N)]
    ver_max = [0 for i in range(M)]
    for r in range(N):
        hor_max[r] = max(heights[r])
    for c in range(M):
        mx = -1
        for r in range(N):
            mx = max(mx, heights[r][c])
        ver_max[c] = mx
    
    for r in range(N):
        for c in range(M):
            if heights[r][c] < hor_max[r]:
                ver_max[c] = min(ver_max[c], heights[r][c])

    print "Case #%d:" % t ,
    for r in range(N):
        flag = False
        for c in range(M):
            if heights[r][c] > ver_max[c]:
                print "NO"
                flag = True
                break 
        if flag:
            break
    else:
        print "YES" 
    

