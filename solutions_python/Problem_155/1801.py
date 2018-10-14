'''
Created on 11 apr 2015

@author: algestam
'''

def solve(max, audience): 
    a = 0
    adds = 0
        
    for i, x in enumerate(audience):
        x = int(x)
        if not i == max:
            a -= 1
            a = a + x
            if a < 0:
                adds += abs(a)
                a = 0
        #print i, x, a, adds
    
    return adds
    

for case in xrange(input()):
    MAX, audience = raw_input().split()
    
    res = solve(int(MAX), audience)

    print "Case #%i: %d" % (case+1, res)
    