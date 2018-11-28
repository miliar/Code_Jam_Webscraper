# Magic Trick : Google Code Jam 2014

ncases = int(raw_input())
for i in range(ncases):
    ans1 = int(raw_input())
    mat1 = []
    for j in range(4):
        l = raw_input().split()
        mat1.append(l)
    ans2 = int(raw_input())
    mat2 = []
    for j in range(4):
        l = raw_input().split()
        mat2.append(l)
    r1 = set(mat1[ans1 - 1])
    r2 = set(mat2[ans2 - 1])
    intersection = r1 & r2
    print 'Case #' + str(i + 1) + ':',
    if len(intersection) == 0:
        print 'Volunteer cheated!'
    elif len(intersection) == 1:
        print intersection.pop()
    else:
        print 'Bad magician!'