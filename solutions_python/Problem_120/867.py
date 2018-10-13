def solve(r,t):
    c=0
    p=1+(2*r)
    while p<=t :
        t=t-p
        p=p+4
        c=c+1
       # print (c)
    return c

f=open("answer_circles.txt","w")
T=int(input())
for i in range(1,T+1):
    r,t=map(int,input().split())
    f.write("Case #"+str(i)+": "+str(solve(r,t))+"\n")
        
                
f.close()