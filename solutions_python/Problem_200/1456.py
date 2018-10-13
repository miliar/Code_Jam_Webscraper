def check(nl, i):
    if i == 0:
        return check(nl, i+1)
    if i == len(nl):
        return nl
    if nl[i] < nl[i-1]:
        nl[i-1] -= 1
        for k in range(i, len(nl)):
            nl[k] = 9
        if nl[i-1] < nl[i-2]:
            return check(nl, i-1)
    return check(nl, i+1)


input = open('input2.txt', 'r')
t = int(input.readline())
for i in range(t):
    n = input.readline()
    nl = []
    for d in n[:-1]:
        nl.append(int(d))
    nl = check(nl, 0)
    for k in range(len(nl)):
        nl[k] = str(nl[k])
    print "Case #" + str(i+1) + ": " + str(int(''.join(nl)))


