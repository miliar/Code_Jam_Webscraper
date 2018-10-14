fh = open("a.in",'r')
fhw = open("b.txt",'w')
f = fh.readlines()
cases = int(f[0].strip())
Casedir = {}
for i in range(0,cases):
    Casedir[i+1] = (f[i+1].strip()).split(" ")
Keys = list(Casedir.keys())
Keys.sort()
for j in Keys:
    C = float(Casedir[j][0])
    F = float(Casedir[j][1])
    X = float(Casedir[j][2])
    Mintime = X/2
    Rate = 2
    while ((C/Rate) + (X/(Rate + F))) <= (X/Rate):
        Mintime = Mintime + ((C/Rate) + (X/(Rate + F))) - (X/Rate)
        Rate += F
    fhw.write("Case #" + str(j) + ": " + str(Mintime) + "\n")
fh.close()
fhw.close()
