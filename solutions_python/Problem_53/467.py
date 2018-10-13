HexBin ={"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

def main():
    f = open('A-large.in', 'r')
    fOut = open('A-large.out', 'w')
    inp = f.readlines()
    cases = inp[0]
    del inp[0]
    for i in range(len(inp)):
        line = inp[i].replace('\n', '').split(' ')
        n = int(line[0])
        k = int(line[1])
        val = ''.join([HexBin[j] for j in '%X' % k]).lstrip('0')
        result = ''
        if len(val) > 0 and val[-n:] == ('1'*n):
            result = 'Case #' + str(i+1) + ': ON'
        else:
            result = 'Case #' + str(i+1) + ': OFF'
        print result
        fOut.write(result + '\n')
    f.close()
    fOut.close()


if __name__ == '__main__':
    main()
