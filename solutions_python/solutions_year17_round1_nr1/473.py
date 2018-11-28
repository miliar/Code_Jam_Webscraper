def solution(cake):
    result = []
    empty = "?" * len(cake[0])
    current_line = empty
    num_times = 1
    for i in range(len(cake)):
        if cake[i] == empty and current_line == empty:
            num_times += 1
        elif cake[i] == empty:
            result.append(current_line)
        else:
            current_line = replace_line(cake[i])
            for _ in range(num_times):
                result.append(current_line)
            num_times = 1
    return result


def replace_line(cake_row):
    result = ""
    num_times = 1
    current_element = "?"
    for element in cake_row:
        if element == "?" and current_element == "?":
            num_times += 1
        elif element == "?":
            result += current_element
        else:
            result += element * num_times
            current_element = element
            num_times = 1
    return result


def format_output(output, case):
    return "Case #{}:\n{}\n".format(case, "\n".join(output))


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", dest="input_file", help="input file")
    args = parser.parse_args()

    with open(args.input_file) as f, open(args.input_file.replace("in", "out"), "w") as out:
        test_nums = int(f.readline().strip())
        for index in range(test_nums):
            rows, cols = (int(num) for num in f.readline().strip().split(" "))
            cake = []
            for _ in range(rows):
                cake.append(f.readline().strip())
            out.write(format_output(solution(cake), index + 1))


if __name__ == "__main__":
    main()
