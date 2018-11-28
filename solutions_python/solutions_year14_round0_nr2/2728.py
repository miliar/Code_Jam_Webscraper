def parseCase(case):
    lst = case.split('\n')[0].split(' ')
    C = float(lst[0])
    F = float(lst[1])
    X = float(lst[2])

    print lst, C, F, X

    turn = 0.0
    currRate = 2
    #decision rule: if the difference between num of turns for X (with curr rate)
    #  and num of turns for X (with another factory) is larger than num of turns
    #  for a new factory, buy a new factory. Otherwise, wait for X.
    while (X/currRate - X/(currRate+F)) > C/currRate:
      #  print turn, '\t', X/currRate, '\t', X/(currRate+F), '\t', C/currRate
        turn += C/currRate
        currRate += F
    turn += X/currRate

    return str(turn)



fname = raw_input('filename: ')
outname = fname.replace('.in','') + '.out'
out = open(outname,'w')

T = -1
f = open(fname, 'r')

linesPerCase = 1
caseNum = 1
with open(fname,'r') as f:
    currCase = ''
    currCount = 0
    for line in f:
        if T == -1:
            T = line
            continue
        if currCount == linesPerCase:
          #  print 'Case ', caseNum, ': ', parseCase(currCase)
            out.write('Case #' + str(caseNum) + ': ' + parseCase(currCase) + '\n')
            currCase = ''
            currCount = 0
            caseNum += 1

        currCase = currCase + line
        currCount += 1

    if currCount == linesPerCase:
        out.write('Case #' + str(caseNum) + ': ' + parseCase(currCase) + '\n')
        currCase = ''
        currCount = 0
        caseNum += 1
            
f.close()
out.close()


print '\t', outname, ':'
g = open(outname,'r')
print g.read()
g.close()
