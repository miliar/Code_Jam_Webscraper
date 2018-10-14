fhr = open("input.txt",'r')
fhw = open("output.txt",'w')

f = fhr.readlines()
fhr.close()
Cases = int(f[0].strip())

for i in range(0,Cases):
    raw = (f[i+1].strip()).split()
    X = int(raw[0])
    R = int(raw[1])
    C = int(raw[2])
    winner = "RICHARD"
    if X == 1:
        winner = "GABRIEL"
    elif X == 2:
        r = R%2
        c = C%2
        if (r,c) != (1,1):
            winner = "GABRIEL"
    elif X == 3:
        if R*C in [6,9,12]:
            winner = "GABRIEL"
    else:
        if R*C in [12,16]:
            winner = "GABRIEL"
    fhw.write("Case #" + str(i+1) + ": " + winner + "\n")
fhw.close()
