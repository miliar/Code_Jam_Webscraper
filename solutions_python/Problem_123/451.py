'''
Created on 2013-5-4

@author: t
'''
import math



def solve(mysize,nodes):
    nodes.sort()
    oper = 0
    num = len(nodes)
    i = 0
    b = 10**7
    if mysize == 1:
        return num
    for node in nodes:
        thr = oper + (num-i)
        if thr < b:
            b = thr
        mysize,time = gettime(mysize,node)
        mysize = mysize + node
        oper = oper + time
        i = i+1
    if oper < b:
        return oper
    else:
        return b;

def gettime(a,b):
    
#    print 'hello'
    time = 0
    while a <= b:
        a=a*2-1;
        time = time+1;
#        print str(a)+' '+str(b)
        
    return a,time
    
    

if __name__ == "__main__":
#    inputfile = open("A-small.in",'r')
    inputfile = open("A-large.in",'r')
    outputfile = open('result_big','w')
    num_test = int(inputfile.readline())
    for i in range(num_test):
        
        record = inputfile.readline()
        mysize = int(record.split(' ')[0])
        num = int(record.split(' ')[1])
        record = inputfile.readline()
        nodesstring = record.split(' ')
        nodes = []
        for node in nodesstring:
            nodes.append(int(node))
        nodes.sort()
        outputfile.write('Case #'+str(i+1)+': '+str(solve(mysize,nodes))+'\n')
#    print gettime(3,11)
#        print solve(2,[ 2,1,1,6 ])