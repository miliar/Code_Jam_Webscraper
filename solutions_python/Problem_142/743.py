import sys


def slim_string(i_string):
    new_string = [(i_string[0], 1)]
    for l in i_string[1:]:
        if l != new_string[-1][0]:
            new_string.append((l, 1))
        else:
            new_string[-1] = (new_string[-1][0], new_string[-1][1] + 1)
    return new_string


def is_compatible(s1, s2):
    return [s[0] for s in s1] == [s[0] for s in s2]


def add_to_average(average, i_string):
    for i in range(len(i_string)):
        # average[i][1] += i_string[i][1]
        average[i] = average[i][0], average[i][1] + i_string[i][1]


def compute_averages(average, N):
    for i in range(len(average)):
        # average[i][1] = int(average[i][1]/N)
        average[i] = average[i][0], int(average[i][1] / N)


def diff_i_strings(s1, s2):
    flips = 0
    for i in range(len(s1)):
        # print(s1, s2)
        flips += abs(s1[i][1] - s2[i][1])
    return flips


def get_flips(i_strings, average):
    flips = 0
    for i_string in i_strings:
        flips += diff_i_strings(i_string, average)
    return flips


def compute_flips(strings):
    leader = slim_string(strings[0])
    average = leader[:]
    i_strings = [leader]
    for current_string in strings[1:]:
        i_string = slim_string(current_string)
        # print(i_string)
        if is_compatible(i_string, leader):
            add_to_average(average, i_string)
            i_strings.append(i_string)
        else:
            return -1
    # print(i_strings)
    # print(average)
    compute_averages(average, len(strings))
    # print(average)
    # print(len(i_strings))
    return get_flips(i_strings, average)


def read_test_case():
    N = sys.stdin.readline().strip()
    N = int(N)
    strings = []
    for _ in range(N):
        strings.append(sys.stdin.readline().strip())
    return strings


def format_answer(index, answer):
    if answer > -1:
        return "Case #%d: %d" % (index + 1, answer)
    else:
        return "Case #%d: Fegla Won" % (index + 1,)


def display_results(answers):
    output_lines = []
    for index in range(len(answers)):
        output_line = format_answer(index, answers[index])
        output_lines.append(output_line)
    output = "\n".join(output_lines)
    with open("repeater_out.txt", "w") as f:
        print("%s" % output, file=f)


def main():
    line = sys.stdin.readline()
    test_cases = int(line.strip())
    answers = []
    for _ in range(test_cases):
        strings = read_test_case()
        flips = compute_flips(strings)
        # print(flips)
        answers.append(flips)
    display_results(answers)


if __name__ == "__main__":
    main()
