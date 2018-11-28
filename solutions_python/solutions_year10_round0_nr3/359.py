import sys
from itertools import izip, chain

sys.stdin = open('roller.in.txt', 'r')
sys.stdout = open('roller.out.txt', 'w')



def xrange_wrap(start, stop, period):
    if start < stop:
        return xrange(start, stop)
    else:
        return chain(xrange(start, period), xrange(0,stop))

def main():
    T = input('')
    for t in xrange(T):
        R,K,N = map(int, raw_input('').split())
        g = map(int, raw_input('').split())

        win = [0]*N
        nex = [0]*N
        for i,j in izip(xrange(N),g):
            if win[0] + j > K: nex[0] = i; break
            win[0] += j
        else:
            nex[0] = 0
        

        

        for start in xrange(1,N):
            win[start] = max(win[start-1] - g[start-1],0)
            
            for i in xrange_wrap(nex[start-1], start, N):
                #print start,i
                if win[start] + g[i] > K: nex[start] = i; break
                win[start] += g[i]
            nex[start] = i

        #print win,nex

        start = 0
        winsum = 0
        found = [False]*N
        cycle = False
        for r in xrange(R):
            if  found[start]:
                cycle = True
                break
            found[start] = True
            winsum += win[start]
            start = nex[start]

        if cycle:
            R -= r
            cycle = start
            cyclen = 0
            cycwin = 0
            while cyclen == 0 or start != cycle:
                #print start
                cyclen+=1
                cycwin += win[start]
                start = nex[start]

            #print "cycle: start, len, win, R: ", (cycle,cyclen,cycwin, R)
            
            winsum += cycwin * (R // cyclen)

            for r in xrange(R%cyclen):
                winsum += win[start]
                start = nex[start]
        
        print 'Case #%d: %d' % (t+1,winsum)

main()
sys.stdin.close()
sys.stdout.close()
