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
        blah=a.pop().split()
        num=int(blah[0])
        XY=[]

        for x in range(num):
            blah=a.pop().split()
            b=int(blah[0])
            c=int(blah[1])
            XY.append((b,c))
        values.append(findval(XY))
            


    strings=[]
    for x in range(cases):
        string1="Case #"+str(x+1)
        string1+=": "+str(values[x])        
        strings.append(string1)
    f=open("OutputLarge.txt","w")
    for x in strings:
        f.write(x+"\n")
    


def findval(XY):
    if len( XY)==1:
        return 0
    if len(XY)==2:
        if XY[0][0]>XY[1][0] and XY[0][1]<XY[1][1] or XY[0][0]<XY[1][0] and XY[0][1]>XY[1][1]:
            return 1
        return 0
    count=0
    for i in range(len(XY)):
        for j in range(i+1,len(XY)):
            if XY[i][0]>XY[j][0] and XY[i][1]<XY[j][1] or XY[i][0]<XY[j][0] and XY[i][1]>XY[j][1]:
                count+=1
    return count
                


if __name__ == "__main__":
    main()


