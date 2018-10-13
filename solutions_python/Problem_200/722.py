import sys
inp = sys.stdin.readlines()

cases = int(inp.pop(0))
for case in range(1, cases + 1):
    num = [x for x in inp.pop(0).strip()]
    prev = 'a'
    for i in range(len(num) - 1, -1, -1):
        if num[i] > prev:
            for j in range(i, -1, -1):
                if num[j] == '0':
                    num[j] = '9'
                else:
                    num[j] = str(int(num[j]) - 1)
                    break
            for j in range(i + 1, len(num)):
                num[j] = '9'
        prev = num[i]
    while num[0] == '0': num.pop(0)
    result = ''.join(num)
    print 'Case #{}: {}'.format(case, result)
