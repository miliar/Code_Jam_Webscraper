def sol(n):
    n = list(str(n))
    for i in reversed(range(1,len(n))):
        if n[i] < n[i-1]:
            n[i-1] = str(int(n[i-1])-1)
            for j in range(i,len(n)):
                n[j] = '9'

    return ''.join([q for q in n if q != '0'])



t = int(input())
for i in range(t):
    n  = int(input())

    print('Case #%d: %s' % (i+1, sol(n)))
