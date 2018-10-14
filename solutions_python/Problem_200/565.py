def tidy(N):
    tidy = True
    for i in range(len(N)-1):
        if int(N[i]) > int(N[i+1]):
            tidy = False
            break
    return tidy



fread = open('B-large.in')
lines = fread.readlines()
fw = open('output2', 'w')

T = int(lines[0][0:-1])
for t in range(T):
    N = list(lines[t+1][0:-1])

    while not tidy(N):
        for i in range(len(N)-1):
            if int(N[i]) > int(N[i+1]):
                N[i] = str(int(N[i]) - 1)
                for j in range(i+1, len(N)):
                    N[j] = '9'

    result = int(''.join(N))
    fw.write('Case #{}: {}\n'.format(t+1, result))
