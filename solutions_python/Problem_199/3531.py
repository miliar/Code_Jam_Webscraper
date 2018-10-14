def flip():
    global runner, debt, cnt, i, k

    assert i+k <= len(s)

    runner = (runner+1)%2
    debt[i+k] = (debt[i+k]+1)%2
    cnt += 1

def to_binary(s):
    m = {'+':1, '-':0}
    return m[s]

with open('in', 'r') as f:
    T = int(f.readline())
    testcases = [line[:-1].split(' ') for line in f.readlines()]

t = 1
for s, k in testcases:
    k = int(k)
    s = list(map(to_binary, s))
    i = 0
    cnt = 0
    runner = 0
    debt = [0] * (len(s) + 1)

    while i < len(s):
        runner += debt[i]
        runner %= 2
        if (runner + s[i]) % 2 != 1:
            if (i + k > len(s)):
                print('Case #{}: IMPOSSIBLE'.format(t))
                break
            else:
                flip()
        i += 1
    else:
        print('Case #{}: {}'.format(t, cnt))
    t += 1
