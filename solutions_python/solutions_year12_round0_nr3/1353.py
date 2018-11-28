number_of_cases = int(raw_input())

for i in range(1, number_of_cases + 1):
    c = raw_input()
    ranges = c.split()
    A = int(ranges[0])
    B = int(ranges[1])

    count = 0

    ap = {}
    for j in range(A, B+1):
        strj = str(j)
        lenj = len(strj)
        for k in range(1, lenj):
            if strj[k] == '0':
                continue
            else:
                newj = int(strj[k:] + strj[:k])
                if A <= newj and newj <= B and j <> newj:
                    if newj < j and not (newj, j) in ap:
                        ap[(newj, j)] = 1
                    elif not (j, newj) in ap:
                        ap[(j, newj)] = 1

    print "Case #" + str(i) + ": " + str(len(ap)/2)

