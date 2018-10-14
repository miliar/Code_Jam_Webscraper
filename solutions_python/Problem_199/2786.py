t = int(input())

for j in range(1, t + 1):
    s, k = input().split()
    k = int(k)
    sol = 0
    length = len(s)
    for i in range(length - k + 1):
        if s[i] == '-':
            middle = '+' + ''.join(['+' if x == '-' else '-' for x in s[i+1:i+k]])
            s = s[:i] + middle + s[i+k:]
            sol += 1
    flag = True
    for c in s:
        if c == '-':
            print('Case #{0}: IMPOSSIBLE'.format(j))
            flag = False
            break
    if flag:
        print('Case #{0}: {1}'.format(j, sol))
