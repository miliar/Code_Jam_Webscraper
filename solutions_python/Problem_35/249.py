#!/usr/bin/python
import sys
input = sys.stdin


neighbours = [(1,0),(0,-1),(0,1),(-1,0)] 

basins = 'abcdefghijklmnopqrstuvwxyz'

def solve(key, flow):
    if '-' in flow[key]:
        sol =  solve(flow[key], flow)
        flow[key] = sol
        return sol
    else:
        return flow[key]


T = int(input.readline())

for t in range(1,T+1):
    currentbasin = 0
    H, W = [int(x) for x in input.readline().split()]
    map = []
    for h in range(H):
        map.append([int(x) for x in input.readline().split()])

    flow = {}
    for h in range(H):
        for w in range(W):
            currentaltitude = map[h][w] 
            flows = [(map[dh+h][dw+w],dh+h,dw+w) for (dh, dw) in neighbours if dh + h >= 0 and dw + w >= 0 and dh + h < H and dw + w < W and map[dh+h][dw+w] < currentaltitude]
            key = str(h)+'-'+str(w)
            if not flows:
                flow[key] = str(currentbasin)
                currentbasin += 1
            else:
                flows.sort()
                flow[key] = str(flows[0][1]) + '-' + str(flows[0][2])

    mapping = {}
    currentbasin = 0
    for h in range(H):
        for w in range(W):
            key = str(h)+'-'+str(w)
            sol = solve(key, flow)
            if not sol in mapping:
                mapping[sol] = basins[currentbasin]
                currentbasin +=1
            map[h][w] = mapping[sol]

    print 'Case #' + str(t) + ':'    
    for h in range(H):
        print ' '.join(map[h])
