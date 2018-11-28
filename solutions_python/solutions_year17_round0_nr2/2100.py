def findTidy(s):
    n = list(s)
    for i in range(len(n)-1, 0, -1):
        if ord(n[i-1]) > ord(n[i]):
            n[i-1] = chr(ord(n[i-1]) - 1)
            for j in range(i, len(n)):
                n[j] = '9'
    return ''.join(n).lstrip('0')

t = int(input())
for i in range(1, t + 1):
    print('Case #'+str(i)+': '+findTidy(input()))