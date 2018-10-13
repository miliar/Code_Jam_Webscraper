
q=int(input())
for z in range(0,q):
    a=int(input())
    while 1:
        s=str(a)
        for i in range(0,len(s)-1):
            if s[i]>s[i+1]:
                a-=1
                break
        else:
            print("Case #"+str(z+1)+":",a)
            break