def magic_trick(filename):
    with open(filename, 'r') as f:
        t = int(f.readline())
        cases = []
        for i in range(t):
            cases.append(read_test_case(f))
        for i, case in enumerate(cases):
            print("Case #" +  str(i + 1) + ":", solve(case))

def read_test_case(f):
    first_ans = int(f.readline())
    for i in range(4):
        if i + 1 == first_ans:
            first_row = f.readline().strip().split(' ')
        else:
            f.readline()
    second_ans = int(f.readline())
    for i in range(4):
        if i  + 1 == second_ans:
            second_row = f.readline().strip().split(' ')
        else:
            f.readline()
    return (first_row, second_row)

def solve(case):
    first = case[0]
    second = case[1]
    union = set(first + second)
    if len(union) == 8:
        return "Volunteer cheated!"
    elif len(union) < 7:
        return "Bad magician!"
    else:
        return list(filter(lambda elem: elem in second, first))[0]

# magic_trick('sample_test_case.txt')
magic_trick('A-small-attempt0.in')
