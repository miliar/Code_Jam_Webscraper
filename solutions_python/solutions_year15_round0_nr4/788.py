#-------------------------------------------------------------------------------
# Name:        Problem D. Ominous Omino
# Purpose:     Code Jam Qualification Round 2015
#
# Author:      Vihanga Liyanage
#
# Created:     11/04/2015
# Copyright:   (c) Vihanga Liyanage 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#can - GABRIEL
#else - RICHARD

def main():
    infile = open("input.txt", "r")
    outfile = open("output.txt", "w")
    T = int(infile.readline()) #test cases
    for i in range(T):
        (x, r, c) = (int(y) for y in infile.readline().split())
        result = ""
        if x > r and x > c:
            result = "RICHARD"
        elif x > 6:
            result = "RICHARD"
        elif x == 1:
            result = "GABRIEL"

        elif x == 2:
            one = r%2==0
            two = c%2==0
            if one==False and two==False:
                result = "RICHARD"
            else:
                result = "GABRIEL"
            print(i+2,"\t",x,r,c,result)
        elif x==3:
            one = r%3==0
            two = c%3==0
            if (one==False and two==False) or (one and c<2) or (two and r<2):
                result = "RICHARD"
            else:
                result = "GABRIEL"

        elif x==4:
            one = r%4==0
            two = c%4==0
            if (one==False and two==False) or (one and c<3) or (c==4 and r<3) :
                result = "RICHARD"
            else:
                result = "GABRIEL"


        outfile.write("Case #" + str(i+1) + ": " + result +"\n")

if __name__ == '__main__':
    main()
