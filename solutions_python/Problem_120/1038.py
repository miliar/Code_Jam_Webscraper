import sys
import math as m

###

f = open("A-small-attempt0.in", "r")
out = open("paint_out.txt", "w")
numInputs = long(f.readline())

for input in xrange (0, numInputs):
    nums = f.readline().split()
    r = long(nums[0])
    t = long(nums[1])
    
    x = (-(2*r+3) + m.sqrt(4*r*r - 4*r + 8*t + 1))/4
    n = m.ceil(x)
    if (n+1)*(2*n+2*r+1) > t:
        n -= 1
    numRings = int(m.floor(n+1))
    line_out = "Case #" + str(input + 1) + ": " + str(numRings) + "\r\n"
    out.write(line_out)
    print line_out
    
f.close()
out.close()