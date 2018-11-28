#! /usr/bin/env python
import sys

# parsing input for a case

## first line
def process1(line):
    arr = line.split()
    return int(arr[0]),int(arr[1]),int(arr[2])

## second line
def process2(line):
    arr = line.split()
    arrout = []
    for t in arr:
        arrout.append(int(t))
    return arrout


#computation

## money and change in array for a round
def permute(arr,n,N):
    arr1 = arr[n:]
    arr2 = arr[:n]
    return arr1+arr2

def data(k,N,arr):
    n,s=0,0
    for i in range(N):
        if (s + arr[i] <=k):
            s+=arr[i]
            n+=1
        else:
            break
    return n,s

def process(k,N,arr):# N = len(arr)
    n,m = data(k,N,arr)#nb of groups, money
    array = permute(arr,n,N)
    return m,array

## money for a case
def money(R,k,N,arr):
    sum = 0
    for i in range(R):
        s,arr = process(k,N,arr)
        sum += s
    return sum

## main function for the process of a case
def caseprocess(f,i):
    line1 = f.readline()
    R,k,N = process1(line1)
    line2 = f.readline()
    arr = process2(line2)
    eur = money(R,k,N,arr)
    return "Case #%d: %d\n" % (i+1,eur)
        
# to have a nice name
def getfilename():
    args = sys.argv
    n = len(args)
    if n>1:
        return args[1]

# main
if __name__=='__main__':
    input = getfilename()
    name = input[:-3]
    output = name+".out"
    f = open(input,'r')
    l=f.readline()
    arr = l.split()
    t = int(arr[0])
    o = open(output,'w')
    for i in range(t):
        oline = caseprocess(f,i)
        #print oline
        o.write(oline)
    o.close()
    f.close()
