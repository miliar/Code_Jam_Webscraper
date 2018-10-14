'''
Created on Apr 7, 2017

@author: gbenedisgrab
'''
def solve(n):
    print n
    borrow = False
    s=str(n)
    pos = -1
    if len(s) == 1 : return s
    for i in range(len(s)-2,-1,-1):
        if int(s[i]) > int(s[i+1]) :
            pos =i
            borrow = True
        elif int(s[i]) == int(s[i+1]) and borrow:
            pos = i
        else:
            borrow = False
    if pos<0: return s
    last_tidy = s[:pos] +str(int(s[pos])-1) +'9'*(len(s)-pos-1)
    if last_tidy[0] == '0': return last_tidy[1:]
    return last_tidy

#########################  FORMATTING ##########################

final = True;
name = 'B-large'
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
            
            N = int(next(fr))
            ans = solve(N)
            
            fo.write("Case #" + str(cs) + ": " + ans + '\n')
            if not final :
                print("Case #" + str(cs) + ": " + ans )

