
from pylab import *
import StringIO
import heapq


class Case():
    def __init__(self, input):
        self.num=int(input.readline())
        self.vec = [int(x) for x in input.readline().split(' ')]
        self.vec.sort()

    def dosweep(self):
        myh=[]

        s = -sum(c.vec)
        x1 = 0
        x2 = reduce(bitwise_xor, c.vec)

        for k in range(len(self.vec)):
            v = self.vec[k]
            ns = s + v
            nx1 = x1 ^ v
            nx2 = x2 ^ v

            nvec = self.vec[:]
            nvec.pop(k)

            souts = [k]

            heapq.heappush(myh, (ns,nx1,nx2,
                                 souts) )

        while myh:
            s, x1, x2, outs = heapq.heappop(myh)
            if x1==x2:
                return '%d'%-s
                #print '***'
            # else:
            #     print '   '
            # print s,x1,x2,outs ## for debuging

            ## Neighbors to visit
            for k in range(len(self.vec)):
                if outs!=[] and k <= max(outs):
                    continue
                v = self.vec[k]
                ns = s + v
                nx1 = x1 ^ v
                nx2 = x2 ^ v

                nvec = self.vec[:]
                nvec.pop(k)

                souts = outs+[k]

                heapq.heappush(myh, (ns,nx1,nx2,
                                     souts) )
        
        return "NO"

            

fil = open(sys.argv[1])
Ncases = int(fil.readline())
for case in range(1,1+Ncases):

    print 'Case #%d:'%case,
    c = Case(fil)
    # print c.vec
    print c.dosweep()
    # print





