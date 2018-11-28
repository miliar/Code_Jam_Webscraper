import sys
import math

inFile = open(sys.argv[1], 'r')

outFile = open(sys.argv[1][:-2]+"out", "w")

number_of_input = int(inFile.readline().rstrip("\n"))

count = 0
flag = 1

while(count != number_of_input):
    limits = inFile.readline().rstrip("\n").split()
    count = count + 1
    A = int(limits[0])
    B = int(limits[1])
    
    fairSq = 0

    for num in range(A, B+1):

        pal_num1 = str(num)
        pal_num2 = pal_num1[::-1]
        
        if(pal_num1 == pal_num2):
            x  = math.sqrt(num)
            perfSqr = int(x)
            
            if(perfSqr == x):
                pal_perfSqr1 = str(perfSqr)
                pal_perfSqr2 = pal_perfSqr1[::-1]

                if(pal_perfSqr1 == pal_perfSqr2):
                    fairSq = fairSq + 1
        
    #print "Case #%d: %d" % (count, fairSq)
    outFile.write("Case #%d: %d\n" % (count, fairSq))

inFile.close()
outFile.close()
