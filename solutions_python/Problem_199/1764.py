import sys

sys.stdin = open('A-large.in', 'r')
sys.stdout = open('A_large.out', 'w')

def flip(j, k, s):
    sout = s
    flip.count += 1
    for j in range(j, j + k):
        sout[j] = '+' if s[j] == '-' else '-'
    return sout


def check(s):
    out = True
    for c in s:
        out = out and c == '+'
    return out


def iterate(s, k):
    for j in range(len(s)):
        if j + k <= len(s) and s[j] == '-':
            s = flip(j, k, s)
            if check(s):
                return True
    return False


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    u = input().split(" ")
    s = []
    flip.count = 0
    for c in u[0]:
        s.append(c)
    k = int(u[1])
    if check(s):
        print("Case #{}: {}".format(i, flip.count))
    elif iterate(s, k):
        print("Case #{}: {}".format(i, flip.count))
    else:
        print("Case #{}: IMPOSSIBLE".format(i))
