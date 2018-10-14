from fractions import gcd

with open('A.in', 'r') as fin:
    lines = fin.readlines()

T = int(lines[0])

for i in range(1, T + 1):
    line = lines[i]
    bits = line.split()
    N = int(bits[0])
    PD = int(bits[1])
    PG = int(bits[2])
    Dgcd = gcd(PD, 100)
    Ddenom = 100 / Dgcd
    if Ddenom > N:
        #print "Ddenom > N"
        print "Case #{0}: Broken".format(i)
        continue
    Ggcd = gcd(PG, 100)
    WD = PD / Dgcd
    D = 100 / Dgcd
    WG = PG / Ggcd
    G = 100 / Ggcd
    #print "D:", D, "WD:", WD, "G:", G, "WG:", WG
    if PD == 100 and PG == 100:
        print "Case #{0}: Possible".format(i)
    elif PD == 0 and PG == 0:
        print "Case #{0}: Possible".format(i)
    elif PG == 100 or PG == 0:
        print "Case #{0}: Broken".format(i)
    else:
        print "Case #{0}: Possible".format(i)
