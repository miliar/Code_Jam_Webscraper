t=int(input())
for x in range(t):
    l=input()
    m=l.split(' ')
    (a,b)=int(m[0]),int(m[1])
    r=[1,4,9,121,484]
    flag=0
    for y in range(5):
        if r[y]>=a and flag==0:
            for z in range(y,5):
                if r[z]>b and flag==0:
                    print("Case #"+str(x+1)+": "+str(z-y))
                    flag=1
                if b>=484 and flag==0:
                    z=4
                    print("Case #"+str(x+1)+": "+str(z-y+1))
                    flag=1
        if a>484 and flag==0:
            print("Case #"+str(x+1)+": 0")
            flag=1           
    
