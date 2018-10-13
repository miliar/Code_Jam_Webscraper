def palindrom(n):
    a=n
    b=0
    while(n>0):
        b=b*10+(n%10)
        n=n/10
    if(a==b):
        return 1
    elif (a!=b):
        return 0

def squareroot(n):
    i=1
    while i<=n:
        if i**2 == n:
            return i
        i=i+1
    return -1

def fandsq(a,b):
    i=a
    c=0
    while i<=b:
        if(palindrom(i)==1):
            n=squareroot(i)
            if(n!=-1):
                if(palindrom(n)==1):
                    c=c+1
        i=i+1
        
    return c

def rang():
    infile=file("G:\ONLINE COURSES\Google Code Jam 2013\CSIN.IN",'r')
    whole=infile.readlines()
    infile.close()
    n=int(whole[0])
    i=1
    count=[]
    while i<=n:
        ran=whole[i].split()
        a=int(ran[0])
        b=int(ran[1])
        count.append(fandsq(a,b))
        i=i+1
    i=0
    while i<n:
        print"Case #"+str(i+1)+": "+str(count[i])
        i=i+1
    
               

if __name__=="__main__":
    rang()
