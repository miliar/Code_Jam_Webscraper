from fractions import Fraction, gcd

fin = file("A-large.in", "rU")
fout = file("A-large.out", "w")

nruns = int(fin.readline().strip())
for i in xrange(nruns):
    line = fin.readline().strip().split()
    n = int(line[0])
    pd = int(line[1])
    pg = int(line[2])

    fraca = Fraction(pd, 100)
    fracb = Fraction(pg, 100)

    nwon = fraca.numerator
    nlost = fraca.denominator - fraca.numerator
    #print nlost

    #Find LCM of fraca.denominator and fracb.denominator
    #gcdval = gcd(x.denominator, y.denominator)
    #lcm = x.denominator * y.denonminator / gcdval

    if n < fraca.denominator or (nlost > 0 and pg == 100) or (nwon > 0 and pg == 0): 
        result = "Broken"
    else:
        result = "Possible"

    strout = "Case #" + str(i+1) + ": " + str(result) + "\n"
    #print strout
    fout.write(strout)
fin.close()
fout.close()
