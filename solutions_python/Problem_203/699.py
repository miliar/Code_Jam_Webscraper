import sys

cakes = []
input = (line.strip() for line in sys.stdin if line.strip())
num_of_cases = int(next(input))
for i in range(num_of_cases):
    cake = []
    rows = int(next(input).split(' ')[0])
    for j in range(rows):
        cake.append(next(input))
    cakes.append(cake)

cases = []


def solve_col(cake, row_index):
    row = cake[row_index]
    for i in range(len(row)):
        k = row_index
        while cake[k][i] == '?':
            k = (k + 1) % len(cake)
        row = row[:i] + cake[k][i] + row[i+1:]
    return row


def solve_column(cake, row_index):
    row = cake[row_index]
    for i in range(len(row)):
        column = ''.join(x[i] for x in cake)
        assert(set(column) != {'?'})
        try:
            while True:
                first_blank = column.index('?')
                if first_blank > 0:
                    column = column[:first_blank] + column[first_blank-1] + column[first_blank+1:]
                else:
                    for letter in column:
                        if letter != '?':
                            column = letter + column[1:]
                            break
        except ValueError:
            pass
        for j, letter in enumerate(column):
            cake[j] = cake[j][:i] + letter + cake[j][i+1:]
    return cake


def solve_row(cake):
    do_later = []
    for i in range(len(cake)):
        row = cake[i]
        if set(row) == {'?'}:
            # new_cake.append(solve_col(cake, i))
            # cake = solve_column(cake, i)
            do_later.append(i)
        else:
            try:
                while True:
                    first_blank = row.index('?')
                    if first_blank > 0:
                        row = row[:first_blank] + row[first_blank-1] + row[first_blank+1:]
                    else:
                        for letter in row:
                            if letter != '?':
                                row = letter + row[1:]
                                break
            except ValueError:
                pass
            cake[i] = row
    for i in do_later:
        cake = solve_column(cake, i)
    return cake


for case_number, cake in enumerate(cakes):
    # solve_row(cake)
    print(('Case #%d:\n' % (case_number + 1)) + '\n'.join(solve_row(cake)))
