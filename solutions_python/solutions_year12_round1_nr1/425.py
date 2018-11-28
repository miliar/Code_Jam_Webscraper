#-------------------------------------------------------------------------------
# Problem
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import io,functools;

def parseProb(fd):
    line = fd.readline()
    values=line.split()
    A = int(values[0])
    B = int(values[1])

    line = fd.readline()
    p = [float(s) for s in line.split()]
    return (A,B,p)



def solve(A,B,pr):

    if A==0:
         return float('nan');

    restart = (B+1) + 1
    keepTyping = ((B-A+1) * (pr[A-1])) + ((2*B-A+2)*(1-pr[A-1]))

    return min(restart,
               keepTyping,
               solve(A-1,B,pr) + 1)

def main():
    # prepare whatever
    fd = open( "input.txt" )
    numoftestcases = int(fd.readline())

    for i in range (1,numoftestcases+1):
        (A,B,p) = parseProb(fd)
        pr=[p[0]] ;
        for j in range(1,A):
            pr.append(pr[j-1]*p[j])

        result = solve(A,B,pr);
        print ("Case #%d:"%(i),result)

if __name__ == '__main__':
    main()
