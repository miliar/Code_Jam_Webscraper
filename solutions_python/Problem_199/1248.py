import sys

def isHappy(s):
    for i in range(len(s)):
        if s[i] == '-' :
            return False
    return True

def flip(s, j, k):
    result = s[:]
    for i in range(j, j + k):
        if result[i] == '+' :
            result[i] = '-'
        else:
            result[i] = '+'
    return result

t = int(sys.stdin.readline())

for i in range(1, t + 1):
    sk = sys.stdin.readline().split(' ')
    s = list(sk[0])
    k = int(sk[1])

    result = 0
    for j in range(0, len(s) - k + 1):
        if isHappy(s) :
            break
        if s[j] == '-' :
            s = flip(s, j, k)
            result += 1
    if not isHappy(s) :
        result = 'IMPOSSIBLE'

    print('Case #{0}: {1}'.format(i, result))
