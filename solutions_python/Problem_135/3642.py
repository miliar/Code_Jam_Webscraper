def getNums(f, row):
    line = ''
    for i in range(1, 5):
        if i == row:
            line = f.readline()
        else:
            f.readline()
    return line.split()

f = open('file.in', 'r')
numCases = int(f.readline())

out = ''
for i in range(1, numCases + 1):
    nums1 = getNums(f, int(f.readline()))
    nums2 = getNums(f, int(f.readline()))

    vals = {}
    for j in range(len(nums1)):
        if nums1[j] not in vals:
            vals[nums1[j]] = 0
        vals[nums1[j]] += 1

        if nums2[j] not in vals:
            vals[nums2[j]] = 0
        vals[nums2[j]] += 1
    
    intsct = []
    for j in vals.keys():
        if vals[j] == 2:
            intsct.append(j)
    
    out += 'Case #' + str(i) + ': '
    if len(intsct) == 1:
        out += intsct[0]
    elif len(intsct) > 1:
        out += 'Bad magician!'
    else:
        out += 'Volunteer cheated!'
    out += '\n'
f.close()

f = open('file.out', 'w')
f.write(out)
f.close()
