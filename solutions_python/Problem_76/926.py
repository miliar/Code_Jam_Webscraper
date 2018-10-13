def getsolution(line):
    vals = line.split(' ')
    values = []
    for x in vals:
        values.append(int(x))
    temp = 0
    low = 9999999999
    for x in values:
        temp ^= x
        if x < low:
            low = x
    if temp:
        return -1
    else:
        return (sum(values) - low)

def main():
    infile = open('input.in','r')
    outfile = open('output.out','w')
    testCases = int(infile.readline())
    counter = 1
    while testCases > 0:
        testCases -= 1
        N = int(infile.readline())
        values = infile.readline()
        answer = getsolution(values)
        
        if answer == -1:
            outfile.write('Case #' + str(counter) + ': NO'+'\n')
        else:
            outfile.write('Case #' + str(counter) + ': ' + str(answer)+'\n')
        counter += 1
    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
