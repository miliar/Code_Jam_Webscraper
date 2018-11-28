INPUT = r'D:\Repository\CodeJamQualification\A.in'
OUTPUT = r'D:\Repository\CodeJamQualification\A.out'

def intersect(a, b):
    return list(set(a) & set(b))

def decode(temp):
    if temp[-1] == r'\n':
        temp = temp[0:len(str) - 1]
    temp = temp.split(r' ')
    result = []
    for item in temp:
        result.append(int(item))
    return result

def process_single_case(index, input, output):
    print 'Case #', index

    # Read.
    row_1 = int(input.readline()) - 1
    rows_1 = []
    for i in xrange(4):
        rows_1.append(input.readline())
    row_2 = int(input.readline()) - 1
    rows_2 = []
    for i in xrange(4):
        rows_2.append(input.readline())

    # Decode.
    cand_1 = decode(rows_1[row_1])
    cand_2 = decode(rows_2[row_2])

    print cand_1, cand_2
    inter = intersect(cand_1, cand_2)

    # Decide.
    if len(inter) == 0:
        output.write('Case #' + str(index + 1) + ': Volunteer cheated!' + '\n')
    if len(inter) == 1:
        output.write('Case #' + str(index + 1) + ': ' + str(inter[0]) + '\n')
    if len(inter) > 1:
        output.write('Case #' + str(index + 1) + ': Bad magician!' + '\n')

with open(INPUT, 'r') as input:
    input.seek(0)
    with open(OUTPUT, 'w') as output:
        cases = int(input.readline())
        print 'Cases:', cases
        for i in xrange(cases):
            process_single_case(i, input, output)

