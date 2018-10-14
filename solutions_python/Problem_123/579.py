import time
import sys
import pdb
import numpy

infile = open("input.txt")
outfile = open("output.txt", 'w')

timeit = 1
debugv = 1

def main():
        T = int(infile.readline())
        for case in range(1,T+1):
            doCase(case)
            
def numoperations(i,j):
        temp = i
        t = 0
        while(temp <= j ):
             temp = temp + (temp - 1)
             t +=1
        return t,temp  
             

def solve(m,otherms,nm):
        otherms.sort()
        if( m == 1 ):
                return nm
        k = 0
        for i,item in enumerate(otherms):
                tt = 0
                if( m <= otherms[i]):    
                                t,tt = numoperations(m,otherms[i])
                                if (t >= (nm - i)):
                                        return k + (nm - i)
                                else:
                                        m = tt
                                        k = k + t
                m = m + otherms[i]                                       
        return k       
def doCase(case):
    l = map(int, infile.readline().strip().split())
    m = l[0]
    nm = l[1]
    otherms = map(int, infile.readline().strip().split())
    assert(m!=0)
    result = solve(m,otherms,nm)
    debug("{}\n".format(result))
    outfile.write("Case #{}: {}\n".format(case, result))
    

def debug(m):
    if debugv:
        sys.stdout.write(m)

		
if __name__ == '__main__':  
    startTime = time.clock()
    main()
    if timeit:
        sys.stdout.write("Completed in {} seconds.\n".format(time.clock() - startTime))
    outfile.close()
