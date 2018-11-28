import sys

filename = sys.argv[1]
print "Using file", filename
inputf = open(filename, 'r')
outputname = filename[:-2] + "out"
outputf = open(outputname, 'w')

#def letter_value(l):
#    if ord(l) >= 48 and ord(l) <= 57:
#        return int(l)
#    else:
#        return ord(l) - 87

possible = [ 1, 0 ]
for i in range(2, 100):
    possible.append(i)
print "possible", possible

cases = int(inputf.readline())
print cases, "test cases"
for case in range(1, cases + 1):
    outputf.write("Case #" + str(case) + ": ")
    print "Case", case
    
    symbols = tuple( c for c in inputf.readline()[:-1] )
    print symbols
    #print tuple( letter_value(s) for s in symbols )
    
    #base = letter_value(max(symbols))
    
    currposs = 0
    visited = []
    values = {}
    for s in symbols:
        if s in visited or s in values.keys():
            pass
        else:
            values[s] = possible[currposs]
            currposs += 1
            visited.append(s)
    
    print "values", values
    
    base = possible[currposs]
    if base == 0 or base == 1:
        base = 2
    print "base", base
    
    tot = 0
    symrev = list(symbols)
    symrev.reverse()
    for i in range(len(symrev)):
        tot += values[symrev[i]] * pow(base, i)
    
    print "===", tot
    
    outputf.write(str(tot) + "\n")
    
inputf.close()
outputf.close()
