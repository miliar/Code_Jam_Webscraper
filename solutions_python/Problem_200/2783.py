n = int(raw_input())
for k in xrange(1, n + 1):
    num = list('0' + raw_input())
    for i in range(1,len(num)):
        if num[i - 1] > num[i]:
            j = i - 1
            while j > 0:
                if num[j] > num[j - 1]:
                    break
                j -= 1
            num[j] = str(int(num[j]) - 1)
            j += 1
            while j < len(num):
                num[j] = '9'
                j += 1
            break
    for i in range(1,len(num)):
        if num[i] != '0':
            print 'Case #' + str(k) +': ' + ''.join(num[i:])
            break
            