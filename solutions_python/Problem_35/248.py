"""B
   Google CodeJam 2009
"""

from datetime import datetime

SENTINEL = (99999,99999,99999)
       
def routine(rows):
    def flow(row, col):
        N = (rows[row-1][col], row-1,col) if row>0 else SENTINEL
        W = (rows[row][col-1], row, col-1) if col>0 else SENTINEL
        E = (rows[row][col+1], row, col+1) if col<len(rows[row])-1 else SENTINEL
        S = (rows[row+1][col], row+1, col) if row<len(rows)-1 else SENTINEL

        res = min(N,W,E,S)
        
        if res[0] >= rows[row][col]:
            return None   #sink
        
        return res[1:]       
    
    def trace_sink(row, col):
        while flow(row, col):
            row, col = flow(row, col)
        return row, col
            
    
    #pass to find sinks
    tracerows = []
    for row in xrange(len(rows)):
        tracerow = []
        for col in xrange(len(rows[row])):
            tracerow.append(trace_sink(row, col))
        tracerows.append(tracerow)
        
    #pass to mark sinks
    basins = {}
    mark=ord('a')
    for row in xrange(len(rows)):
        for col in xrange(len(rows[row])):
            if tracerows[row][col] not in basins:
                basins[tracerows[row][col]] = chr(mark)
                mark += 1
                
            tracerows[row][col] = basins[tracerows[row][col]]
         
    #print tracerows
    return tracerows

if __name__ == '__main__':
    filename = "B-large"
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline())
    print c, "cases"
    for case in xrange(c):
        H, W = [int(x) for x in f.readline().split()]

        print H, W

        rows = []
        for row in xrange(H):
            rows.append([int(x) for x in f.readline().split()])

        #print rows

        #print
        print >>fo, "Case #%d:" % (case+1)
        for tr in routine(rows):
            print >>fo, " ".join(tr)

    fo.close()
    f.close()
    print datetime.now()
