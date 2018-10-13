def check_lawn(input,N,M):
    check = True
    inputT = map(list, zip(*input))
    for line in inputT:
        if min(line) != max(line):
            b = [item for item in range(len(line)) if line[item] == min(line)]
            for index in b:
                if input[index].count(min(line)) != M:
                    check = False
    if check == True:
        return 'YES'
    else :
        return 'NO'



num = raw_input()
for i in range(0,int(num)):
    N_M = raw_input()
    N_M = N_M.split(' ')
    N = int(N_M[0])
    M = int(N_M[1])
    input = []
    for line in range(0,int(N)):
        inp = raw_input()
        input.append(inp.split(' '))
    print 'Case #'+str(i+1)+': '+check_lawn(input,N,M)