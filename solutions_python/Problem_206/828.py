'''
Created on Apr 22, 2017

@author: gbenedisgrab
'''
def solve(d,n,h):
    maxt = 0
    for i in h:
        k = i[0]
        s = i[1]
        maxt=max(maxt,1.*(d-k) / s) 
    return str(d/maxt)

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
            
            D,N = map(int,next(fr).split())
            horses = []
            for i in range(N):
                k,s = map(int,next(fr).split())
                horses.append([k,s])
            ans = solve(D,N,horses)
            
            fo.write("Case #" + str(cs) + ": " + ans + '\n')
            if not final :
                print("Case #" + str(cs) + ": " + ans )

