import sys

def neighbors(p):
    for offs in [(-1,0),(0,-1),(0,1),(1,0)]:
        yield (p[0]+offs[0], p[1]+offs[1])
        
def print_map(lmap, R, C):
    for r in range(R):
        print ' '.join([lmap[(r,c)] for c in range(C)])
        
def point_map(R, C):
    for r in range(R):
        for c in range(C):
            yield (r,c)
        
T = int(sys.stdin.readline())

for t in range(T):
    maps = {}
    
    (H,W) = map(int, sys.stdin.readline().split(' '))
    
    for h in range(H):
        alts = map(int, sys.stdin.readline().split(' '))
        for w in range(W):
            maps[(h,w)] = alts[w]
    
    sinks = {}
    mark = 'a'

    def mark_sink(p):
        if p in sinks:
            return sinks[p]
            
        min_alt = maps[p]
        flow = None
        for n in neighbors(p):
            if n in maps:
                if maps[n] < min_alt:
                    min_alt = maps[n]
                    flow = n
        
        if flow:
            sinks[p] = mark_sink(flow)
            return sinks[p]
        else:
            global mark
            sinks[p] = mark
            mark = chr(ord(mark)+1)
            return sinks[p]
            
    for p in point_map(H, W):
        mark_sink(p)
        
    print "Case #%d:" % (t+1)
    print_map(sinks, H, W)
