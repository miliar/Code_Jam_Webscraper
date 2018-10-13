import sys

def check(n, pd, pg):
     
    for d in xrange(1, n + 1): #(n % 100) + 1):
        if (d * pd) % 100 == 0:
            wd = (d * pd) / 100 
       
            for g in xrange(d, d + 10000 + 1):
                if (g * pg) % 100 == 0 and g * pg / 100 >= wd and g - (g * pg / 100) >= (d - wd):
                    print d, g, wd, g * pg / 100
                    return 'Possible'
        
    return 'Broken'

f_name = sys.argv[1]
with open('%s.in' % f_name, 'r') as f_in:
    with open('%s.out' % f_name, 'w') as f_out:
        for i in xrange(int(f_in.readline().strip())):
            
            n, pd, pg = map(int, f_in.readline().strip().split(' '))
            print n, pd, pg
            result = check(n, pd, pg)    
            print result
                     
            f_out.write('Case #%s: %s\n' % (i + 1, result))
