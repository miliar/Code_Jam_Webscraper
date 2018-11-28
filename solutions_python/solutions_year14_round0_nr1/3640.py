f = open('inp.in', 'r')
numTests = int(f.readline().strip())
print "floop"
for test in range(numTests):
    testNum = test+1
    ind1 = int(f.readline().strip())
    ind1 -= 1
    arr1 = [f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip()]
    arr1 = [i.split() for i in arr1]

    row1 = arr1[ind1]

    ind2 = int(f.readline())
    ind2 -= 1
    arr2 = [f.readline().strip(), f.readline().strip(), f.readline().strip(), f.readline().strip()]
    arr2 = [i.split() for i in arr2]

    row2 = arr2[ind2]

    overlap = [i for i in row1 if i in row2]

    if len(overlap) == 0:
        ans = "Volunteer cheated!"
    elif len(overlap) == 1:
        ans = str(overlap[0])
    else:
        ans = "Bad magician!"

    print "Case #"+str(testNum)+": "+ans
