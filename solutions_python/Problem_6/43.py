from decimal import Decimal
inf = open("c.in", "r")
outf = open("c.out", "w")
r = Decimal("5.2360679774997896964091736687313")
t = int(inf.readline())
for i in range(1, t + 1):
    n = int(inf.readline())
    outf.write(str(r ** n).split('.')[0][-3:] + "\n")
inf.close()
outf.close()
