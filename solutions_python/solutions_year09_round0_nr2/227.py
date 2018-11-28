def main():
    in_file = open('b_in.txt','r')

    num_maps = int(in_file.readline())

    for m in (x+1 for x in range(num_maps)):
        H,W = map(int,in_file.readline().strip().split())
        ter = []
        bas = []
        snum = 0
        for y in range(H):
            ter.append(map(int,in_file.readline().strip().split()))
            bas.append([])
            for x in range(W):
                bas[y].append('-')
        print 'Case #%s:' % m
        sinkmap = find_sinks(W,H,ter)
        sinks = dict(zip(sinkmap,[-1]*len(sinkmap)))
        for y in range(H):
            for x in range(W):
                snum = flow(x, y, ter, bas, sinks, snum)
        print_map(bas)
        

def flow(x,y,ter,bas,sinks,snum):
    def lowest_dir():
        u,l,r,d = get_surrounding(ter,tx,ty)
        m = min((u,l,r,d))
        if m == u: return 'n'
        if m == l: return 'w'
        if m == r: return 'e'
        if m == d: return 's'

    tx = x
    ty = y
    while not (tx,ty) in sinks.keys():
        d = lowest_dir()
        if d == 'n':
            ty -= 1
        elif d == 'w':
            tx -= 1
        elif d == 'e':
            tx += 1
        elif d == 's':
            ty += 1
    if sinks[(tx,ty)] == -1:
        sinks[(tx,ty)] = snum
        snum += 1
    bas[y][x] = sinks[(tx,ty)]
    return snum

def get_surrounding(ter,x,y):
    h = len(ter)
    w = len(ter[0])
    if x == 0: l = ter[y][0]
    else:      l = ter[y][x-1]

    if x == w-1: r = ter[y][w-1]
    else:        r = ter[y][x+1]

    if y == 0: u = ter[0][x]
    else:      u = ter[y-1][x]

    if y == h-1: d = ter[h-1][x]
    else:        d = ter[y+1][x]

    return u,l,r,d
    
def find_sinks(w,h,ter):
    sinks = []
    for y in range(h):
        for x in range(w):
            mx = ter[y][x]
            mn = min(get_surrounding(ter,x,y))
            if mx <= mn: #this is a sink!
                sinks.append((x,y))
    return sinks

def print_map(m):
    for y in m:
        for x in y:
            print chr(97+x),
        print ''

main()
            
