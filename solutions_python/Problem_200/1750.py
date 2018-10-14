def Solve(N):
    if (N[-1] == '\n'):
        del N[-1]

    ind = len(N)
    ntequal = len(N)
    for i in range(1,len(N)):
        if (N[i] > N[i - 1]):
            ntequal = i
        if (N[i] < N[i-1]):
            ind = i - 1
            break
    if ind == len(N):
        a = 1
    elif N[ind] == '1':
        L = list();
        for j in range (len(N)-1):
            L.append('9')
        N = L
    else:
        if (ntequal != len(N)):
            ind = ntequal
        if ntequal == len(N) and ind != len(N):
            ind = 0
        N[ind] = str(int(N[ind]) - 1)
        for i in range(ind + 1, len(N)):
            N[i] = '9'
    return ''.join(N)


input = open('task2.in','r')
output = open('output2.txt','w+')
T = int(input.readline())
for t in range(T):
    N = input.readline()
    N = list(N)
    output.write("Case #{}: {}\n".format(t + 1, Solve(N)))