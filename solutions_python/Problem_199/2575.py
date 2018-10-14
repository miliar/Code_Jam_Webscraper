testNum = int(input())

for i in range(1, testNum + 1):

    count = 0
    flag = True
    status = []
    instr, pan = input().split(' ')
    status += instr
    pan = int(pan)
    
    for n in range(0, len(status) - pan + 1):
        if (status[n] == '-'):
            for j in range(n, n + pan):
                if(status[j] == '-'):
                    status[j] = '+'
                else:
                    status[j] = '-'
            count += 1
    for n in range(len(status) - pan + 1, len(status)):
        if (status[n] == '-'):
            flag = False
    if (flag):
        print("Case #" + str(i) + ": " + str(count))
    else:
        print("Case #" + str(i) + ": IMPOSSIBLE")

