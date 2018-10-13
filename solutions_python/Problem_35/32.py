from StringIO import StringIO

example = StringIO( """5
3 3
9 6 3
5 9 6
3 5 9
1 10
0 1 2 3 4 5 6 7 8 7
2 3
7 6 7
7 6 7
5 5
1 2 3 4 5
2 9 3 9 6
3 3 0 8 7
4 9 8 9 8
5 6 7 8 9
2 13
8 8 8 8 8 8 8 8 8 8 8 8 8
8 8 8 8 8 8 8 8 8 8 8 8 8""")

class Cell:
    def __init__(self, elev):
        self.elev = int(elev)
        self.sink = None
        self.down = None
        self.up = []
        self.sinkname = None
        
    def set_and_get_sink(self):
        if self.sink is not None:
            return self.sink
        
        if self.down is None:
            self.sink = self
        else:
            self.sink = self.down.set_and_get_sink()
        return self.sink
        
    def __repr__(self):
        return "<%s>"%(self.elev)

def main(strm):
    T = int( strm.readline() )
    
    fp = open( "B-large.out", "w" )
    
    for i in range(T):
        fp.write( "Case #%d:\n"%(i+1) )
        
        # load map
        H, W = [int(x) for x in strm.readline().split()]
        map = []
        for j in range(H):
            row = strm.readline()
            map.append( [Cell(x) for x in row.split()] )
        
        # tag cells with their uphill and downhill neighbors
        for y in range(H):
            for x in range(W):
                curr = map[y][x]
                
                w = map[y][x-1] if x>0 else None
                s = map[y+1][x] if y<H-1 else None
                e = map[y][x+1] if x<W-1 else None
                n = map[y-1][x] if y>0 else None
                
                winnerval = 100000000
                winner = None
                for neighbor in (n, w, e, s):
                    if neighbor is not None and neighbor.elev < winnerval:
                        winner = neighbor
                        winnerval = neighbor.elev
                
                if winner is not None and winner.elev < curr.elev:
                    curr.down = winner
                    winner.up.append(curr)
        

        
        lexy = tuple("abcdefghijklmnopqrstuvwxyz")
        curr_sinkname = 0
        for y in range(H):
            sinkrow = []
            for x in range(W):
                sink = map[y][x].set_and_get_sink()
                if sink.sinkname == None:
                    sink.sinkname = lexy[curr_sinkname]
                    curr_sinkname += 1
                sinkrow.append( sink.sinkname )
            print " ".join(sinkrow)
            fp.write( " ".join(sinkrow)+"\n" )
                
        
    
if __name__=='__main__':
    fp = open( "B-large.in" )
    main(fp)
    print "done"