cases=int(input())
for case in range(1, cases+1):
    n=input().split()
    no=[]
    flag=False
    no+=[int(i) for i in n]
    no.pop(0)
    no.sort(reverse=True)
    for i in range(1,2**20):
        num1=bin(i)
        num1=num1[2:]
        num1=num1.rjust(20,'0')
        s=0
        for k in range(len(num1)):
            if num1[k]=='1':
                s+=no[k]
                
        for j in range(1,2**20):
            if i==j:
                continue
            s2=0
            num=bin(j)
            num=num[2:]
            num=num.rjust(20,'0')
            for k in range(len(num)):
                if num[k]=='1':
                    s2+=no[k]
            if s2>s:
                break
            elif s2==s:
                flag=True
                break
        if flag:
            break
    if flag:
        print ('Case #%d:' % (case))
        for k in range(len(num1)):
            if num1[k]=='1':
                print(no[k],end=' ')
        print()
        for k in range(len(num)):
            if num[k]=='1':
                print(no[k], end=' ')
        print()
    else:
        print ('Case #%d:' % (case))
        print("Impossible")
        
