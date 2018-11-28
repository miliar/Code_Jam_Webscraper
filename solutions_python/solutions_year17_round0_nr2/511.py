import sys

def reverse(s,start,k):
    for i in range(start, start+k):
        if s[i] == '-':
            s[i] = '+'
        else:
            s[i] = '-'

t = int(sys.stdin.readline().strip())
for t0 in range(t):
    n = sys.stdin.readline().strip()
    res = [int(char) for char in n]
    i = 0
    while i < len(res) - 1:
        if res[i] > res[i+1]:
            while i > 0 and res[i] == res[i-1]:
                i -= 1
            # i == 0 or res[i] != res[i-1]
            while i >= 0 and res[i] == 0:
                res[i] = 9
                i -= 1
            # res[i] != 0
            res[i] -= 1
            i += 1
            while i < len(res):
                res[i] = 9
                i += 1
        i += 1
    i = 0
    while res and res[0] == 0:
        res = res[1:]
    print("Case #" + str(t0 + 1) + ': ' + ''.join([str(i) for i in res]))



