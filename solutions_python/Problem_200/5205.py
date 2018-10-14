T=int(input())
for j in range (T):
    n=int(input())
    while(n>0):
        y=[]
        x=[int(d) for d in str(n)]
        y=x
        s=sorted(y,key=int)
        if(x==s):
            print ("Case #",j+1,": ",*x,sep='')
            break
        else:
            n=n-1
            continue
