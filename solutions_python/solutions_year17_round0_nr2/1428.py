import sys






def check(num):
    for i in range(len(num) - 1):
        if(num[i+1]>num[i]):
            return False
    return True
out=open("out.txt","w")
with open("input.txt","r") as f:
    n=int(f.readline().strip())
    for k in range(n):
        num=map(int,list(f.readline().strip()))
        num=num[::-1]
        #print (num)
        while( not check(num)):
            for i in range(len(num)-1):
                if(num[i+1]>num[i]):
                    num[i+1]=num[i+1]-1
                    for j in range(i,-1,-1):
                        num[j]=9
                    break
        num=num[::-1]

        print "Case #%d: %d" % (k+1,int(''.join(str(x) for x in num)))
        out.write("Case #%d: %d\n" % (k+1,int(''.join(str(x) for x in num))))


