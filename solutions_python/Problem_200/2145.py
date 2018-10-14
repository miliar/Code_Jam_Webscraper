import sys

inputFileName="input.in"
outputFileName="output.out"

fi=open(inputFileName,"r")
fo=open(outputFileName,"w")

T=int(fi.readline())

def subOrdered(number):
    for i in range(1,len(number)):
        if(number[i]<number[i-1]):
            return number[:i],number[i:]
    return number,[]

def compute(number):
    number=map(lambda n:int(n),list(number))
    ordered,rest=subOrdered(number)
    while(rest!=[]):
        rest=[9]*len(rest)
        ordered[-1]=ordered[-1]-1
        ordered,rest=subOrdered(ordered+rest)
    return str(int("".join(map(str,ordered))))

map(lambda i:fo.write("Case #"+str(i+1)+": "+compute(fi.readline().strip())+"\n"),range(T))
