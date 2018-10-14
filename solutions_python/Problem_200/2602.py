

def is_tidy(num):
    num_list = [int(i) for i in list(str(num))]
    for i in range(len(num_list) - 1):
        if num_list[i+1] < num_list[i]:
            return False
    return True


def solve_old(n):
    while n >= 1:
        if is_tidy(n):
            return n
        n -= 1

    raise Exception


def solve(n):
    while not is_tidy(n):
        num_list = [int(i) for i in list(str(n))]
        for i in range(len(num_list) - 1):
            if num_list[i+1] < num_list[i]:
                num_list[i] -= 1
                num_list[i+1:] = [9] * (len(num_list) - i - 1)

        while num_list[0] == 0:
            del num_list[0]

        n = int(''.join([str(i) for i in num_list]))

    return n


if __name__ == "__main__":
    file_in = 'B-large.in'
    with open(file_in) as f:
        input = f.read().splitlines()

    t = int(input[0])
    # t = int(input())

    output = ''

    for case_no in range(t):
        # pancakes, k = parse(input[case_no+1])
        # n = int(input())
        n = int(input[case_no+1])
        # print("Case #{}: {}".format(case_no + 1, solve(n)))
        output += "Case #{}: {}\n".format(case_no + 1, solve(n))

    file_out = 'solutionB_long.out'
    with open(file_out, 'w') as f:
        f.write(output)


