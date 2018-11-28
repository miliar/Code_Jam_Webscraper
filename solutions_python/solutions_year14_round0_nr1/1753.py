input = open("jamcode.txt")

T = int(input.readline())

for i in range(T):
    first_line = int(input.readline())
    for j in range(4):
        line = input.readline()
        line = line[:-1]
        if (j == first_line - 1):
            candidats = [int(x) for x in line.split()]
    second_line = int(input.readline())
    for k in range(4):
        line = input.readline()
        line = line[:-1]
        if (k == second_line - 1):
            candidats2 = [int(x) for x in line.split()]
    intersect = [val for val in candidats if val in candidats2]
    if (len(intersect) == 0):
        print("Case #"+str(i+1)+": Volunteer cheated!")
    elif (len(intersect) > 1):
        print("Case #"+str(i+1)+": Bad magician!")
    else:
        print("Case #"+str(i+1)+": "+str(intersect[0]))
