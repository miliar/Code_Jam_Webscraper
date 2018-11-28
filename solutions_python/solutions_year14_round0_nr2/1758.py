#!/usr/bin/python
with open('B-small-attempt1.in') as fIn:
    n_case = int(fIn.readline())
    for i in range(n_case):
        [c, f, x] = fIn.readline().split()
        c = float(c)
        f = float(f)
        x = float(x)
        #print '============',c,f,x,'============='
        total_time = []
        for j in range(int(x/c)+10):
            t = x/(2+j*f)
            if j > 0:
                for k in range(1,j+1):
                    t = t + c/(2+(k-1)*f)
            #print t,k,j
            total_time.append(t)
        t_minimum = min(total_time)
        print 'Case #{0}:'.format(i+1), '%10.7f'%t_minimum

# <codecell>


