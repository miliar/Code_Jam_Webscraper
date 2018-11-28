case = 0


def handle_case(case_input):

    is_board_full = True
    col_chk_chars = [case_input[0][0], case_input[0][1], case_input[0][2], case_input[0][3]]
    equal_cols = [True, True, True, True]

    diag_chars = [case_input[0][0], case_input[0][3]]
    diag_found = [True, True]

    if diag_chars[0] == "T":
        diag_chars[0] = case_input[1][1]

    if diag_chars[1] == "T":
        diag_chars[1] = case_input[1][2]

    for i, char in enumerate(col_chk_chars):
        if char == ".":
            equal_cols[i] = False
        elif char == "T":
            col_chk_chars[i] = case_input[1][i]

    for idx, row in enumerate(case_input):
        if row[0] == "T":
            chk_idx = 1
        else:
            chk_idx = 0

        if is_equal_row(row, row[chk_idx]):
            print_case(row[chk_idx] + " won")
            return

        for i, char in enumerate(row):
            if char == ".":
                is_board_full = False
                equal_cols[i] = False
            elif char != col_chk_chars[i] and char != "T":
                equal_cols[i] = False

        if (row[idx] != diag_chars[0] and row[idx] != "T") or row[idx] == ".":
            diag_found[0] = False

        if (row[3-idx] != diag_chars[1] and row[3-idx] != "T") or row[3-idx] == ".":
            diag_found[1] = False

    for i, val in enumerate(equal_cols):
        if val:
            print_case(col_chk_chars[i] + " won")
            return

    if (diag_found[0]):
        print_case(diag_chars[0] + " won")
        return

    if (diag_found[1]):
        print_case(diag_chars[1] + " won")
        return

    if is_board_full:
        print_case("Draw")
        return

    print_case("Game has not completed")



def is_equal_row(row, check_char):
    for char in row:
        if char != check_char and char != "T":
            return False
        if char == ".":
            return False
    return True

def print_case(out):
    global case
    case += 1
    print "Case #%i: %s" % (case, out)



with open("in.txt") as fin:
    lines = fin.read().split("\n")

# Remove newlines
while "" in lines:
    lines.remove("")

print "%s cases" % lines[0];
cases = int(lines[0])
lines = lines[1:]


for i in range(0, cases):
    start = i * 4
    end = 4 + (i * 4)
    case_input = lines[start:end]
    handle_case(case_input)
