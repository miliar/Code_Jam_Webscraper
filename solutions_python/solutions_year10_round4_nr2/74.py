run = 'small-attempt1'

inName = 'B-' + run + '.in'
outName = 'B-' + run + '.out'

infile = open(inName,'r')
outfile = open(outName,'w')

cases = int(infile.readline().strip('\n'))

for case in range(1,cases+1):
    print case
    P = int(infile.readline().strip('\n'))
    tix = 2**P - 1
    
    M = []
    line = infile.readline().strip('\n')
    tokens = line.split()
    for m in tokens:
        M.append(int(m))
    
    for round in range(0, P):
        line = infile.readline().strip('\n')
        
    for round in range(1, P+1):
        for game in range(0, 2**(P-round)):
            canSkip = True
            for team in range(0, 2**(round)):
                if M[game*(2**round)+team] <= 0:
                    canSkip = False
            if canSkip == True:
                tix -= 1
                for team in range(0, 2**round):
                    M[game*(2**round)+team] -= 1
    
    outfile.write("Case #" + str(case) + ": " + str(tix) + "\n")

infile.close()
outfile.close()
