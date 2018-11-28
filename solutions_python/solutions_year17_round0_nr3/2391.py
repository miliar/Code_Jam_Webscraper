def parse_input(input_string):
    lines = input_string.split("\n")
    number_of_inputs = int(lines[0])

    cases = []
    for line in lines[1:]:
        if line:
            input = line.split(' ')
            stalls = [1] + [0]*int(input[0]) + [1]
            cases.append((stalls,int(input[1])))
    return cases


def count_empty_stalls(stalls):
    count = 0
    for s in stalls:
        if s == 0:
            count += 1
        else:
            break
    return count


def choose_a_stall(stalls, bladders):
    for user in range(bladders):
        stall_desirability = []
        for i, stall in enumerate(stalls):
            if stall == 0:
                number_empty_left = count_empty_stalls(reversed(stalls[:i]))
                number_empty_right = count_empty_stalls(stalls[i+1:])
                closest = min(number_empty_right, number_empty_left)
                furthest = max(number_empty_left, number_empty_right)
                stall_desirability.append((i, number_empty_left, number_empty_right, closest, furthest))

        maxmin = max([s[3] for s in stall_desirability])
        furthest_stalls = [s for s in stall_desirability if s[3] == maxmin]

        if len(furthest_stalls) == 1:
            chosen_stall = furthest_stalls[0]
            stalls[chosen_stall[0]] = 1
        else:
            maxmax = max([s[4] for s in furthest_stalls])
            other_stalls = [s for s in furthest_stalls if s[4] == maxmax]
            chosen_stall = other_stalls[0]
            stalls[chosen_stall[0]] = 1
    return "{max} {min}".format(max=chosen_stall[4], min=chosen_stall[3])


def main():
    with open('data.txt', 'r') as f:
        input = f.read()

    cases = parse_input(input)

    total_output = ""
    for i, case in enumerate(cases):
        result = choose_a_stall(*case)
        output = "Case #{i}: {result}\n".format(result=result, i=i+1)
        print(output)
        total_output += output

    with open('out.txt', 'w') as f:
        f.write(total_output)


if __name__ == "__main__":
    main()