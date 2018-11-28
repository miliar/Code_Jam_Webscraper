import math



def divide(Len):    
    L = int(math.ceil(float(Len) / 2) - 1)
    R = int(math.floor(float(Len) / 2))
    #print Len
    #print L
    #print R
    return L, R

def flow(N, K):
    #q = [N]
    dic = {N : 1}
    minLR = 0
    maxLR = 0 
    for i in range(0,K):
        maxLen = max(dic.keys())
        dic[maxLen] -= 1
        if dic[maxLen] == 0:
            del dic[maxLen]
        L,R = divide(maxLen)
        minLR = min(L, R)
        maxLR = max(L, R)
        if L not in dic:
            dic[L] = 1
        else:
            dic[L] += 1
        if R not in dic:
            dic[R] = 1
        else:
            dic[R] += 1
        
        
        
    return str(maxLR) +  " " + str(minLR)
    
f = open("C-small-2-attempt1.in", "r")

T = int(f.readline())

for x in range(0, T):
    readline = f.readline().strip()
    N, K = readline.split(" ")    
    print "Case #" + str(x+1) + ": " + flow(int(N), int(K))