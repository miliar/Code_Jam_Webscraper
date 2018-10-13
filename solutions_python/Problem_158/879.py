inputF = open('D-small-attempt0.in', 'r')
output = open('D-small-attempt0.out', 'w')

numCases = int(inputF.readline())

for i in range(numCases):
    line = inputF.readline()
    split = map(lambda x: int(x), line.split())
    X = split[0]
    R = split[1]
    C = split[2]
    breakable = False

    if X == 2 and (R*C)%2 == 1:
        breakable = True
    elif X == 3:
        if (R*C)%3 != 0:
            breakable = True
        elif R == 1 or C == 1:
            breakable = True
    elif X == 4:
        if (R*C)%4 != 0:
            breakable = True
        elif R <= 2 or C <= 2:
            breakable = True
    

    if breakable:
        winner = 'RICHARD'
    else:
        winner = 'GABRIEL'
    output.write('Case #' + str(i+1) + ': ')
    output.write(winner + '\n')




inputF.close()
output.close()
