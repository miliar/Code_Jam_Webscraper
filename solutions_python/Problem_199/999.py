'''
Created on Apr 7, 2017

@author: gbenedisgrab
'''
def flip(ps,start,k):
    chars = list(ps)
    for i in range(k):
        if chars[i+start] == "+":
            chars[i+start] = '-'
        else:
            chars[i+start] = '+'
    return ''.join(chars)
def solve(ps,k):
    count = 0
    for i in range(len(ps)-k+1):
        if ps[i] == '-':
            ps = flip(ps,i,k)
            count +=1
    for i in range(k-1):
        if ps[len(ps)-k+1+i] == '-':
            return "IMPOSSIBLE"
    return str(count)

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
            
            PS,K = next(fr).split()
            ans = solve(PS,int(K))
            
            fo.write("Case #" + str(cs) + ": " + ans + '\n')
            if not final :
                print("Case #" + str(cs) + ": " + ans )

