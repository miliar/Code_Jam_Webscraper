from math import *


def isP(s):
    l = len(s)/2
    for x in range(l):
        if s[x] != s[-1-x]:
            return False
    return True

def isSqrt(n):
    a = sqrt(n)
    return a == floor(a)
        

def main():
    inpfile = open("C-small-attempt0.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        S = 0
        line = inpfile.readline().strip()
        linelst = line.split()
        a = int(linelst[0])
        b = int(linelst[1])
        print a,b
        
        for x in range(a, b+1):
            if isSqrt(x):
                s = str(x)
                s2 = str(int(floor(sqrt(x))))
                #print s, s2
                if isP(s) and isP(s2):
                    S += 1
        
        result = "Case #" + str(case) + ": " + str(S)+"\n"
        print result
        
        outfile.write(result)
    inpfile.close()
    outfile.close()




if __name__ == "__main__":


    main()
    

    
    