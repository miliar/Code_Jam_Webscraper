def diva(inFile, outFile):
    for case, line in enumerate(inFile):
        smax, audience = line.split()
        count = 0
        output = 0
        for level, nb in enumerate(audience):
            if count < level:
                output += level - count
                count = level + int(nb)
            else:
                count += int(nb)
        outFile.write('Case #{0}: {1}\n'.format(case+1, output))


if __name__ == '__main__':
    inFile = open('/home/raphael/Downloads/A-large.in', 'r')
    outFile = open('/home/raphael/output.txt', 'w')
    inFile.readline()
    diva(inFile, outFile)



