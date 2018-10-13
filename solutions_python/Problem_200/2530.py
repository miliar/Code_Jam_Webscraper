countTrials = int(input())
for a in range(countTrials):
    t = []
    for ch in input():
        t.append(int(ch))
    result = str(t[-1])
    for i in range(len(t) - 2, -1, -1):
        if(t[i] > t[i + 1]):
            t[i] -= 1
            for j in range(i, -1, -1):
                if(t[j] < 0):
                    t[j] += 10
                    t[j - 1] -= 1
            result = '9' * len(result)
        result = str(t[i]) + result
    while(result[0] == '0'):
        result = result[1 : ]
    print('Case #%i: %s' % (a + 1, result))