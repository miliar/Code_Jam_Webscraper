
from sys import stdin



def low_neighbor(x,y,ele):
    le = ele[y][x]
    h = len(ele)
    w = len(ele[0])
    ret = [y,x]
    #North
    if y > 0:
        if ele[y-1][x] < le:
            le = ele[y-1][x]
            ret = [y-1,x]
    #West
    if x > 0:
        if ele[y][x-1] < le:
            le = ele[y][x-1]
            ret = [y,x-1]
    #East
    if x < w-1:
        if ele[y][x+1] < le:
            le = ele[y][x+1]
            ret = [y,x+1]
    #South
    if y < h-1:
        if ele[y+1][x] < le:
            le = ele[y+1][x]
            ret = [y+1,x]
    return ret



cases = int(stdin.readline().strip())

for i in range(cases):
    print "Case #%s:" % (i+1)
    dim = stdin.readline().strip().split(' ')
    h = int(dim[0])
    w = int(dim[1])
    ele = []
    for y in range(h):
        ele += [stdin.readline().strip().split(' ')]
    low_ns = []
    for y in range(h):
        row = []
        for x in range(w):
            row += [low_neighbor(x,y,ele)]
        low_ns += [row]
        
    changed = True
    while changed:
        changed = False
        for y in range(h):
            for x in range(w):
                rop = low_ns[y][x]
                if low_ns[rop[0]][rop[1]] != rop:
                    changed = True
                    low_ns[y][x] = low_ns[rop[0]][rop[1]]


    cb = 97
    bid = {}
    for y in range(h):
        rs = ''
        for x in range(w):
            bpos = str(low_ns[y][x])
            if bpos not in bid:
                bid[bpos] = cb
                cb += 1
            rs += chr(bid[bpos]) + ' '
        print rs.strip()
    