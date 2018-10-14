from fractions import Fraction
import math
t = int (raw_input())
n = []
for i in range(0,t):
    n.append ( Fraction (raw_input()))

i = 1
for item in n:
    a = math.log(item.denominator,2)
    number_dec = (a-int(a))
    if number_dec > 0:
        print "Case #" + str(i) + ": " + "impossible"
    else:
        if int(item.numerator) == 1:
            print "Case #" + str(i) + ": " + str(int(a))
        else:
            while int(item.numerator) != 1:
                x = int(item.numerator) - 1 
                y = int(item.denominator)
                z = Fraction(x,y)
                a = math.log(z.denominator,2)
                item = z
            
            print "Case #" + str(i) + ": " + str(int(a))
    i = i+1

    
