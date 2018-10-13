#! /usr/bin/python
import sys
mainD={}
    
def main():
    file1=open(sys.argv[1])
    a=file1.readlines()
    cases=int(a.pop(0))
    values=[]
    a.reverse()
    while len(a)>0:
        mainD={}
        values.append(0)
        blah=a.pop().split()
        N=int(blah[0])
        M=int(blah[1])
        Nlist=[]
        Mlist=[]
        for x in range(N):
            Nlist.append(a.pop())
            Nlist[x]=Nlist[x].split()
            Nlist[x]=Nlist[x][0].split("/")
            Nlist[x].pop(0)
            gahgah=''
            for y in Nlist[x]:
                    
                gahgah+="/"+y
                mainD[gahgah]=True
                
        for x in range(M):
            Mlist.append(a.pop())
            Mlist[x]=Mlist[x].split()
            Mlist[x]=Mlist[x][0].split("/")
            Mlist[x].pop(0)
            if len(values)==19:
                print Mlist
            gahgah=''
            for y in Mlist[x]:
                gahgah+="/"+y
                if len(values)==19:
                    print gahgah
                try:
                    if mainD[gahgah]:
                        values[len(values)-1]+=0
                except:
                    if len(values)==19:
                        print "reached"
                    values[len(values)-1]+=1
                    mainD[gahgah]=True

        

    strings=[]
    for x in range(cases):
        string1="Case #"+str(x+1)
        string1+=": "+str(values[x])        
        strings.append(string1)
    f=open("OutputLarge.txt","w")
    for x in strings:
        f.write(x+"\n")
    




if __name__ == "__main__":
    main()


