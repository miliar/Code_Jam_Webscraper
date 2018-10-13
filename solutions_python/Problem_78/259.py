import sys
import math

def main(args):
    input = open(args[0])
    cases = int(input.readline())
    for i in range(cases):
        casenum = i + 1
        casein = input.readline().split(" ")
        n = int(casein[0])
        pd = int(casein[1])
        pg = int(casein[2])
        result = "Possible"
        if((pg == 100) and (pd < 100)):
            result = "Broken"
        elif((pg == 0) and (pd > 0)):
            result = "Broken"
        elif((pd > 0) and (n <= 100)):
            #ensure that n is divisible into pd
            valid = False
            for x in range(n):
                y = (x+1) * (pd/100.0)
                if(math.trunc(y) == y):
                    valid = True
                    break
            if(not valid):
                result = "Broken"
        
        print "Case #{0}: {1}".format(casenum, result)
        #print combinations
        #print oppositions
        

if __name__ == '__main__':
    main(sys.argv[1:])