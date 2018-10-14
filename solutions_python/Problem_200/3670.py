def is_tidy(n):
    n = str(n)
    tidy = True
    previous = '0'
    for digit in n:
        if digit < previous:
            return False
        previous = digit
    return True

def last_tidy(n):
    for i in range(n,0,-1):
        if is_tidy(i):
            return i

def solve_file(file_path):
    f = open(file_path)
    solution = open('tidy_results.txt','w')
    # skip first line and read remaining lines
    case_number = 1
    for line in f.readlines()[1:]:
        if line[0] != '#':
            result = last_tidy(int(line))
            print('Case #{}: {}'.format(case_number,result),file=solution)
            case_number += 1

solve_file('B-small-attempt0.in')
