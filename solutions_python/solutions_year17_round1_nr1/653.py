'''
Created on Apr 14, 2017

@author: gbenedisgrab
'''
def solve(r,c,cake):
    final = []
    for i in range(r):
        cur = '?'
        for j in range(c):
            if cake[i][j] == '?':
                if cur <> '?': 
                    cake[i][j] = cur
            else:
                cur = cake[i][j]
                for k in range(j-1,-1,-1): # check left
                    if cake[i][k] == '?':
                        cake[i][k] = cur
    count = 0
    last = []
    for i in range(r):
        if cake[i][0] == '?':
            if last == []:
                count +=1
            else:
                final.append(last)
        else:
            last = cake[i]
            for j in range(count):
                final.append(last)
            count =0
            final.append(last)
                        
    for i in range(r):
        s=''.join(final[i])
        fo.write(s + '\n')    
        print(s)
    return

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
            CAKE=[]
            R,C = map(int,next(fr).split())
            for i in range(R):
                CAKE.append(list(next(fr).strip())) 
                
            fo.write("Case #" + str(cs) + ":"+ '\n')
            if not final :
                print("Case #" + str(cs) + ":")
                
            solve(R,C,CAKE)
            
            

