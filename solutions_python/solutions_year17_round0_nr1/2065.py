def flip(c):
    if c == '+': return '-'
    return '+'

def damn_apprentice(s, k):
    s = list(s)
    flip_count = 0
    i = 0

    while i <= (len(s) - k):
        if s[i] == '-':
            s[i:i + k] = map(flip, s[i:i + k])
            flip_count += 1
        i += 1

    while i < len(s):
        if s[i] == '-': return 'IMPOSSIBLE'
        i += 1
    return flip_count


t = int(input())
for case in range(1, t + 1):
    (s, k) = input().split()

    print('Case #%d: ' % case, end='')
    print(damn_apprentice(s, int(k)))
