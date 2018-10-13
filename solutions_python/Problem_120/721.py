import math
dict = {}

def read(f):
    line = f.readline()
    data = [int(i) for i in line.split()]
    return data 

def work(data):
    t = data[1]
    r = data[0]
    result = 0
    
    k = 1
    x = need(r,k)
    
    while(t>x/2):
        k = 2*k
        x = need(r,k)
        
    while(t<x):
        k = int(0.9*k)
        x = need(r,k)
        
    while(t>x):
        k+= 1
        x = need(r,k)
    if t == need (r,k):
        return k
    else:
        return k-1

def need(r,k):
    return 2*k*r+k+(2*k-2)*k

def main():
    f = open("input.txt")
    counter = int(f.readline())
    case = 1
    while case<= counter:
        result = work(read(f))
        print "Case #%s: %s"%(case,result)
        case +=1
        
main()