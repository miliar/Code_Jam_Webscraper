import sys,os,re

def testCase(fd):
    N = int(fd.readline())
    table = [[None] * N for n in range(N)]# (row,col) -> 1/0/None

    for r in range(N):
        ln = fd.readline()
        #print "line = %s" % ln,
        for c in range(N):
            if ln[c] == "1": table[r][c] = 1
            if ln[c] == "0": table[r][c] = 0
            if ln[c] == ".": table[r][c] = None
        #print table[r]
                
    #print table

    wins = [0] * N
    losts = [0] * N
    
    wp = [0] * N
    for i in range(N):
        wins[i]  = table[i].count(1)
        losts[i] = table[i].count(0)
        wp[i] = wins[i] * 1.0 / (wins[i] + losts[i])

    #print "WP =  ", wp

    owp = [None] * N
    for i in range(N):
        ary = []
        
        for j in range(N):
            if i == j: continue
            if table[j][i] is None: continue

            w = wins[j]
            l = losts[j]

            if table[j][i] == 1: w -= 1
            if table[j][i] == 0: l -= 1

            ary.append( w * 1.0 / (w + l) )
        owp[i] = avg(ary)

    #print "OWP = ", owp

    oowp = [None] * N
    for i in range(N):
        ary = []
        for j in range(N):
            if table[i][j] is not None:
                ary.append(owp[j])
        oowp[i] = avg(ary)

    #print "OOWP = ", oowp


    pri = [None] * N
    for i in range(N):
        pri[i] = 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]

    #print "PRI = ", pri
    
    return pri

def avg(ary): return sum(ary) / len(ary)

def main():
    T = int(sys.stdin.readline())
    
    for t in range(T):
        print "Cast #%d:" % (t + 1)
        print "\n".join( ["%.12f" % oowp for oowp in testCase(sys.stdin)] )

if __name__ == "__main__":
    main()
