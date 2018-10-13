def Omino(X, R, C):
    WIDTH = ((R >= (X-1)) or (R >= X)) and ((C >= X-1) or (C >= X)) or (X==1)
    if ((R*C)%X == 0) and WIDTH:
        return "GABRIEL"
    return "RICHARD"

input_file = open('D-small-attempt0.in', 'r')
source = input_file.read()
source = source.splitlines()
input_file.close()
output = open('output.txt', 'w')
for i in range(int(source[0])):
    output.write('Case #%d: '%(i+1))
    [X, R, C] = source[i+1].split()
    winner = Omino(int(X), int(R), int(C))
    output.write(winner + '\n')
output.close()
