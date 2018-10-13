def parse_input(file_name):
    with open(file_name) as f:
        lines = f.readlines()

    num_cases = int(lines[0])

    cases = []

    for case_number in range(num_cases):
        shy_max, people_vals = lines[case_number+1].strip("\n").split(" ")
        shy_max = int(shy_max)
        people_vals = [int(val) for val in people_vals]

        cases.append((shy_max, people_vals))

    return cases


def solve_one_case(case):
    # N^2 fast enough for problem sizes.
    shy_max, people_vals = case

    num_friends = 0

    # print("CASE   {}".format(case))
    while True:
        currently_standing = num_friends

        # print("NUM FRIENDS: {}".format(num_friends))
        for shy_tier in range(shy_max + 1):
            currently_standing += people_vals[shy_tier]
            # print("\tSHY TIER: {}".format(shy_tier))
            # print("\tCURRENTLY STANDING: {}".format(currently_standing))
            if currently_standing <= shy_tier:
                break
        # print shy_max
        if shy_tier == shy_max:
            return num_friends
        else:
            num_friends += 1

    raise Exception("No result found, we have a bug.")



def write_output(solved_cases):
    lines = []
    for case_idx, case in enumerate(solved_cases):
        line = "Case #{}: {}".format(case_idx + 1, case)
        lines.append(line)
    with open("output.txt", "w") as f:
        f.write("\n".join(lines))

    with open("output.txt") as f:
        print(f.read())


def solve_all(file_name):
    cases = parse_input(file_name)
    solved_cases = []
    for case in cases:
        solved_case = solve_one_case(case)
        solved_cases.append(solved_case)

    write_output(solved_cases)
    return solved_cases

# print(parse_input("./test_input.txt"))
print(solve_all("/home/tim/Downloads/A-large.in"))
