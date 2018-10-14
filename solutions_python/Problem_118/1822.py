n=int(input())
for j in range(n):
    a,b=map(int,input().split())
    k=0
    for i in range(4):
        if a<=i*i<=b:
            k+=1
    for i in range(1,1000):
        for ch in ['','0','1','2']:
            s=int(str(i)+ch+str(i)[::-1])
            p=str(s*s)[::-1] 
            if str(s*s)==p:
                if a<=int(p)<=b:             
                    k+=1
            if s*s>b: break    
    print('Case #'+str(j+1)+':',k)