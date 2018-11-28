

import sys


if __name__=="__main__":
    fname = sys.argv[1]
    f = open(fname)
    gname = sys.argv[2]
    g = open(gname,'w')
    T  = int(f.readline())
    print T
    c=0
    for i in xrange(T):
        line = f.readline().strip()
        n=int(line)
        line = f.readline().strip()
        line = line.split(' ')
        to_solve = map(int, line)
        if len(to_solve) != n:
            print to_solve
            print n
            print "something stinks"
            sys.exit(1)
        xor = s = 0
        m=to_solve[0]
        for i in to_solve:
            xor^=i
            if i < m:
                m=i
            s+=i
        if xor != 0:
            rez = 'NO'
        else:
            rez = s-m
        c+=1
        g.write('Case #%d: %s\n' % (c, rez))
 
