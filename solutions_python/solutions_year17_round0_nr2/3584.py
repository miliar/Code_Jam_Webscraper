import sys
import optparse

debug = True


def setData(data, numList):
    ret = ''
    strData = str(data)

    for i in range(len(strData)):
        if debug:
            print('[+] numList ' + str(numList))
        cmp = strData[i]
        if cmp in numList:
            ret = cmp
            numList.remove(cmp)
    return ret


def solve(data):
    N = []
    for i in range(len(data)):
        N.append(int(data[i]))

    if debug:
        print('[+] input data ', N)

    for i in range(len(N) - 1):
        if N[len(N)-i-1] >= N[len(N)-i-2]:
            continue
        else:
            N[len(N)-i-2] -= 1
            for j in range(i+1):
                N[len(N)-i-1+j] = 9


    result = ""
    for i in N:
        result += str(i)
    return int(result)


def readData(infile):
    N = str(infile.readline().strip())
    return N


def howto():
    usage = ' -i <input file> [-o <output file>]'
    parser = optparse.OptionParser(sys.argv[0] + usage)
    parser.add_option(
        '-i', dest='infile', type='string', help='specify infile name')
    parser.add_option(
        '-o', dest='outfile', type='string', help='specify outfile name')
    (options, args) = parser.parse_args()
    if options.infile is None:
        print(parser.usage)
    return options.infile, options.outfile

if __name__ == '__main__':
    #infile, outfile = howto()
    infile = "b_input.txt"
    outfile = "b_out.txt"
    if infile is None:
        exit()

    infile = open(infile, 'r')
    if outfile is not None:
        outfile = open(outfile, 'w')

    T = int(infile.readline().strip())
    for caseN in range(1, T + 1):
        data = readData(infile)
        result = solve(data)
        resultForm = 'Case #%i: %s\n' % (caseN, result)

        if outfile:
            outfile.write(resultForm)
        else:
            print(resultForm)

    infile.close()
    if outfile is not None:
        outfile.close()
