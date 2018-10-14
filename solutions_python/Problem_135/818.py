#!/usr/bin/env python 
import copy
import sys
import os 
debug = 0
def withSameCard(cr1, cr2):
    return set(cr1) & set(cr2)
    
def solve(R1,ca1, R2, ca2):
    ca1 = [[int(a) for a in e.split()] for e in ca1]
    ca2 = [[int(a) for a in e.split()] for e in ca2]
    setSameCards = withSameCard(ca1[R1-1], ca2[R2-1])
    nsc = len(setSameCards  ) 
    rBad = "Bad magician!"
    bCheat = "Volunteer cheated!"
    if nsc == 1:
        return list(setSameCards )[0]
    elif nsc > 1: 
        return "Bad magician!"
    else:#elif nsc ==0:
        return "Volunteer cheated!"
    print "should not happen!"
    print R1, ca1
    print R2, ca2
    return None

def foo(filename):
    f = open(filename,"r")
    output = open("%s.out"%filename, 'w')
    context = f.read().split('\n')    
    C = int(context[0])  # C, the number of test cases
    k = 1
    for i in range(0,C):
        k = 10*i+1
        R1 = int(context[k])  # the number of row which seleted card in at 1st card arrangement 
        begin = k+1
        ca1 = context[begin :begin +4]
        R2 = int(context[k+5])  # the number of row which seleted card in at 2nd card arrangement 
        begin = k+6
        ca2 =  context[begin :begin +4]
        output.write( "Case #%d: %s\n"%(i+1, solve(R1,ca1, R2, ca2)))
    f.close()
    output.close()
  
def main():
    if len(sys.argv) > 1:
        inputfile = sys.argv[1] 
    else:
        inputfile = "input"
    foo(inputfile)
            
if __name__ == "__main__":
    main()
    # # 1. make all milkshake unmalted 
    # milkshakes = N*[0]

    # # # remove duplicate
    # a = list(set( customers))
    # customers = a
    # M = len(customers)

    # b = [[int(a) for a in e.split()] for e in customers]
    # # b = [[int(a) for a in e.split()[1:]] for e in customers]        
    # # satisfy each customers 
    # i = 0 
    # while( i < M):
        # customer = b[i]
        # if not  satisfy(customer  , milkshakes):
            # # 2. If there is an unsatisfied customer who only likes unmalted flavors, and all those flavors have been made malted, then no solution is possible.
            # if impossible(customer, milkshakes ) :
               # return "IMPOSSIBLE";
            # # 3. If there is an unsatisfied customer who has one favorite malted flavor, then we must make that flavor malted. We do this, then go back to step 2.
            # # find the malted malted flavor
            # likeFlavor = findLikeMaltedFlavor(customer)
            # if likeFlavor :
                # milkshakes[likeFlavor  - 1 ] = 1
                # customer[0] = 0
                # i = 0 # goto step 2
                # continue
            # else:
                # print "Not found favorite malted flavor for customer %s, where shakemilks = %s" % (customer, milkshakes)
        # i = i + 1
    # result = str(milkshakes[0])
    # for i in range(1,N):        result = "%s %s"%(result,milkshakes[i])

    # def satisfy(customer, milkshakes):
    # if  customer[0] == 0 : return True;
    # likeflavors = customer[1:]
    # for i in  range(0, len(likeflavors) , 2):
        # idx = likeflavors[i] - 1
        # if milkshakes[idx] == likeflavors[i+1] :
            # return True
    # return False
    
# def findLikeMaltedFlavor(customer):
    # likeflavors = customer[1:]
    # for i in  range(0, len(likeflavors) , 2):
        # if likeflavors[i+1]  == 1: return likeflavors[i]
    # return None
    
# def impossible(customer, milkshakes):
    # # 2. If there is an unsatisfied customer who only likes unmalted flavors, and all those flavors have been made malted, then no solution is possible.
    # likeflavors = customer[1:]
    # for i in  range(0, len(likeflavors) , 2):
        # if likeflavors[i+1]: return False
        # if not milkshakes[likeflavors[i]-1]: return False
    # return True
    

