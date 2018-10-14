#q1
#dynamic programing

def file2list(filename):
    l = []
    with open(filename) as fp:
        for line in fp:
            l.append(line)
    return l

from operator import mul

def writeData(data):
    f = open('test.out', 'w')
    s = ''
    for i in range(len(data)):
        s += 'Case #' + str(i + 1) + ': '
        s += str(data[i])
        s += '\n'
    f.write(s[:-1])
    f.close()

def reverse(x):
    return int(str(x)[::-1])

l = [[0,0]]

def getAns(N):
    #dynamic programing:    
    if (N < len(l)):
        return l[N][0]
    for x in range(len(l),N + 1):
        tmp = reverse(x)
        if (len(l) > reverse(x) and l[tmp][0] < l[x - 1][0] and x % 10 != 0):
            l.append([l[tmp][0] + 1, tmp])
        else:
            l.append([l[x - 1][0] + 1, x - 1])            
    return l[N][0]

def main():
    print 'read data...'
    data = file2list('A-small-attempt2.in')
    T = int(data[0])
    data = data[1:]
    print 'iterations: ', T

    result = []
    print 'start computing...'
    
    for i in range(len(data)):
        result.append(getAns(int(data[i])))
        print i, T

    print result
    writeData(result)
    return result
    
if __name__ == '__main__':
    test = main()
