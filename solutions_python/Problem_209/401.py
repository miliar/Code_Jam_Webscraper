import sys,math
'''
Consider each first pancake, then choose the set to top by sort rest of list by RH

'''

if __name__  == '__main__':
    xx = sys.stdin.readline()
    num = 0
    while True:
        line = sys.stdin.readline()
        if not line: break
        num += 1
        (n,k) = line.strip().split()
        n = int(n)
        k = int(k)
        cake = []
        side = {}
        for i in range(n):
            (ri,hi) = sys.stdin.readline().strip().split()
            ri = int(ri)
            hi = int(hi)
            cake.append( (ri,hi) )
            side[ (ri,hi) ] = -ri*hi
        cake.sort(reverse=True)
        #print 'all',cake

        max_syrup = 0
        for i in range(len(cake)):
            # consider starting with cake c
            first = cake[i]
            rest = cake[i+1:]
            rest.sort(key = lambda k: side[k])
            (r0,h0) = first
            syrup = r0*r0 + 2*r0*h0
            for (r0,h0) in rest[0:(k-1)]:
                syrup += 2*r0*h0
            syrup *= math.pi
            if syrup > max_syrup:
                max_syrup = syrup
            #print syrup
            #print first
            #print rest
            #print
            #print ki,ks[ki],tm
        #print slow_time
        #print d/slow_time
        #print

        print 'Case #'+str(num)+': '+str(max_syrup)
