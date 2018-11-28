repeat = int(input())
for i in range(repeat):
    row0 = int(input())
    mat0 = []
    for j in range(4):
        line = input()
        if j == row0 - 1:
            mat0 = [int(a) for a in line.split(" ")]
    row1 = int(input())
    mat1 = []
    for j in range(4):
        line = input()
        if j == row1 - 1:
            mat1 = [int(a) for a in line.split(" ")]
    result = 0
    for a in mat0:
        if a in mat1:
            if result == 0:
                result = a
            else:
                result = -1
    if result == -1:
        print("Case #"+str(i+1)+": Bad magician!")
    elif result == 0:
        print("Case #"+str(i+1)+": Volunteer cheated!")
    else:
        print("Case #"+str(i+1)+": "+str(result))