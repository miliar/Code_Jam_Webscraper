
ifile = open("C:\Python25\source\A-large.in")
ofile = open("GCJ2010-q-1-large.txt", 'w')

cases = ifile.readline()
casesN = int(cases)

for l in range(casesN):
    line = ifile.readline()
    snappers = int(line.split()[0])
    snaps = int(line.split()[1])
    
    factS = snaps % (2**snappers)
    
    ofile.write("Case #%d: " % (l+1))
    if factS == 2**snappers - 1:
        ofile.write("ON\n")
    else:
        ofile.write("OFF\n")


        

                 