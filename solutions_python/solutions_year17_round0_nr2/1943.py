def parse(a):
    down=0
    up=0
    for i in range(1,len(a)):
        if a[i]>a[i-1]:
            up=i
        if a[i]<a[i-1]:
            down=i
            break
    if down ==0:
        return a
    elif up==0 and a[0]=='1':
        return '9'*(len(a)-1)
    else:
        return a[:up]+str(int(a[up])-1)+'9'*(len(a)-1-up)
N=int(input())
for c in range(1,N+1):
    a=input()
    print("Case #{}: {}".format(c,parse(a)))
    
