def flip(b):
    if b == '+':
        return '-'
    else:
        return '+'

for t in range(1, int(input())+1):
    s, k = input().split()
    k = int(k)

    c = 0
    for i in range(len(s)):
        if i+k <= len(s):
            if s[i] == '-':
                a = ''
                for b in s[i:i+k]:
                    a += flip(b)
                s = str(s[:i]) + a + str(s[i+k:])
                c += 1
    if '-' in s:
        c = 'IMPOSSIBLE'

    print('Case #{}: {}'.format(t, c))
    
