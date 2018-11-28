def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
    
infile = open("B-small-attempt3.in", "rU")
outfile = open("B-small-attempt3.out", "w")

import math

case = 1
linenum = 0

##triangles = [1]
##i = 1
##
##while (2*i+1)*(i+1) < 1100000:
##    triangles.append((2*i + 1) * (i + 1))
##    i += 1

for line in infile:
    if linenum != 0:
        l = line.strip().split(" ")
        n = int(l[0])
        x = abs(int(l[1]))
        y = int(l[2])
        
        # Find largest triangular number T(2k+1) smaller than n
        k = int(math.floor((-3 + math.sqrt(9 + 8*n - 8))/4.0))
        tn = (2*k + 1) * (k + 1)

        print n, (x, y), k, tn

        if (x+y) <= 2*k:
            outfile.write("Case #%d: 1.0\n" % case)

        elif (x+y) > 2*(k+1):
            outfile.write("Case #%d: 0.0\n" % case)

        else:
            coins = n - tn

            if coins <= 2*(k+1):
                prob = 0
                for j in xrange(y+1, 2*(k+1)+1):
                    prob += choose(coins, j)/float(2**coins)
                    
                outfile.write("Case #%d: %f\n" % (case, prob))
                
            else:
                if x == 0 and y == 2*(k+1):
                    outfile.write("Case #%d: 0.0\n" % case)

                elif coins - 2*(k+1) >= y+1:
                    outfile.write("Case #%d: 1.0\n" % case)

                else:
                    prob = 0
                    for j in xrange(0, 2*(k+1)-y):
                        prob += choose(4*(k+1)-coins, j)/float(2**(4*(k+1)-coins))
                    
                    outfile.write("Case #%d: %f\n" % (case, prob))

        case += 1

    linenum += 1

infile.close()
outfile.close()
