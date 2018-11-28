from sys import stdin, stdout
n = int(stdin.readline().strip())
case = 1
for i in xrange(n):
    count = 0
    a, b = stdin.readline().strip().split()
    if len(a) == 1 and len(b) == 1:
        print 'Case #%d: 0' %case
        case += 1
    else:
        numbers = map(str, range(int(a), int(b)+1))
        
        for i in xrange(len(numbers)):
            n = numbers[i]
            m = numbers[i]
            length = len(numbers[i])
            for j in xrange(length):
                m = m[-1] + m[:len(m)-1]

                if int(m) <= int(b) and int(m) > int(n) and int(m) >= int(a):
                    count += 1
        print 'Case #%d: %d' %(case, count)
        case += 1





