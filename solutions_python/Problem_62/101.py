#! /usr/bin/env python
import sys

# parsing input for a case

def read_line_int(f):
    line = f.readline()
    arr = line.split()
    t = [int(i) for i in arr]
    return t

   

     
# to have a nice name
def getfilename():
    args = sys.argv
    n = len(args)
    if n>1:
        return args[1]




def wire(f):
    t = read_line_int(f)
    N = t[0]#directories existing
    #print N
    M = t[1]#dir to create 
    #print M
    return (N,M)


def nb_wire(f):
    t =  read_line_int(f)
    #print "nb de cables %d"%t[0]
    return t[0]


def info(f,N):
    arr = []
    for i in range(N):
        arr.append(wire(f))
    return arr


def count(a,b,l):
    c = 0
    for (aa,bb) in l:
        #print ((a-aa)*(b-bb)<0)
        if ((a-aa)*(b-bb)<0):
            #print "intersection"
            c+=1
    return c
        

def count_all(arr,N):
    c = 0
    for i in range(N-1):
        (a,b) = arr[i]
        l = arr[i+1:]
        c+= count(a,b,l)
    return c
    

def caseprocess(f,i):
    N = nb_wire(f)
    arr = info(f,N)
    res = count_all(arr,N)
    return "Case #%d: %d\n" % (i+1,res)


# main
if __name__=='__main__':
    input = getfilename()
    name = input[:-3]
    output = name+".out"
    f = open(input,'r')
    t1 = read_line_int(f)
    T = t1[0]
    #print "nb of cases :%d\n" % T
    o = open(output,'w')
    for i in range(T):
        #print "case number %d processed\n" % i
        oline = caseprocess(f,i)
        print oline
        o.write(oline)
    o.close()
    f.close()
