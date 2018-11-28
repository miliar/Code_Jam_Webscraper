inp = raw_input()
inp = inp.split('\n')
T = int(inp[0])
case = 0
while T:
    case = case + 1
    num1 = int(inp[1+(case-1)*10])
    row1 = inp[1+(case-1)*10+num1]
    row1 = row1.split(' ')
    num2 = int(inp[1+case*10-5])
    row2 = inp[1+case*10+num2-5]
    row2 = row2.split(' ')
    param = 0
    for i in range(0,4):
        for j in range(0,4):
            if row1[i] == row2[j]:
                param = param + 1
                answer = row2[j]
    if param == 0:
        print 'Case #'+str(case)+': Volunteer cheated!'
    elif param == 1:
        print 'Case #'+str(case)+':',answer
    else:
        print 'Case #'+str(case)+': Bad magician!'
    T = T - 1
    
