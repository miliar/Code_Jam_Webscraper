def findTidy(n):

    if len(n) == 1:
        if n[0] == 0:
            return ''
        return str(n[0])

    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            b = n[:i+1]
            b[i] -= 1
            return findTidy(b) + '9'*(len(n)-1-i)
    else:
        return ''.join([str(x) for x in n])

t = int(input())
i = 0

while t:
    t -= 1
    i += 1

    n = input()
    n = [int(x) for x in n]

    print("Case #{}: {}".format(i, findTidy(n)))
