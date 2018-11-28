f = open('A-small-attempt2.in')
a = f.readline()
answers = []

def check(inString, caseNum):
    if '.' in inString:
        return False
    elif 'X' in inString and 'O' not in inString:
        answers.append('Case #{}: X won'.format(str(caseNum)))
        return True
    elif 'O' in inString and 'X' not in inString:
        answers.append('Case #{}: O won'.format(str(caseNum)))
        return True
    
for i in range(int(a)):
    c = []
    hasWinner = False
    for b in range(4):
        c.append(f.readline().strip('\n'))
        if not hasWinner and check(c[b], i + 1):
            hasWinner = True
        if b == 3 and not hasWinner:
            if check('{}{}{}{}'.format(c[0][0], c[1][1], c[2][2], c[3][3]), i + 1):
                hasWinner = True
            elif check('{}{}{}{}'.format(c[0][3], c[1][2], c[2][1], c[3][0]), i + 1):
                hasWinner = True
    if not hasWinner:
        for b in range(4):
            if not hasWinner:
                if check('{}{}{}{}'.format(c[0][b], c[1][b], c[2][b], c[3][b]), i + 1):
                    hasWinner = True
    if not hasWinner:
        for v, b in enumerate(c):
            if '.' not in b and v == 3:
                answers.append('Case #{}: Draw'.format(i + 1))
                break
            elif v == 3:
                answers.append('Case #{}: Game has not completed'.format(i+1))
                break
    f.readline()
f.close()
f = open('A-small-attempt2.txt', 'w')
for i in answers:
    f.write(i)
    f.write('\n')
f.close()
