import sys

def assign_row_wise(row):
    current_initial = None
    current_start = 0
    current_end = 0
    initial_row_span_dict = {}
    for c, cell in enumerate(row):
        if cell != '?':
            if current_initial is not None and cell != current_initial:
                initial_row_span_dict[current_initial] = [current_start, c]
                current_start = c
            current_initial = cell
        current_end = c

    if current_initial is not None:
        initial_row_span_dict[current_initial] = [current_start, current_end + 1]

        if cell != '?':
            if current_initial is not None and cell != current_initial:
                initial_row_span_dict[cell] = (current_start, c)
                current_start = c

            current_initial = cell

    for initial in initial_row_span_dict:
        start, end = initial_row_span_dict[initial]
        assign(row, start, end, initial)

    return initial_row_span_dict

def count_unassigned(row, start, end):
    total = 0
    for i in xrange(start, end):
        if row[i] == '?':
            total += 1
    return total

def assign(row, start, end, initial):
    for cell_ind in xrange(start, end):
        row[cell_ind] = initial

def cross_assign(ref_row, ref_span_info, row, row_span_info):
    # print ref_row, row, ref_span_info, row_span_info
    for initial in ref_span_info:
        start, end = ref_span_info[initial]
        span_length = end - start
        if count_unassigned(row, start, end) == span_length:
            assign(row, start, end, initial)
            row_span_info[initial] = [start, end]

def main(cake):
    row_span_info = [assign_row_wise(row) for row in cake]

    # print cake
    for i in xrange(len(cake) - 1):
        cross_assign(cake[i], row_span_info[i], cake[i + 1], row_span_info[i + 1])
        cross_assign(cake[i + 1], row_span_info[i + 1], cake[i], row_span_info[i])

    for i in xrange(len(cake) - 1, 0, -1):
        cross_assign(cake[i], row_span_info[i], cake[i - 1], row_span_info[i - 1])
        cross_assign(cake[i - 1], row_span_info[i - 1], cake[i], row_span_info[i])

    cake_str = ''
    for row in cake:
        for cell in row:
            cake_str += cell
        cake_str += "\n"
    # print cake_str
    # print
    return cake_str




if __name__ == '__main__':
    input_file = sys.argv[1]
    output_file = input_file.split('.')[0] + '_output.txt'
    with open(input_file, 'rb') as f:
        with open(output_file, 'wb') as o:
            T = int(f.readline().rstrip())
            case_num = 1
            while T > 0:
                case = f.readline().rstrip().split(' ')
                R, C = int(case[0]), int(case[1])
                cake = [list(f.readline().rstrip()) for row_num in xrange(R)]
                answer = main(cake)
                o.write("Case #" + str(case_num) + ": " + "\n" + answer)
                T -= 1
                case_num += 1