import copy

#________________________________________________________________
def convert():
        f=open('B-small-attempt8.txt','r')
        x=[]
        j=0
        for i in range(0,101):
            x.append(int(f.readline()))
        return x[1:]
#_________________________________________________________________
def istidy(N):
        x=[]
        temp=N
        while temp>0 :
            x.append(temp%10)
            temp=temp/10
        x=x[::-1]
        y=copy.deepcopy(x)
        y.sort()
        l=len(x)
        if x[l-1]!=0:
            if x==y:
                return 1
            else:
                return 0
        else :
            return 0

#_________________________________________________________________
def largesttidy(N):
    l=0
    for i in range(1,N+1):
        if(istidy(i)):
            l=i
    return l

#_________________________________________________________________
def mainprog(q):
        p=1
        for i in q:
                print "Case #%d:"%p,largesttidy(i)
                p=p+1
mainprog(convert())
