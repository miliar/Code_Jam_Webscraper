#!/usr/bin/python

T = int(raw_input())

def isLowest(Map, h, w, H, W):
    if (h > 0 and Map[h][w] > Map[h-1][w]):
        return False
    if (w > 0 and Map[h][w] > Map[h][w-1]):
        return False
    if (h < H - 1 and Map[h][w] > Map[h+1][w]):
        return False
    if (w < W - 1 and Map[h][w] > Map[h][w+1]):
        return False
    return True

def next(Map,h,w,H,W):
    nextH = h
    nextW = w
    lowest = 10000
    if (h > 0 and lowest > Map[h-1][w]):
        lowest = Map[h-1][w]
        nextH = h-1
        nextW = w
    if (w > 0 and lowest > Map[h][w-1]):
        lowest = Map[h][w-1]
        nextH = h
        nextW = w-1
    if (w < W - 1 and lowest > Map[h][w+1]):
        lowest = Map[h][w+1]
        nextH = h
        nextW = w+1
    if (h < H - 1 and lowest > Map[h+1][w]):
        lowest = Map[h+1][w]
        nextW = w
        nextH = h+1
    if (Map[h][w] <= lowest):
        nextH = h
        nextW = w
    
    return (nextH, nextW)

for x in range(0, T):
    (H, W) = map(int, raw_input().split(' '))
    Map = []
    for y in range(0, H):
        Map.append(map(int, raw_input().split(' ')))
    
    Basins = [[None]*W]*H
    sinks = {}
    count = ord('a')
    
    print "Case #"+str(x+1)+":"
    # print Map
    # print Basins    
    for i in range(0, H):
        for j in range(0, W):
            # if (Basins[i][j] != None):
                # continue
                
            h = i
            w = j
            while True:
                # print h,w
                (oldH, oldW) = (h,w)
                (h,w) = next(Map, h,w,H,W)
                if oldH == h and oldW == w:
                    break
            
            # print ''
            
            if (not sinks.has_key((h,w))):
                # print "New sink",h,w,count
                sinks[(h,w)] = chr(count)
                count += 1
            
            # print i,j,'sinks at',h,w, ", sink:",sinks[(h,w)]
            print sinks[(h,w)],
            Basins[i][j] = sinks[(h,w)]
        print
                
    # for i in range(0, H):
    #     for j in range(0, W):
    #         print Basins[i][j],
    #     print ''
    
    # exit(0)
    