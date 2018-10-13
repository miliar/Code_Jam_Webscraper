from collections import deque

T = int(raw_input())

for j in range(1,T+1):
    
    C = int(raw_input())
    S = map(int, raw_input().split(' '))
    #S = str.split(raw_input())
    sean1 = sean2 = 0
    pat = 0
    values = []
    S.sort()
    for i in range(0,C):
        
        for p in range (0, i+1):
            pat = pat ^ int(S[p])
        
        for s in range(i+1,C):
            sean1 = sean1 + int(S[s])
            sean2 = sean2 ^ int(S[s])
        if(pat==sean2):
            values.append(sean1)
            pat=0
            sean1 = sean2 = 0
        else:
            pat=0
            sean1 = sean2 = 0
    if(not values):
        result = 'NO'
    else:
        values.sort()
        values.reverse()
        result = values[0]
    print "Case #"+str(j)+": "+str(result)
            
        