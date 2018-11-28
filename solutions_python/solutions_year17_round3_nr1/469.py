'''
Created on Apr 30, 2017

@author: gbenedisgrab
'''
import math
def solve(k,pan): 
    calc = []
    for i in pan:
        calc.append([2*math.pi*i[0]*i[1],i[0]])
    calc = sorted(calc,key=lambda x: -x[0])
    calc2 = list(calc)
    bigr,c = 0,[]
    for i in calc2:
        if bigr<i[1]:
            bigr = i[1]
            c = i
    calc2.remove(c)
    calc = calc[:k]
    calc2 = calc2[:(k-1)]
    calc2.append(c)
    
    bigr,val1,val2=0,0,0
    for i in calc:
        val1+=i[0]
        bigr=max(bigr,i[1]) 
    for i in calc2:
        val2+=i[0]     
    val2+= math.pi*c[1]**2
    val1+= math.pi*bigr**2
    
    return max(val1,val2)

#########################  FORMATTING ##########################

final = True;
name = 'A-large'
#name = 'A-large'
if final : 
    file_out = name + '.out'
    file_in = name + '.in'
else :
    file_out = 'out.txt'
    file_in = 'in.txt'
    

with open(file_in, 'r') as fr :
    with open(file_out, 'w') as fo:
        t = int(next(fr)) #comment 
        for cs in range(1, t + 1):
            
            ######  get my code for getting the input here #########
            N,K = map(int,next(fr).split())
            PANCAKES = []
            for i in range(N):
                R,H = map(int,next(fr).split())
                PANCAKES.append([R,H])
            ans = solve(K,PANCAKES)
            
            fo.write("Case #" + str(cs) + ": %.7f" % ans +'\n')
            if not final :
                print("Case #" + str(cs) + ": %.7f" % ans)

