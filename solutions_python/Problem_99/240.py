#!/usr/bin/python
# Filename:Problem A. Password Problem.py
import sys,time

#file = "Problem A. Password Problem"
#file = "Problem A. Password Problem small"
file = "Problem A. Password Problem large"

#debug = True
debug = False

def solve(A,B,P):
  
    PBNoError = []
    
    pPreError = 0.0
    for i  in range(A):
        PBNoError.append(1-pPreError)
        pNowError = (1-pPreError)*P[i]
        pPreError += pNowError
        
    if debug:
        print(A)
        print(B)
        print(P)
        print(pPreError)
        print(PBNoError)
        print("\n\n")
        
    ret = 0
    enterRightAway = 2+B
    keepTyping = (1- pPreError)*(B-A+1) + pPreError*(B-A+1 + B+1)
    
    print(enterRightAway)
    print(keepTyping)
    if (enterRightAway>keepTyping):
        ret = keepTyping
    else:
        ret = enterRightAway

    
    for i in range(1,A+1):
        typeNow = (PBNoError[A-i]*(B-A+1 + 2*i) + (1-PBNoError[A-i])*(B-A+1 + 2*i + B+1))
        if(debug):
            print("%d,%d"%(i,typeNow))
        if(typeNow < ret):
            ret = typeNow
    
    return ret

def main():
    inFile = open(file+".in")
    assert inFile
    outFile = open(file+".out",'w')
    assert outFile
    
    T = int(inFile.readline())
    for n in range(T):
        ab = inFile.readline().split()
        A = int(ab[0])
        B = int(ab[1])
        P = []
        pstr = inFile.readline().split()
        for i in range(len(pstr)):
            P.append(1-float(pstr[i]))
     
            
        soln = solve(A,B,P)
        print ("Case #%d: %s" % (n+1, soln))
        total_time = time.time() - start_time
        print("Case #%d Completed in %.1f seconds" % (n+1, total_time))
        outFile.write("Case #{0}: {1}\n".format(n+1, soln));
        
    inFile.close()
    outFile.close()

start_time = time.time()

main()

total_time = time.time() - start_time
print("All Completed in %.1f seconds" % total_time)
