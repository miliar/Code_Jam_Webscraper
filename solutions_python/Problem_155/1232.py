#q1

def file2list(filename):
    l = []
    with open(filename) as fp:
        for line in fp:
            l.append(line)
    return l


def writeData(data):
    f = open('test.out', 'w')
    s = ''
    for i in range(len(data)):
        s += 'Case #' + str(i + 1) + ': ' + str(data[i]) + '\n'
    f.write(s[:-1])
    f.close()

def test1(max_shy, aud):
    re = 0
    total_aud = 0
    for i in range(max_shy + 1):
        if total_aud < i:
            re += i - total_aud
            total_aud = i
        total_aud += aud[i]
    return re

def main():
    print 'read data...'
    data = file2list('A-large.in')
    T = int(data[0])
    data = data[1:]
    print 'iterations: ', T

    result = []
    print 'start computing...'
    
    for i in range(len(data)):
        tmp = data[i].split(' ')
        max_shy = int(tmp[0])
        aud = []
        for i in range(max_shy + 1):
            aud.append(int(tmp[1][i]))
            
        result.append(test1(max_shy, aud))
        print i, T

    print result
    writeData(result)
    return result
    
if __name__ == '__main__':
    test = main()
