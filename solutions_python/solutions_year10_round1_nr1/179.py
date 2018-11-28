import re

def process_case() :
    # n = int(raw_input())
    N, K = map(int, raw_input().split())
    arr = []
    def dmp(a) :
        for line in a : print line
    for i in range(0, N) :
        line = raw_input()
        line = line.strip()
        assert len(line) == N
        arr.append( line.strip() )

    # dmp(arr)

    # rotate
    new_arr = []
    for i in range(0, N) :
        new_arr.append( [None]*N )
    for x in range(0, N) :
        for y in range(0, N) :
            new_arr[x][y] = arr[N-y-1][x]
    # dmp(new_arr)

    cols = []
    for i in range(0, N) :
       cols.append( [] )
    for y in range(0, N) :
        for x in range(N-1, -1, -1) :
            cell = new_arr[x][y]
            if cell in ("R", "B") :
                cols[y].append(cell)
    # print cols

    garr = []
    for i in range(0, N) :
        garr.append( ["."] * N )
    
    for y in range(0, N) :
        pos = N-1
        for cell in cols[y] :
            garr[pos][y] = cell
            pos -= 1
    # dmp(garr)

    DIR = ( (1, 0), (1, 1), (0, 1), (0, -1) )
    def scanc(c, x, y) :
        for d in DIR :
            tx = x + d[0]*(K-1)
            ty = y + d[1]*(K-1)
            if tx<0 or ty<0 :
                continue
            if tx>=N or ty>=N :
                continue
            success = True 
            for i in range(0, K) :
                ox = x + d[0] * i
                oy = y + d[1] * i
                # print "***%d, %d" % (ox, oy)
                if garr[ox][oy] != c :
                    success = False
                    break
            if success :
                # print x, y, d
                return True
        return False

    def scan(c) :
        for x in range(0, N) :
            for y in range(0, N) :
                if scanc(c, x, y) :
                    return True
        return False

    red = scan("R")
    blue = scan("B")
    if red and blue :
        return "Both"
    elif red :
        return "Red"
    elif blue :
        return "Blue"
    else :
        return "Neither"

if __name__ == "__main__" :
    case_num = int(raw_input())
    for i in range(case_num) :
        result = process_case()
        print "Case #%d: %s" % (i+1, result)
