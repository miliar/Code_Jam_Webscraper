T = int(input())
num = T

def swap(l):
    for i in range(len(l)):
        if l[i] == '-': l[i] = '+'
        else: l[i] = '-'
    return l

while T:
    T -= 1
    case = num - T
    count = 0
    [s,N] = input().split()
    N = int(N)
    s = list(s)

    for i in range(len(s) - N + 1):
        if s[i] == '-':
            s[i:i + N] = swap(s[i:i + N])
            count += 1

    for i in range(len(s) - 1, len(s) - N, -1):
        if s[i] == '-':
            s[i-N:i] = swap(s[i-N:i])
            count += 1

    if '-' not in s: print("Case #"+ str(case) + ': ' + str(count))
    else: print("Case #"+ str(case) + ': IMPOSSIBLE')