
def read_cases(path):
    f = open(path)
    lines_count = int(f.readline())
    lines = [line.strip() for line in f.readlines()]
    for i in range(lines_count):
        yield lines[i*5:i*5+4]

def work_on_case(case):
    value = [is_win_row(row) for row in check_rows(case)]
    if any([v == "O" for v in value]):
        return "O won"
    elif any([v == "X" for v in value]):
        return "X won"
    elif all([v =="progress" for v in value]):
        return "Game has not completed"
    else:
        return "Draw"

def check_rows(case):
    yield case[0]
    yield case[1]
    yield case[2]
    yield case[3]
    for i in range(4):
        yield [case[j][i] for j in range(4)]
    yield [case[i][i] for i in range(4)]
    yield [case[i][-i-1] for i in range(4)]

def is_win_row(quartet):
    if all([d == "O" or d == "T" for d in quartet]):
        return "O"
    elif all([d == "X" or d == "T" for d in quartet]):
        return "X"
    elif any([d == "." for d in quartet]):
        return "progress"
    else:
        return None

if __name__ == "__main__":
    tic_result = open(r"C:\temp\ticout.txt", "w")
    for i, case in enumerate(read_cases(r"C:\temp\A-small-attempt0.in")):
        result = work_on_case(case)
        print("Case #%d: %s" % (i+1, result), file=tic_result)
    tic_result.close()
