#dijkstra


def file2list(filename):
    f = open(filename, 'r')
    data = f.read()
    f.close()
    l = data.split('\n')
    return l

def convert(a, b):
    if a == b:
        return '-'
    elif a == 'i' and b == 'j':
        return 'k'
    elif a == 'j' and b == 'k':
        return 'i'
    elif a == 'k' and b == 'i':
        return 'j'
    else:
        return '-' + convert(b, a)

def getAllStringsStartsWith(seq, prefix, minus = 0):
    re = []
    while len(seq) > 1:
        if seq[0] == prefix:
            re.append((minus, seq[1:]))
        seq = convert(seq[0],seq[1]) + seq[2:]
        minus = (seq.count('-') + minus) % 2
        seq = seq.replace('-', '')
    if len(seq) > 0 and seq[0] == prefix:
            re.append((minus, seq[1:]))
    return re

def bruteOneSeq(L, X, string):
    seq = string * X

    #get all the strings with 'i':
    start_with_i = getAllStringsStartsWith(seq, 'i')
    #print start_with_i
    for x in start_with_i:
        start_with_j = getAllStringsStartsWith(x[1], 'j', x[0])
        #print start_with_j
        for y in start_with_j:
            start_with_k = getAllStringsStartsWith(y[1], 'k', y[0])
            #print start_with_k
            if (0, '') in start_with_k:
                return True
    return False

def computeOneSeq(L, X, string):
    seq = string * X
    if len(seq) < 3:
        return False
    
    minus = 0
    while len(seq) > 1:
        seq = convert(seq[0],seq[1]) + seq[2:]
        minus = (seq.count('-') + minus) % 2
        seq = seq.replace('-', '')
        #print seq, minus

    #print seq, minus
    
    if len(seq) == 1 or minus == 0:
        return False
    else:
        return bruteOneSeq(L, X, string)

def writeData(data):
    f = open('test.out', 'w')
    s = ''
    for i in range(len(data)):
        s += 'Case #' + str(i + 1) + ': '
        if data[i]:
            s += 'YES'
        else:
            s += 'NO'
        s += '\n'
    f.write(s[:-1])
    f.close()

def main1():
    print bruteOneSeq(2, 6, 'ji')

def main():
    print 'read data...'
    data = file2list('C-small-attempt1.in')
    T = int(data[0])
    data = data[1:]
    print 'iterations: ', T

    result = []
    print 'start computing...'
    for i in range(len(data) / 2):
        l = data[i * 2].split(' ')
        L = int(l[0])
        X = int(l[1])
        string = data[i * 2 + 1]
        result.append(computeOneSeq(L, X, string))
        print i, T

    print result
    writeData(result)
    return result
    
if __name__ == '__main__':
    test = main()
