from sys import stdout
from collections import defaultdict

ifile = open('../input/B-large.in', 'r')
#ifile = open('../input/B.x.in', 'r')
ofile = open('../output/B-large.out', 'w')
#ofile = stdout

cases = int(ifile.readline())

for case in xrange(cases):
    values = map(int, ifile.readline().split())
    l = values[0]
    t = values[1]
    n = values[2]
    c = values[3]
    a = values[4:]
    a = map(lambda x : 2*x, a)
    if len(a) > n:
        raise ValueError('Period')
    dist = {}    
    period = sum(a)    
    count, rem = divmod(n, c)
    #print count, rem
    for i, d in enumerate(a): 
        if d not in dist:
            dist[d] = 0
        dist[d] += count
        if i < rem:
            dist[d] += 1        
            
    #print dist
    pdiv, pmod = divmod(t, period)
    time = period * pdiv
    #print a    
    for i, d in enumerate(a):  
        #print i, d      
        dist[d] -= pdiv
        if pmod:
            dist[d] -= 1
            if dist[d] == 0:
                del dist[d]
            if d <= pmod:                
                pmod -= d
                time += d
            else:                
                if (d-pmod) not in dist:
                    dist[d-pmod] = 1
                else:
                    dist[d-pmod] += 1
                time += pmod
                pmod = 0
    #count in doubled time
    #print dist
    #print time  
    #print l
    time *= 2
    for d in reversed(sorted(dist.keys())):        
        if l == 0:
            break;
        if dist[d] <= l:
            time += dist[d] * d
            l -= dist[d]
            del dist[d]            
        else:
            time += l * d
            dist[d] -= l 
            l = 0;
    #normal speed    
    #print dist  
    #print time
    for d, count in dist.iteritems():
        time += d * count * 2    
    ofile.write('Case #%d: %d\n' % (case+1, time / 2))
        
    
    
    
    
    
    