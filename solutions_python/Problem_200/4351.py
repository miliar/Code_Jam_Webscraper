def firstProblem(num):
    for i in range(len(num) - 1):
        if int(num[i]) > int(num[i+1]):
            return i
    return -10

def tidy(num):
    s = str(int(num))
    f = firstProblem(s)
    if f < 0:
        return s
    else:
        newS = s[:f] + str(int(s[f]) - 1)
        for i in range(len(s[f+1:])):
            newS += '9'
        return tidy(newS)

t = int(input())
for i in range(1, t + 1):
    num = input()
    print('Case #{}: {}'.format(i, tidy(num)))
