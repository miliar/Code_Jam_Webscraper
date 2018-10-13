#! /usr/bin/python
import sys
    
def main():
    file1=open(sys.argv[1])
    a=file1.readlines()
    cases=int(a.pop(0))
    values=[]
    a.reverse()
    while len(a)>0:
        values.append(0)
        blah=a.pop().split()
        N=int(blah[0])
        K=int(blah[1])
        B=int(blah[2])
        T=int(blah[3])
        Xe=a.pop().split()
        XV=[]
        Ve=a.pop().split()
        
        for x in range(N):
           XV.append((int(Xe[x]),int(Ve[x])))
        
        Ve=[]
        Xe=[]
        
        finishT=[]
        count=0
        finishOT=[]
        for x in range(len(XV)):
            finishT.append(float(B-XV[x][0])/float(XV[x][1]))
            if finishT[x]<=T:
                count+=1
                finishOT.append(True)
            else:
                finishOT.append(False)
                


        trueVar=(count>=K)
        KCount=0
        count=0
        if trueVar:
            finishOT.reverse()
            x=0
            
            while KCount<K:
                if finishOT[x]:
                    KCount+=1
                    
                    values[len(values)-1]+=count
                else:
                    count+=1
                    
                x+=1
                
        else:
            values[len(values)-1]="IMPOSSIBLE"

        
        
        
    
    
    strings=[]
    for x in range(cases):
        string1="Case #"+str(x+1)
        string1+=": "+str(values[x])        
        strings.append(string1)
    f=open("OutputLarge.txt","w")
    for x in strings:
        f.write(x+"\n")
    
    

def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)
    
if __name__ == "__main__":
    main()


