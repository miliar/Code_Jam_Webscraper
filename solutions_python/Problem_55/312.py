#! /usr/bin/python
import sys
    
def main():
    file1=open(sys.argv[1])
    a=file1.readlines()
    cases=int(a.pop(0))
    rkn=[]
    sizes=[]
    values=[]
    for x in range(2*cases):
        if x%2==0:
            rkn.append(a[x].split())
            for y in range(len(rkn[x/2])):
                rkn[x/2][y]=int(rkn[x/2][y])
        else:
            sizes.append(a[x].split())
            for y in range(len(sizes[x/2])):
                sizes[x/2][y]=int(sizes[x/2][y])

    for x in range(len(rkn)):
        values.append(numtimes(rkn[x][0],rkn[x][1],sizes[x]))
    
    strings=[]
    for x in range(cases):
        string1="Case #"+str(x+1)
        string1+=": "+str(values[x])        
        strings.append(string1)
    f=open("Output.txt","w")
    for x in strings:
        f.write(x+"\n")
    
    

def numtimes(R,K,list1):
    sumv=0
    index=0
    for x in range(R):
        (tempsumv,index)=iterate(K,list1,index)
        sumv+=tempsumv
    return sumv

def iterate(K,list1,index):
    sumv=0
    orig=index
    if K>=list1[index]:
        sumv+=list1[index]
        K-=list1[index]
        index=(index+1)%len(list1)

    while K>=list1[index] and orig<>index:
        sumv+=list1[index]
        K-=list1[index]
        index=(index+1)%len(list1)
    return sumv,index
    

if __name__ == "__main__":
    main()


