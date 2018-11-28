from sys import stdin, stdout
stdin = open('A-large.in', 'r')
input = stdin.readline
def standing(n, s, c):
    h, t = 0, int(s[0])
    for i in range(1, n + 1):
        x = int(s[i])
        if i > t and x:
            c += i - t
            h += i - t
            t += i - t
        if x: h = i
        t += x
    return c
print('\n'.join('Case #%d: %d' % (i, standing(*(lambda x: (int(x[0]), x[1], 0))(input().split()))) for i in range(1, int(input()) + 1)))
stdin.close()
