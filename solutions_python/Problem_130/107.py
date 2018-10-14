infile = open("B-small-attempt1.in", "rU")
outfile = open("B-small-attempt1.out", "w")

import math

case = 1
linenum = 0
for line in infile:
    if linenum != 0:
        line = line.strip().split(" ")
        n = int(line[0])
        p = int(line[1])

        if n == 1:
            if p == 1:
                outfile.write("Case #%d: 0 0\n" % case)
                case += 1
            elif p == 2:
                outfile.write("Case #%d: 1 1\n" % case)
                case += 1

        else:
            x = 0
            y = 0
            
            if p == 2**n:
                x = 2**n - 1
                y = 2**n - 1

            else:
                power = n-1
                xp = p

                while xp > 2**power:
                    xp -= 2**power
                    x += 2**(n - power)
                    power -= 1

                # x is guaranteed to win

                yp = int(math.floor(math.log(p, 2)))

                for i in xrange(1, yp+1):
                    y += 2**(n-i)

            outfile.write("Case #%d: %d %d\n" % (case, x, y))
            case += 1
        
    linenum += 1

outfile.close()
