import sys
import optparse

debug = False


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


def createMap(N):
    map = []
    maxmin = -1
    maxmin_index = -1
    maxmax = -1
    maxmax_index = -1
    for i in range(N):
        left = i
        right = N - i - 1
        minval = min(left, right)
        maxval = max(left, right)
        if maxmin < minval:
            maxmin = minval
            maxmax = maxval
            maxmin_index = i
        elif maxmin == minval and maxmax < maxval:
            maxmax = maxval
            maxmin_index = i
        map.append([0, left, right, -1, N])

    map.append([1, maxmin_index, -1])
    if debug:
        print(map)

    return map


def setStall(N, map):
    pos = map[-1][1]
    

    map[pos][0] = 1

    for i in range(N):
        if pos - i - 1 < 0 or map[pos - i - 1][0] == 1:
            break
        else:
            map[pos - i - 1][2] -= map[pos-i-1][4] - pos
            map[pos-i-1][4] = pos

    for i in range(N):
        if pos + i + 1 > N or map[pos + i + 1][0] == 1:
            break
        else:
            map[pos + i + 1][1] -= pos - map[pos+i+1][3]
            map[pos+i+1][3] = pos

    maxmin = -1
    maxmin_index = -1
    maxmax = -1
    maxmax_index = -1
    for i in range(N):
        if map[i][0] == 1:
            continue
        minval = min(map[i][1],map[i][2])
        maxval = max(map[i][1],map[i][2])
        if maxmin < minval:
            maxmin = minval
            maxmax = maxval
            maxmin_index = i
        elif maxmin == minval and maxmax < maxval:
            maxmax = maxval
            maxmin_index = i

    map[-1][2] = map[-1][1]
    map[-1][1] = maxmin_index

    if debug:
        print(map)
def solve(data):

    if debug:
        print('[+] input data ', data)

    N = data[0]
    K = data[1]

    map = createMap(N)

    for i in range(K - 1):
        setStall(N, map)

    pos = map[-1][1]
    return str(max(map[pos][1], map[pos][2])) + " " + str(min(map[pos][1], map[pos][2]))


def readData(infile):
    N, K = map(int, infile.readline().strip().split())
    return N, K


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
    infile = "c_input.txt"
    outfile = "c_out.txt"
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
