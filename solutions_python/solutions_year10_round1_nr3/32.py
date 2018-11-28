import psyco
psyco.full()

name = 'C-small-attempt0'
f = open(name+'.in')
fo = open(name + '.out','w')

T = int(f.next().strip())

for t in xrange(T):
    A1,A2,B1,B2 = [int(x) for x in f.next().strip().split()]
    tot = 0
    
    for A in xrange(A1,A2+1):
        for B in xrange(B1,B2+1):
            x = max(A,B)
            y = min(A,B)
            if x - y > y:
                tot += 1
            else:
                whose = False
                while x != y:
                    x -= y
                    x,y = y,x
                    if x - y > y:
                        break
                    whose = not whose
                if whose:
                    tot += 1
                
                
    fo.write('Case #%d: %d\n'%(t+1,tot))

f.close()
fo.close()
