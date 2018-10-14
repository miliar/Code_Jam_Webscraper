import sys
from sys import exit



def main(caseNo,input):
    for l in reversed(xrange(1, int(input)+1)):
      
        l = list(str(l))
        
        if all(l[i] <= l[i+1] for i in xrange(len(l)-1)):
            final = l
            break
        else:
            continue

            

    print "Case #"+str(caseNo)+": "+''.join(final)
    
    
    

numCases = int(sys.stdin.readline())

for i in range(numCases):
    tmp = sys.stdin.readline().strip()
   
    main(i+1, tmp)
    