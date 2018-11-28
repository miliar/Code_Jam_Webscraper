import sys

def cases(l, T):
    case_len = len(l) / T
    for i in xrange(0, len(l), case_len):
        yield l[i:i+case_len]

def outcome(solution):
    output = ''
    if len(solution) > 1:
        output = "Bad magician!"
    elif len(solution) < 1:
        output = "Volunteer cheated!"
    else:
        output = solution.pop()
    return output

def main():
    args = sys.argv
    if len(args) < 2:
        print('Forgot an argument')
        sys.exit()
    filename = args[1]
    with open(filename, 'r') as f_in:
        input_text = f_in.read().splitlines()

    T, cases_list = int(input_text[0]), input_text[1:]
    output = []

    for i, case in enumerate(cases(cases_list, T)):
        i += 1
        ans1, grid1 = int(case[0]), [x.split() for x in case[1:5]]
        row1 = set(grid1[ans1 - 1])

        ans2, grid2 = int(case[5]), [x.split() for x in case[6:]]
        row2 = set(grid2[ans2 - 1])

        solution = row1.intersection(row2)

        output_string = "Case #{0}: {1}".format(i, outcome(solution))
        print(output_string)



if __name__ == '__main__':
    main()
