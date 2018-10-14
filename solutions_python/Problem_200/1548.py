def lastTidy(num):
    num = list(str(num))
    lastDig = 0
    for k, v in enumerate(num):
        if int(v) < lastDig:
            num[k-1] = str(int(num[k-1])-1)
            num = [str(9) if (ind >= k) else val for ind,val in enumerate(num)]
            return lastTidy(int(''.join(num)))
        lastDig = int(v)

    return ''.join(num)

f = open('dataset.txt')
out = open('output.txt', 'w')

cases = int(f.readline())

for i in range(cases):
    case = int(f.readline())
    print('Case #{}: {}'.format(i+1, lastTidy(case)), file=out)

