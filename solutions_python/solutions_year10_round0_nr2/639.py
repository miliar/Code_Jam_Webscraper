# fair warning.

import time
st = time.time()


# maybe thic cache will speed things up a tiny bit
#gcd_cache = {} # { (a,b): gcd } 

def gcd(a,b):
        # faster algorithms?
        
        #k = (a,b)
        #if k in gcd_cache:
        #        print '!MATCH!'
        #        return gcd_cache[k]
        
        while a:
                a, b = b%a, a

        #gcd_cache[k] = b
        return b



f = open('d:/jam/in2.txt')
C = int(f.next())

res = []

for cs in xrange(C):

        ss = f.next()[:-1].split(' ')
        N  = int(ss[0])
        Ti = [int(x) for x in ss[1:]]   # hopefully python handles the > 64bit automatically
 
        print 'cs:%d  @%.0f  >  N:%d' % (cs,time.time()-st,N),

        mn  = min(Ti)        

        # how many comparisons are really needed? this seems to work [O=N]       
        cd  = abs(Ti[0] - Ti[1])
        for i in range(1,N-1):     #map/reduce?
                dif = abs(Ti[i] - Ti[i+1])
                cd = gcd(cd,dif)


        # and finally:
        r = - (mn%(-cd))
        res.append(r)
        
        print
        #print '     > res:%d' % r        
#

f.close()



fw = open('d:/jam/ot2.txt', 'w')
for ix,r in enumerate(res):
        fw.write('Case #%d: %s\n' % (ix+1, r))
fw.close()


        
print 'fin @%.0f' % (time.time()-st)

        


        
        
