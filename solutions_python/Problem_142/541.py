from string import ascii_lowercase
import math

def solve(strs):
    global case
    case += 1
    # First check if it's impossible
    # Minimally condense each string
    oString = ""
    mString = ""
    numberChars = 0
    sSE = []
    for str in strs:
        localSeriesEncoded = []
        for ch in str:
            if mString[-1:] == ch:
                numberChars += 1
            elif mString == "":
                mString += ch
                numberChars += 1
            else:
                mString += ch
                localSeriesEncoded.append(numberChars)
                numberChars = 1
        if oString == "":
            oString = mString
            mString = ""
        elif oString == mString:
            mString = ""
        else:
            wfile.write("Case #{0}: Fegla Won\n".format(case))
            return
        localSeriesEncoded.append(numberChars)
        numberChars = 0
        sSE.append(localSeriesEncoded)
    
    averageEncoding = []
    l = 0
    for x in range(len(sSE[0])):
        total = 0
        n = 0
        for strE in sSE:
            total += strE[x]
            n += 1
        averageEncoding.append(math.floor(total / n))
    
    for strSummary in sSE:
        for x in range(len(strSummary)):
            l += math.floor(abs(averageEncoding[x] - strSummary[x]))
    wfile.write("Case #{0}: {1}\n".format(case, l))
    print("Case #{0}: {1}".format(case, l))
   
f = open("input.in")
f.readline()

wfile = open("output.out", "w")

case = 0

line = f.readline()
while line != "":
    strings = []
    stringcount = int(line)
    for x in range(stringcount):
        strings.append(f.readline().rstrip('\n'))
    
    solve(strings)
    line = f.readline()
