import math

f = open('A-small-attempt0.in', 'r')
g = open('Output.txt', 'w')
T = [int(s) for s in f.readline().split() if s.isdigit()][0]

for i in range (0,T):

    row_1 = [int(s) for s in f.readline().split() if s.isdigit()][0]
    A = [[],[],[],[]]
    A[0] = [int(s) for s in f.readline().split() if s.isdigit()]
    A[1] = [int(s) for s in f.readline().split() if s.isdigit()]
    A[2] = [int(s) for s in f.readline().split() if s.isdigit()]
    A[3] = [int(s) for s in f.readline().split() if s.isdigit()]
    A = A[row_1 - 1]

    row_2 = [int(s) for s in f.readline().split() if s.isdigit()][0]
    B = [[],[],[],[]]
    B[0] = [int(s) for s in f.readline().split() if s.isdigit()]
    B[1] = [int(s) for s in f.readline().split() if s.isdigit()]
    B[2] = [int(s) for s in f.readline().split() if s.isdigit()]
    B[3] = [int(s) for s in f.readline().split() if s.isdigit()]
    B = B[row_2 - 1]
    
    C = set(A)&set(B)
    size = len(C)
    if (size == 1):
        case = str(C.pop())
    elif (size == 0):
        case = 'Volunteer cheated!'
    else:
        case = 'Bad magician!'
    ans_str = 'Case #'+str(i+1)+': '+case
    print(ans_str)
    g.write(ans_str)
    if (i+1 != T):
        g.write('\n')

g.close()
