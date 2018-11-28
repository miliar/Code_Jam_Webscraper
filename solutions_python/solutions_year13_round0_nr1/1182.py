#!/usr/bin/python

import sys

def check_item(it, x_count, o_count, t_count, dot_count):
    if it == 'X':
        x_count += 1
    elif it == 'O':
        o_count += 1
    elif it == 'T':
        t_count += 1
    elif it == '.':
        dot_count += 1
    return x_count, o_count, t_count, dot_count

def return_rules(x_count, o_count, t_count, dot_count):
    if (x_count == 3 and t_count == 1) or x_count == 4:
        return 'X'
    elif (o_count == 3 and t_count == 1) or o_count == 4:
        return 'O'
    elif dot_count > 0:
        return 'N'
    else:
        return 'D'

def check_horizontal(rows):
    results = []
    for r in rows:
        x_count = 0
        o_count = 0
        t_count = 0
        dot_count = 0
        for item in range(0, 4):
            it = r[item]
            x_count, o_count, t_count, dot_count = check_item(it, x_count, o_count, t_count, dot_count)
        results.append(return_rules(x_count, o_count, t_count, dot_count))
        if results[-1] in ('X', 'O'):
            return results[-1]
    return 'N' if 'N' in results else 'D'

def check_vertical(rows):
    results = []
    for item in range(0, 4):
        x_count = 0
        o_count = 0
        t_count = 0
        dot_count = 0
        for r in rows:
            it = r[item]
            x_count, o_count, t_count, dot_count = check_item(it, x_count, o_count, t_count, dot_count)
        results.append(return_rules(x_count, o_count, t_count, dot_count))
        if results[-1] in ('X', 'O'):
            return results[-1]
    return 'N' if 'N' in results else 'D'

def check_diagonal(rows):
    diag_one = [rows[0][0], rows[1][1], rows[2][2], rows[3][3]]
    diag_one_res = check_horizontal([diag_one])
    if diag_one_res in ('X', 'O'):
        return diag_one_res
    diag_two = [rows[0][3], rows[1][2], rows[2][1], rows[3][0]]
    diag_two_res = check_horizontal([diag_two])
    if diag_two_res in ('X', 'O'):
        return diag_two_res
    return None
    
def map_res_to_string(res):
    if res == 'X':
        return 'X won'
    elif res == 'O':
        return 'O won'
    elif res == 'D':
        return 'Draw'
    elif res == 'N':
        return 'Game has not completed'

def solve(in_file, out_file):
    cases = int(in_file.readline())
    for case in range(0, cases):
        rows = []
        for row in range(0, 4):
            in_line = list(str(in_file.readline()[:-1]))
            rows.append(in_line)
        in_file.readline()
        diag_res = check_diagonal(rows)
        if not diag_res is None:
            out_file.write("Case #%d: %s\n" % (case+1, map_res_to_string(diag_res)))
        else:
            h_res = check_horizontal(rows)
            if h_res in ('X', 'O'):
                out_file.write("Case #%d: %s\n" % (case+1, map_res_to_string(h_res)))
            else:
                v_res = check_vertical(rows)
                out_file.write("Case #%d: %s\n" % (case+1, map_res_to_string(v_res)))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print u"Error: Invalid number of arguments. Expected 1 and received %d." % (len(sys.argv) - 1)
        sys.exit(2)

    input_file_name = sys.argv[1]
    output_file_name = input_file_name.split('.')[0] + '.out'
    in_file = open(input_file_name, 'r')
    out_file = open(output_file_name, 'w')
    solve(in_file, out_file)
    in_file.close()
    out_file.close()

