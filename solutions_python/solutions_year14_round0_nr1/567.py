T = int(input())
test = 1

while test <= T:
    print("Case #" + str(test) + ": ", end="")
    test += 1

    ans1 = int(input())
    mat1 = []
    for i in range(4):
        mat1.append([int(a) for a in input().split()])
    ans2 = int(input())
    mat2 = []
    for j in range(4):
        mat2.append([int(a) for a in input().split()])
    intersect = [a for a in mat1[ans1-1] if a in mat2[ans2-1]]
    if len(intersect) == 1:
        print(intersect[0])
    elif len(intersect) == 0:
        print("Volunteer cheated!")
    else:
        print("Bad magician!")