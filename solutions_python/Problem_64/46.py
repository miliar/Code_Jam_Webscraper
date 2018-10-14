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
        valDict={}
        blah=a.pop().split()
        M=int(blah[0])
        N=int(blah[1])
        darr=[]
        for x in range(M):
            darr.append(stringToArray(a.pop().split()[0]))
        

        while not finished(darr):
            count=dCounts(darr)
                
            try:
                valDict[count]=valDict[count]+1
            except:
                valDict[count]=1
        num=len(valDict.keys())
        pairs=[]
        hello=valDict.keys()
        hello.sort()
        hello.reverse()
        for x in hello:
            pairs.append((x,valDict[x]))
        values.append((num,pairs))
            


    strings=[]
    for x in range(cases):
        string1="Case #"+str(x+1)
        string1+=": "+str(values[x][0])        
        strings.append(string1)
        for y in range(values[x][0]):
            string1=str(values[x][1][y][0])+" "+str(values[x][1][y][1])
            strings.append(string1)
        
    f=open("OutputLarge.txt","w")
    for x in strings:
        f.write(x+"\n")
    




def finished(darr):
    count=0
    for i in range(len(darr)):
        for j in range(len(darr[0])):
            count+=darr[i][j]
    return count==(-1*len(darr)*len(darr[0]))
    

def dCounts(darr):
    countArr=[]
    for i in range(len(darr)):
        countArr.append([])
        for j in range(len(darr[0])):
            countArr[i].append(0)
    for i in range(len(darr)):
        for j in range(len(darr[0])):
            if i==0 or j==0:
                if darr[i][j]>=0:
                    countArr[i][j]=1
                    
            elif darr[i][j]==0:
                if darr[i][j-1]==1 and darr[i-1][j]==1 and darr[i-1][j-1]==0:
                    countArr[i][j]=1+min(countArr[i-1][j-1],countArr[i][j-1],countArr[i-1][j])
                else:
                    countArr[i][j]=1

            elif darr[i][j]==1:
                if darr[i][j-1]==0 and darr[i-1][j]==0 and darr[i-1][j-1]==1:
                    countArr[i][j]=1+min(countArr[i-1][j-1],countArr[i][j-1],countArr[i-1][j])
                else:
                    countArr[i][j]=1
    

    maxval=0
    maxi=-1
    maxj=-1
    for i in range(len(darr)):
        for j in range(len(darr[0])):
            if countArr[i][j]>maxval:
                maxval=countArr[i][j]
                maxi=i
                maxj=j
    for i in range(maxi-maxval+1,maxi+1):
        for j in range(maxj-maxval+1,maxj+1):
            darr[i][j]=-1
    return maxval
        
    
                
    
            
        
def stringToArray(string):
    leng=len(string)
    blah=[]
    for x in range(leng):
        if string[x]=="0":
            blah=blah+[0,0,0,0]
        if string[x]=="1":
            blah=blah+[0,0,0,1]
        if string[x]=="2":
            blah=blah+[0,0,1,0]
        if string[x]=="3":
            blah=blah+[0,0,1,1]
        if string[x]=="4":
            blah=blah+[0,1,0,0]
        if string[x]=="5":
            blah=blah+[0,1,0,1]
        if string[x]=="6":
            blah=blah+[0,1,1,0]
        if string[x]=="7":
            blah=blah+[0,1,1,1]
        if string[x]=="8":
            blah=blah+[1,0,0,0]
        if string[x]=="9":
            blah=blah+[1,0,0,1]
        if string[x]=="A":
            blah=blah+[1,0,1,0]
        if string[x]=="B":
            blah=blah+[1,0,1,1]
        if string[x]=="C":
            blah=blah+[1,1,0,0]
        if string[x]=="D":
            blah=blah+[1,1,0,1]
        if string[x]=="E":
            blah=blah+[1,1,1,0]
        if string[x]=="F":
            blah=blah+[1,1,1,1]
    return blah
        

if __name__ == "__main__":
    main()


