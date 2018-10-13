t=input()
for i in range(t):
    y=input()
    temp1=y
    for x in range(y,0,-1):
        flag=0
        temp=x
        while x>0:
            while x>0:
                if x%10<((x/10)%10):
                    flag=1
                    break
                else:
                    x=x/10
            x=x-1
        if flag==0:
            print "Case #"+str(i+1)+": "+str(temp) 
            break
