d = {'1': '0', '2': '1', '3': '2', '4': '3',
     '5': '4', '6': '5', '7': '6', '8': '7', '9': '8'}
for x in range(int(input())):
    s = list(input())
    n = len(s)
    if n == 1:
        result = s[0]
    else:
        for i in range(n - 1, 0, -1):
            try:
                if s[i] < s[i - 1]:
                    s[i - 1] = d[s[i - 1]]
                    s[i:n] = ['9'] * (n - i)
            except:
                continue
        result = ''.join(s).lstrip('0')
    print('Case #{}: {}'.format(x + 1, result))
