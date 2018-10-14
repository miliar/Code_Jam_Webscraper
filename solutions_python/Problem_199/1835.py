n_cases = int(input())

def flip(s):
    if s == '+':
        return '-'
    else:
        return '+'

for i in range(1, n_cases + 1):
    n_flips =  0
    s, k = input().split(' ')
    s = list(s)
    k = int(k)
    im = False
    for j in range(len(s)):
        if s[j] == '-':
            if j < len(s) - k + 1:
                for m in range(j, j + k):
                    s[m] = flip(s[m])
                n_flips += 1
            else:
                im = True
                break
    if im:
        print('Case #{}: IMPOSSIBLE'.format(i))
    else:
        print('Case #{}: {}'.format(i, n_flips))
