from collections import defaultdict as di
import math

q = int(input())
for case in range(1,q+1):
    n,p = [int(x) for x in input().split()]
    R = [int(x) for x in input().split()]
    vikt = di(list)
    for i in range(n):
        for g in [int(x) for x in input().split()]:
            tal = g/R[i]
            a = math.ceil(tal/1.1)
            b = math.floor(tal/0.9)
            #print("a,b",a,b)
            if a <= b:
                vikt[i].append((a,b))
        vikt[i].sort()
    #print(vikt)
    mat = 0
    index = [0]*n
    
    for port in range(1000000):
        for ind in vikt:
            while index[ind] < len(vikt[ind]) and vikt[ind][index[ind]][1] < port:
                index[ind]+=1

        not_enough_left = False

        for ind in vikt:
            if index[ind] == len(vikt[ind]):
                not_enough_left = True
        if not_enough_left or len(vikt)!=n:
            break
        
        k = 0
        pos = True
        while True:
            for ind in range(n):
                if index[ind] < len(vikt[ind]) and vikt[ind][index[ind]][0] <= port and vikt[ind][index[ind]][1] >= port:
                    pass
                else:
                    pos = False
            if pos == False:
                break
            else:
                k+=1
                for ind in range(n):
                    index[ind] += 1
        #print(port,"portion",k,"antal")
        mat += k
    print("Case #%d: %d" % (case, mat))
                
