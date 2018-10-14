from sets import Set
t = input()

for i in range(t):
    row_1 = input()
    mat = []
    for j in range(4):
        mat.append(map(int, raw_input().strip().split(' ')))

    set1 = Set(mat[row_1 - 1])
    row_2 = input()
    mat2 = []
    for j in range(4):
        mat2.append(map(int, raw_input().strip().split(' ')))

    set2 = Set(mat2[row_2 - 1])

    x = len(set1.intersection(set2))
    if x == 1:
        answer = set1.intersection(set2).pop()
        print "Case #%d: %d" % (i + 1, answer)
    elif x == 0:
        print "Case #%d: Volunteer cheated!" % (i + 1)
    else:
        print "Case #%d: Bad magician!" % (i + 1)
