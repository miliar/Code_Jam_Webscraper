def one(shy, num):
    res = 0
    s = 0
    for i in xrange(shy + 1):
        if s < i:
            res += (i - s)
            s += (i - s)
        s += int(num[i])
    return res

f = file('A-large.in', 'r')
count = 0
T = int(f.readline())
while True:
    line = f.readline()
    count += 1
    if len(line) == 0:
        break
    else:
        line = line.split(' ')
        print 'Case #' + str(count) + ':', one(int(line[0]), line[1])
f.close()
