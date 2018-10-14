
def read_case(file):
    answer = int(file.readline()) - 1
    for skip in range(4):
        line = file.readline()
        if skip is answer:
            result = set(line.split())
    return result


def read_input(filename):
    with open(filename, "r") as in_file:
        n_cases = int(in_file.readline().split()[0])
        for case in range(n_cases):
            yield case + 1, read_case(in_file), read_case(in_file)


def solve_case(first, second):
    answer = first & second
    if len(answer) == 1:
        return "".join(answer)
    elif answer:
        return "Bad magician!"
    else:
        return "Volunteer cheated!"

cases = read_input("A-small-attempt0.in")
outfile = open("output.txt", "w+")
for case, first, second in cases:
    result = solve_case(first, second)
    outfile.write("Case #{}: {}\n".format(case, result))