def parse_input(input_string):
    lines = input_string.split("\n")
    number_of_inputs = int(lines[0])

    cases = []
    for line in lines[1:]:
        if line:
            cases.append((line,))
    return cases


def last_tidy_number(nbr):
    digits = [int(n) for n in reversed(nbr)]

    for i in range(len(digits)-1):
        if digits[i] < digits[i+1]:
            for j in range(i+1):
                digits[j] = 9
            digits[i+1] = digits[i+1] - 1

    digits = digits[::-1]
    for i, d in enumerate(digits):
        if d == 0:
            del(digits[i])
        else:
            break

    return ''.join([str(d) for d in digits])


def main():
    with open('data.txt', 'r') as f:
        input = f.read()

    cases = parse_input(input)

    total_output = ""
    for i, case in enumerate(cases):
        result = last_tidy_number(*case)
        output = "Case #{i}: {result}\n".format(result=result, i=i+1)
        print(output)
        total_output += output

    with open('out.txt', 'w') as f:
        f.write(total_output)


if __name__ == "__main__":
    main()