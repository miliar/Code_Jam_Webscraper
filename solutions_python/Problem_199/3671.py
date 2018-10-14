def flip(x):
    return '+' if x == '-' else '-'

inputfile = open('A-large.in','r')
outputfile = open('large.out','w')
numcases = inputfile.readline()
case = 0
res = ''

for l in inputfile:
    case += 1
    l = l.split()
    s = list(l[0])
    k = int(l[1])
    i = 0
    numflips = 0
    while i <= (len(s)-k):
        if s[i] == '-':
            s[i:i+k] = map(flip, s[i:i+k])
            numflips += 1
        i += 1
    res = 'IMPOSSIBLE' if '-' in s else str(numflips)
    outputfile.write('Case #'+str(case)+": "+str(res)+"\n")