
def f1(n):
    n = str(n)
    while (True):
        #print ''.join(n), '->',
        n = list(str(int(''.join(n))))
        l = len(n)
        flag = False
        for i in range(l-1):
            if (n[i] > n[i+1]):
                flag = True
                if (n[i] == '1'):
                    n[i], n[i+1] = '0', '9'
                if (n[i] == '2'):
                    n[i], n[i+1] = '1', '9'
                if (n[i] == '3'):
                    n[i], n[i+1] = '2', '9'
                if (n[i] == '4'):
                    n[i], n[i+1] = '3', '9'
                if (n[i] == '5'):
                    n[i], n[i+1] = '4', '9'
                if (n[i] == '6'):
                    n[i], n[i+1] = '5', '9'
                if (n[i] == '7'):
                    n[i], n[i+1] = '6', '9'
                if (n[i] == '8'):
                    n[i], n[i+1] = '7', '9'
                if (n[i] == '9'):
                    n[i], n[i+1] = '8', '9'
                for i in range(i+1, l):
                    n[i] = '9'
        #print ''.join(n)
        if (not flag):
            break
    return ''.join(n)


f = open('ip.txt', 'r')
g = open('op.txt', 'w')
for line in f:
    t = int(line)
    break

c = 0
for line in f:
    n = int(line)
    print n, f1(n)
    c += 1
    g.write('Case #'+str(c)+': '+str(f1(n))+'\n')
    if (c >= t):
        break
f.close()
g.close()
