'''
Created on 12-Apr-2014

@author: raju
'''
out = open('/home/raju/Downloads/B-large.out','w')
with open('/home/raju/Downloads/B-large.in') as f:
    t = int(f.readline())
    for i in xrange(t):
        C, F, X = map(float, f.readline().split())
        res = 0.0
        rate = 2.0
        prev = 0
        next1 = 0
        while True:
            prev = res + (X/rate)
            res += (C/rate)
            rate += F
            next1 = res + (X/rate)
            if prev < next1:
                break
        out.write('case #'+str(i+1)+': '+ str(round(prev,7)))
        out.write('\n')