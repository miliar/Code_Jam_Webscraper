# Tidy Numbers

infile = open("B-small-attempt0.in", 'r')
outfile = open("B-small.out", 'w')
numberOfCases = eval(infile.readline())

def isSorted(s):
    if len(s) in [0,1]:
        return True
    if s[0] <= s[1]:
        return isSorted(s[1:])
    return False

for num in range(0,numberOfCases):
    newTest = eval(infile.readline())
    while True:
        newTestStr = str(newTest)
        if isSorted(newTestStr) == True:
            print("Case #", num+1, ": ", newTestStr, sep="", file = outfile)
            break
        else:
            newTest = newTest-1
            continue
outfile.close()