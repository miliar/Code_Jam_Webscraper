def solver(snum):
    for i in range(len(snum)-1):
        if snum[i] > snum[i+1]:
            return solver(snum[0:i] + str(int(snum[i])-1) + '9'*(len(snum)-i-1))
    if snum[0] == '0':
        return snum[1:len(snum)]
    return snum

t = input()
t = int(t)
for i in range(t):
    lines = input()
    print("Case #{0}: {1}".format(i+1, solver(lines)))
    