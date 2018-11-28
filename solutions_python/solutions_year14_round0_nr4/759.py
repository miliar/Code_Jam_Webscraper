#!/usr/bin/env python 
'''
'''
import sys, copy 
debug = 0
def delMinLargerElem(value,l)    :
    for i in range(0, len(l)):
        if l[i] > value:
            del l[i]
            return True;
    return False
def delMaxSmallerElem(value,l)    :
    for i in range( len(l)-1,-1,-1):
        if l[i] < value:
            del l[i]
            return True;
    return False
    
def solve(data):
    N = int(data[0])
    Naomi = sorted([float(x) for x in data[1].split()])
    Ken   = sorted([float(x) for x in data[2].split()])
    if debug :
        print N
        print Naomi
        print Ken
    # compute Naomi's point of deceitful war 
    # loss = 0
    dwpoint = N 
    Ken2 =copy.copy(Ken) 
    for i in range(0, len(Naomi)):
        if Naomi[i] > Ken2[-1]:            
            break; # Naomi will never loss any other points
        if Naomi[i] < Ken2[0]:
            del Ken2 [-1]; 
            dwpoint = dwpoint - 1       
        else:
            code = delMaxSmallerElem( Naomi[i] ,Ken2 )
            if not code : 
                print "Should not happen condition: %d"%(data )
        # if Naomi[i] >= Ken[0]: break
        # loss = loss + 1 
    # pointWd = N-loss
    # compute Naomi's point of war game
    Naomi.reverse() # sort from largest to smallest
    point  = 0
    for i in range(0, len(Naomi)):
        if Naomi[i] < Ken[0]:            
            break; # Naomi will never get any other points
        if Naomi[i] > Ken[-1]: 
            del Ken[0]; 
            point = point + 1 #get one point 
        else :
            code = delMinLargerElem(Naomi[i] ,Ken)
            if not code : 
                print "Should not happen condition: %d"%(data )
    return "%d %d"%(dwpoint , point)
    
def foo(filename):
    f = open(filename,"r")
    output = open("%s.out"%filename, 'w')
    context = f.read().split('\n')    
    C = int(context[0])  # C, the number of test cases
    j = 1
    for i in range(0,C):
        output.write( "Case #%d: %s\n"%(i+1, solve(context[j:j+3])))
        j = j+3
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
