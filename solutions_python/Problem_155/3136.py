"""
Shyness
"""
    
def calFriend(case):
    """
    input: [Smax, Si]
    output: minimum number of friends
    """
    sMax = int(case[0])
    ss = case[1]
    
    if sMax == 0:
        return 0
    else:
        cum = 0
        toAdd = 0
        for shy in range(sMax):
            cum += int(ss[shy])
            if cum < (shy+1):
                add = (shy + 1 - cum)
                toAdd += add
                cum += add
        return toAdd


if __name__ == '__main__':
    nAtt = 2
    # inputFileName = 'A-small-attempt' + str(nAtt) + '.in'
    # outputFileName = 'sub-' + str(nAtt) + '.out'
    inputFileName = 'A-large.in'
    outputFileName = 'sub-large.out'
    
    
    ## read input
    file = open(inputFileName)
    nCase = int(file.readline())

    cases = []
    for line in file:
        cases.append(line.split())
    
    ## Output file
    outfile = open(outputFileName, 'w')
    count = 1
    for case in cases:
        res = "Case #" + str(count) + ': ' + str(calFriend(case)) + '\n'
        outfile.write(res)
        count += 1
    