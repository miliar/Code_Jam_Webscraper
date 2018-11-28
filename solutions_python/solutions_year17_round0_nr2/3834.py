def getTidy(s):
    s = list(s)
    consecutive = -1
    consecut = -1
    for j in range(0, len(s)-1):
        a = int(s[j])
        b = int(s[j+1])
        if a > b:
            if consecutive < 0:
                consecutive = j
            if s[consecutive] == '1':
                s[consecutive] = ''
            else:
                s[consecutive] = str(int(s[consecutive]) - 1)
            for k in range(consecutive + 1, len(s)):
                s[k] = '9'
            return ''.join(s)
        elif a == b and consecut != a:
            consecutive = j
            consecut = a
    return ''.join(s)

c_num = int(input())
cases = []
for i in range(0, c_num):
    cases.append(input())
for i in range(0, c_num):
    print("Case #%d: %s" % ((i+1), getTidy(cases[i])))
