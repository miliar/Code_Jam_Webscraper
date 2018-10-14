mul = {
        ('ONE', 'ONE'): 'ONE',
        ('ONE', 'I'): 'I',
        ('ONE', 'J'): 'J',
        ('ONE', 'K'): 'K',
        ('I', 'ONE'): 'I',
        ('I', 'I'): 'NONE',
        ('I', 'J'): 'K',
        ('I', 'K'): 'NJ',
        ('J', 'ONE'): 'J',
        ('J', 'I'): 'NK',
        ('J', 'J'): 'NONE',
        ('J', 'K'): 'I',
        ('K', 'ONE'): 'K',
        ('K', 'I'): 'J',
        ('K', 'J'): 'NI',
        ('K', 'K'): 'NONE'
        }

def mul_cal(a, b):
    neg = False
    if a[0] == 'N':
        neg = not neg
        a = a[1:]
    if b[0] == 'N':
        neg = not neg
        b = b[1:]
    c = mul[(a, b)]
    if neg:
        c = 'N' + c
    while c.startswith('NN'):
        c = c[2:]
    return c

def read_array(convertor=None):
    ret = raw_input().split()
    if convertor: ret = map(convertor, ret)
    return ret



def main():
    for t in range(1, 1+input()):
        L, X = read_array(int)
        s = raw_input().strip().upper() * X
        dp = [set() for _ in range(L*X)]
        dp[0].add((s[0], 'X', 'X'))
        for i in range(1, L*X):
            for prev in dp[i-1]:
                if prev[1] == 'X':
                    level = 1
                elif prev[2] == 'X':
                    level = 2
                else:
                    level = 3

                if level == 1:
                    new1 = (mul_cal(prev[0], s[i]), 'X', 'X')
                    new2 = (prev[0], s[i], 'X')
                    dp[i].add(new1)
                    dp[i].add(new2)
                elif level == 2:
                    new1 = (prev[0], mul_cal(prev[1], s[i]), 'X')
                    new2 = (prev[0], prev[1], s[i])
                    dp[i].add(new1)
                    dp[i].add(new2)
                else:
                    new1 = (prev[0], prev[1], mul_cal(prev[2], s[i]))
                    dp[i].add(new1)

        print 'Case #%d: %s' % (t, ('I', 'J', 'K') in dp[-1] and 'YES'  or 'NO')




main()
