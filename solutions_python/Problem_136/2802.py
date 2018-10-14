import fileinput
def time(imp,n):
    global F
    return (imp/(2+n*F))

def costo(x,n):
    global C
    if (x,n) in tab :
        return tab[(x,n)]
    else:
        coston=0
        if n==0:
            return time(x,0)
            tab[(x,0)]=time(x,0)
        else:
            #print("x ", x, "n ",n , "C " ,C)
            coston=time(x,n)+costo(C,n-1)
            tab[(x,n)]=coston

    return coston 

global C,F,X,tab

mini=0
leggi=fileinput.input()
numCases=(int)(leggi.readline())
for i in range(numCases):
    read=leggi.readline().split()
    tab={}
    C=float(read[0])
    F=float(read[1])
    X=float(read[2])
    ni=0
    cond=0
    while(cond==0):
        min=costo(X,ni)
        if costo(X,ni+1) > costo(X,ni) :
            cond=1
        else:
            ni+=1
    print("Case #"+str(i+1)+": "+"%.7f"% min)    


