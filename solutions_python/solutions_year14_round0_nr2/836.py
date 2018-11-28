#from Sets import set

ifile = open("B-large.in","r")
T = ifile.next().rstrip("\n")

for i in range (int(T)):
    nextRow = ifile.next().rstrip("\n").split(" ")
    C, F, X = float(nextRow[0]), float(nextRow[1]), float(nextRow[2])
    n = int( (X*F - 2*C)/(C*F) )
    time=0.0
    for j in range(n):
        time += C/float(2+j*F)
    time += (X/float(2+n*F))
    print "Case #" + str(i+1) +": "+ str(round(time,7))
