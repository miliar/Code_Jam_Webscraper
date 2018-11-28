import sys
import os

if __name__=='__main__':
    fin = sys.stdin
    P = fin.readline()
    for case in xrange(int(P)):
        time = 0
        line = fin.readline()
        tokens = line.split()
        N = int(tokens[0])
        rob = {'O':1, 'B':1}
        tokens = tokens[1:]
        l = {'B':0, 'O':0}
        curr = None
        last = 0

        for t in range(0,N*2, 2):
            r = str(tokens[t]).strip()
            b = int(tokens[t+1])
#            print 'r,b, time', r,b, time
#            print 'rob[r], b', rob[r], b
            if rob[r] < b:
                m = b - rob[r]
            else:
                m = rob[r] - b
            rob[r] = b
            m += 1
#            print 'm', m
            if not curr or curr == r:
                time += m
                l[r] = time
#                print 1
            else:
#                print 2
                x = m - (time - l[r])
#                print 'x', x, 'time', time, 'l[r]', l[r]
                
                if x > 0:
                    time += x
                elif x == 0:
                    time +=1
                else:
                    if rob[r] == b:
                        time += 1
#                    print x

            l[r] = time
#            print 'r', r, 'l[r]', l[r]
            curr = r
        print 'Case #%d:' % (case+1), time
