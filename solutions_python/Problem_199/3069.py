def flip(p):
    if p == '+': return '-'
    return '+'

def num_flips(s, k):
    flips = 0

    for i in range(len(s)-k+1):
        if s[i] == '-':
            flips += 1
            for j in range(i, i+k):
                s[j] = flip(s[j])

    for i in range(k-1):
        if s[i-k+1] == '-': return 'IMPOSSIBLE'

    return flips

t = int(input())

for i in range(t):
    line = input().strip()
    s, k = line.split(' ')
    s = list(s)
    k = int(k)
    print('Case #' + str(i+1) + ': ' + str(num_flips(s, k)))
