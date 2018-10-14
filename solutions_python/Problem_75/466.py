from sys import stdin

T = int(stdin.readline())
for t in range(0, T):
    combine = { 'Q': list(), 'W': list(), 'E':list(), 'R':list(), 'A':list(), 'S':list(), 'D':list(), 'F':list() }
    oppose = { 'Q': set(''), 'W': set(''), 'E':set(''), 'R':set(''), 'A':set(''), 'S':set(''), 'D':set(''), 'F':set('') } 
    line = stdin.readline().split(' ')
    C = int(line[0])
    for c in range(0, C):
        combine[line[1 + c][0]].append({line[1 + c][1]:line[1 + c][2]})
        if (line[1 + c][0] != line[1 + c][1]):
            combine[line[1 + c][1]].append({line[1 + c][0]:line[1 + c][2]})
    D = int(line[1 + C])
    for d in range(0, D):
        oppose[line[2 + C + d][0]].add(line[2 + C + d][1])
        oppose[line[2 + C + d][1]].add(line[2 + C + d][0])

    N = int(line[2 + C + D])
    stack = []
    stack.append(line[3 + C + D][0])
    tos = 1
    #print 'stack: ' + str(stack)
    for n in xrange(1, N):
        #print line[3 + C + D][n]
        if (tos == 0):
            stack.append(line[3 + C + D][n])
            tos = 1
        elif (stack[tos - 1] in ('Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F')):
            temp = combine[stack[tos - 1]]
            combineResult = '0'
            for i in range(0, len(temp)):
                if ((temp[i].keys())[0] == line[3 + C + D][n]):
                    combineResult = temp[i][(temp[i].keys())[0]]
                    break
            if (combineResult != '0'):
                #print stack[tos - 1] + ' and ' + line[3+ C + D][n] + ' = ' + combineResult
                stack.pop()
                stack.append(combineResult)
                #print 'stack: ' + str(stack) + '\n'
            else:
                #print 'here'
                temp = oppose[line[3 + C + D][n]]
                #print 'oppose = ' + str(temp)
                if (len(temp) == 0):
                    stack.append(line[3 + C + D][n])
                    tos = tos + 1
                else:
                    clear = 0
                    for i in range(0, len(stack)):
                        if (stack[i] in temp):
                            del stack[:]
                            tos = 0
                            clear = 1
                            break
                    if clear == 0:
                        stack.append(line[3 + C + D][n])
                        tos = tos + 1
                #print 'stack: ' + str(stack) + '\n'
        else:
            #print 'here'
            temp = oppose[line[3 + C + D][n]]
            #print 'oppose = ' + str(temp)
            if (len(temp) == 0):
                stack.append(line[3 + C + D][n])
                tos = tos + 1
            else:
                clear = 0
                for i in range(0, len(stack)):
                    if (stack[i] in temp):
                        del stack[:]
                        tos = 0
                        clear = 1
                        break
                if clear == 0:
                    stack.append(line[3 + C + D][n])
                    tos = tos + 1
            #print 'stack: ' + str(stack) + '\n'
    output = 'Case #' + str(t + 1) + ': ' + str(stack)
    output = output.replace('\'', '')
    print output
    #print '-----------------------------------'

