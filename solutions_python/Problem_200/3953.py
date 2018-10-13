n = int(input())
for i in range(n):
    p = input()
    p = int(p)
    for j in range(p,0,-1):
        c=0
        q = list(str(j))
        #print(len(q))
        for k in range(len(q)-1):
            #print(q[j],q[j+1])
            if q[k]>q[k+1]:
                #print("a")
                c =1
        if c==0:
            print("Case #{}: {}".format(i+1, j))
            break
        
            
