'''
Created on Apr 7, 2017

@author: gbenedisgrab
'''

def insert(spa,item):
    lo=0
    hi = len(spa)
    while lo < hi:
        mid = (lo+hi)//2
        midval = spa[mid][0]
        if midval < item:
            lo = mid+1
        elif midval > item: 
            hi = mid
        else:
            spa[mid][1]+=1
            return
    spa.insert(lo,[item,1])

def solve(n,k):
    spaces = [[n,1]]
    for i in range(k-1):
        top = spaces[-1][0]
        if spaces[-1][1]==1:
            spaces.pop()
        else:
            spaces[-1][1]-=1
        insert(spaces,(top-1)/2)
        insert(spaces,top/2)
    top = spaces[-1][0]       
    return str(top/2) + " " +str((top-1)/2)

#########################  FORMATTING ##########################

final = True;
name = 'C-small-2-attempt0'
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
            ans = solve(N,K)
            
            fo.write("Case #" + str(cs) + ": " + ans + '\n')
            if not final :
                print("Case #" + str(cs) + ": " + ans )


