import sys
import math

inputFileName="input.in"
outputFileName="output.out"

fi=open(inputFileName,"r")
fo=open(outputFileName,"w")

T=int(fi.readline())

def maxString(splits):
    maxv=0
    string=""
    for ob in splits:
        if(len(ob)>maxv):
            maxv=len(ob)
            string=ob
    return string

def getLsRs(index,stalls):
    left,right=stalls[:index],stalls[index+1:]
    ls=len(left)
    rs=len(right)
    print("ls"+str(ls))
    print("rs"+str(rs))
    return ls,rs

def compute(ncells,npeople):
    A=0
    B=0
    mindex=0
    stalls="".join(map(str,[1]+[0]*int(ncells)+[1]))
    for i in range(0,int(npeople)):
        splits=stalls.split("1")
        biggestString=maxString(splits)
        print biggestString
        index=int(math.ceil(len(biggestString)/2.))-1
        print("Index: "+str(index))
        newbiggestString=biggestString[:index]+"1"+biggestString[index+1:]
        stalls=stalls.replace(biggestString,newbiggestString,1)
        A,B=getLsRs(index,newbiggestString)
        print stalls
    if(A<B):
        A,B=B,A
    return str(A)+" "+str(B)

map(lambda i:fo.write("Case #"+str(i+1)+": "+compute(*fi.readline().strip().split(" "))+"\n"),range(T))
