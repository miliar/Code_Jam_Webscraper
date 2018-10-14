lines = open('data.txt').read()
output = open('output.txt', 'w')

lines = lines.splitlines()
cases_num = int(lines[0])
lines = lines[1:]
cur_index = 0
for i in range(cases_num):
    case_num = i + 1
    m, n = lines[cur_index].split()
    n = int(n)
    m = int(m)
    cur_index += 1
    matrix = []
    for row_ind in range(m):
        line = lines[row_ind + cur_index]
        matrix.append([int(x) for x in line.split()])

    rows = []
    columns = []
    for row in matrix:
        rows.append(sorted(set(row)))
    for column in zip(*matrix):
        columns.append(sorted(set(column)))

    def is_lawnable():
        for i in range(m):
            for j in range(n):
                elem = matrix[i][j]
                i_row = rows[i].index(elem)
                j_column = columns[j].index(elem)
                if len(rows[i]) > i_row + 1 and len(columns[j]) > j_column + 1:
                    return False
        return True
    is_good = is_lawnable()
    cur_index += m

    if is_good:
        output.write('Case #{0}:'.format(case_num) + ' YES\n')
        print 'Case #{0}:'.format(case_num), 'YES'
    else:
        output.write('Case #{0}:'.format(case_num) + ' NO\n')
        print 'Case #{0}:'.format(case_num), 'NO'


