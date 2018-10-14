'''
Created on <DATE>
Code Jam <YEAR> <ROUND> <PROBLEM>
@author: manolo
'''

import sys
ifile = sys.stdin
ofile = open('./b.out', 'w')

def r():
    return ifile.readline()[:-1]
    
def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))

T = int(r())
for case in range(1,T+1):
    (C, F, X) = r().split(' ')
    c = float(C)
    f = float(F)
    x = float(X)
    
    cps = float(2)
    passed_t = float(0)
    total_t = float(0)
    rest_t = x / cps # time to have all cookies
    total_t = passed_t + rest_t
    
    farm_t = c / cps # time to be able to buy a farm
    next_rest_t = x / (cps + f)

    if rest_t <= (farm_t + next_rest_t):
        w(case, total_t)
        continue

    n_farms = 0
    while True:
    
        n_farms = n_farms +1
        
        cps = cps + f
        passed_t = passed_t + farm_t
        rest_t = x / cps # time to have all cookies
        total_t = passed_t + rest_t
        
        farm_t = c / cps
        next_rest_t = x / (cps + f)
        if rest_t <= (farm_t + next_rest_t):
            break
            
    w(case, total_t)
        
ofile.close

