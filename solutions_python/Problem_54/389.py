import math

def gcd(a,b):
    if a > b:return gcd(b,a)
    if 0 == a:return b
    if 1 == a:return 1
    return gcd(b%a,a)

infile = open("C:\\B-large.in")
outfile = open("C:\\B-large.out","w")
nCases = int(infile.readline())
iCases = 1
while iCases <= nCases:
    line = infile.readline()
    lineL = line.split(' ')
    n = int(lineL[0])
    lineL = lineL[1:]
    intsL = []
    i = 0
    while i < n:
        intsL.append(int(lineL[i]))
        i = i + 1

    intsL.sort()
    
    disL = []
    i = 1
    while i < n:
        disL.append(intsL[i]-intsL[i-1])
        i = i + 1

    gc = disL[0]
    i = 1
    while i < n-1:
        gc = gcd(gc,disL[i])
        i = i + 1

    r = intsL[0]%gc
    outfile.write("Case #")
    outfile.write(str(iCases))
    outfile.write(": ")
    if 0 == r:outfile.write("0")
    else: outfile.write(str(gc-r))
    outfile.write("\n")
    iCases = iCases + 1

infile.close()
outfile.close()
