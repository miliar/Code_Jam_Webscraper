__author__ = 'Niels De Bock'

nbCases = int(raw_input())
for o in range(1,nbCases+1):
    row1 = int(raw_input())
    matrix1 = []
    for _ in range(4):
        matrix1.append(map(int, raw_input().split()))
    possibilities = set(matrix1[row1-1])

    row2 = int(raw_input())
    matrix2 = []
    for _ in range(4):
        matrix2.append(map(int, raw_input().split()))
    possibilities = possibilities.intersection(set(matrix2[row2-1]))

    if len(possibilities) == 0:
        print "Case #"+str(o)+": "+"Volunteer cheated!"
    elif len(possibilities) == 1:
        print "Case #"+str(o)+": "+str(list(possibilities)[0])
    else:
        print "Case #"+str(o)+": "+"Bad magician!"

