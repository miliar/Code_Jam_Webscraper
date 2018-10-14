import sys
import os.path
import fractions
import math

def main(argv):
    if (len(argv)==1):
        print("No argument!\n")
        return
    
    if(not os.path.isfile(argv[1])):
        print("input file does not exist!\n")
        return

    inname=argv[1]
    outname=argv[1][:-2]+'out'

    with open(inname,"r") as inputFile:
        num=int(inputFile.readline())
        for i in range(num):
            res=""
            p_q=inputFile.readline().rstrip('\n').split('/')
            p=int(p_q[0])
            q=int(p_q[1])
            pq=fractions.Fraction(p,q)
            power=math.log(pq.denominator,2)
            if(abs(power-int(power))>(10**-6)):
                res="impossible"
            else:
                j=1
                while(True):
                    if(1/2**(j-1)>pq>=1/2**j):
                        res=str(j)
                        break
                    else:
                        j+=1

            with open(outname,"a") as out:
                out.write("Case #"+str(i+1)+": "+res+"\n")
        

if __name__=="__main__":
    main(sys.argv)
