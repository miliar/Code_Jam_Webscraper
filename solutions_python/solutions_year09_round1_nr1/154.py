####################################################
#   Tested on python 2.6
####################################################
       
fin = open("A-small-attempt0.in", "r")

#fin = open("A-large-practice.in", "r")

#fin = open("input.txt", "r")
fout = open("output.txt", "w")

import math

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    if (b==1):
        return num*"1"
    return ((num == 0) and  "0" ) or ( baseN(num // b, b).lstrip("0") + numerals[num % b])


def isHappy(num1,b1,copypasssums):

    passsums = list(copypasssums)
    
    s = str(baseN(num1,b1))
    sumsqr = 0

    #print num1,b1,s    
    for snum in s:
        inum = int(snum)
        sumsqr += pow(inum,2)

    suminbase = baseN(sumsqr,b1)

    sumdigits = 0
    for s1 in suminbase:
        sumdigits += int(s1)
        
    #print "sumsqr, sumdigits", sumsqr, sumdigits

    if sumsqr==num1:
        return False
    elif sumsqr in passsums:
        return False
    elif sumdigits==1:
        return True
   # elif sumsqr < b1:
   #    return False
    
    else:
        passsums.append(sumsqr)
        return isHappy(sumsqr,b1,passsums)



icount = int(fin.readline())

for i in range(0,icount):

    bases = fin.readline().strip().split()
    intbases = map(int, bases)
    #print bases
    #print intbases

    answer = 0
    t = 2
    while(True):
        allhappy = True
        for b in intbases:
            #print
            
            if not isHappy(t,b,[]):
                #print "Not happy t, b",t,b
                allhappy = False
                break
                
        if allhappy:
            #print "Happy",t
            answer = t    
            break

        t += 1

    
#    print "Case #"+str(i+1)+": " + str(answer)
    
    
    printline = "Case #"+str(i+1)+": " + str(answer) + "\n"
    print printline,
    fout.write(printline)

fin.close()
fout.close() 



   



    
        
