__author__ = 'danolsen'

def check(n, m, lawn_array):
    for nn in range(0, n, 1):
        for mm in range(0, m, 1):
            # Check the row
            is_max_row = True
            for nnn in range(0, n, 1):
                if nn != nnn:
                    if lawn_array[nn][mm] < lawn_array[nnn][mm]:
                        is_max_row = False
                        break

            is_max_col = True
            for mmm in range(0, m, 1):
                if mm != mmm:
                    if lawn_array[nn][mm] < lawn_array[nn][mmm]:
                        is_max_col = False
                        break

            if not is_max_row and not is_max_col:
                return False
    return True

f = open('lawn_input.txt', 'r')
test_cases = f.readline()
test_cases = int(test_cases.strip())

for i in range(0, test_cases, 1):
    lawn_array = []
    dimensions = f.readline().strip().split()
    n = int(dimensions[0])
    m = int(dimensions[1])

    for j in range(0, n, 1):
        line = f.readline().strip().split()
        for x in range(0, len(line), 1):
            line[x] = int(line[x])
        lawn_array.append(line)

    # print '%d x %d' % (n, m)
    # print lawn_array

    is_possible = check(n, m, lawn_array)

    if is_possible:
        answer = 'YES'
    else:
        answer = 'NO'

    print 'Case #%d: %s' % (i + 1, answer)