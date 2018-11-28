from sets import Set
def shift(tmp):
    return tmp[-1]+tmp[0:-1]
f=open("C-small-attempt1.in","r")
#f=open("in","r")
n=int(f.readline())

for i in range(n):
    A,B=f.readline().split(' ')
    cout=0
    
    for j in range(int(A),int(B)+1):
        tmp=str(j)
        arr=Set([]) 
        for k in range(len(tmp)):
            tmp=shift(tmp)
            if(j<int(tmp) and int(tmp)<=int(B) and tmp not in arr):
                #print j,tmp
                arr.add(tmp)
                cout+=1
    print "Case #"+str(i+1)+": "+str(cout)

