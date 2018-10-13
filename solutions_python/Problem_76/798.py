f = open('c-large.in', 'r')
f2 = open('c-large.out', 'w')

cases = int(f.readline().strip('\n'))
for x in xrange(1, cases+1):
    f2.write('Case #' + str(x) + ': ')
    num = int(f.readline().strip('\n'))
    inputs = f.readline().strip('\n').split()
    minval = 999999999999
    ans = 0
    total = 0
    for y in inputs:
        z = int(y)
        if minval > z:
            minval = z
        ans = ans ^ z
        total = total + z
    if ans:
        f2.write('NO\n')
    else:
        f2.write(str(total - minval) + '\n')

f.close()
f2.close()
