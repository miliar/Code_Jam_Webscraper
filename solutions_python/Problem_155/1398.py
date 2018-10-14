__author__ = 'zfeng'

def solver(line):
    num, input = line.split()
    vals = []

    for i in xrange(len(input)):
        vals.append(int(input[i]))

    req = 0
    total = 0

    for i in xrange(len(vals)):
        if total >= i:
            total += vals[i]
        else:
            req += i - total
            total = i + vals[i]

    return req

if __name__ == '__main__':
    f = open('/Users/zfeng/Downloads/A-large.in')
    lines = f.readlines()
    f.close()

    for i in xrange(int(lines[0])):
        print str.format('Case #{0}: {1}', i + 1, solver(lines[i + 1]))

