import string

def flip_pm(c):
    if (c == '+'):
        return '-'
    return '+'

def case(i):
    line = input().split()
    S = line[0]
    n = len(S)
    k = int(line[1])
    result = 0

    while('-' in S):
        result += 1
        index = S.find('-')

        if (index + k > n):
            print("Case #{}: IMPOSSIBLE".format(i+1))
            return
        
        newS = S[:index]
        for j in range(k):
            newS += flip_pm(S[index + j])
        newS += S[index+k:]
        S = newS

    print("Case #{}: {}".format(i+1, result))

t = int(input())
for i in range(t):
    case(i)
