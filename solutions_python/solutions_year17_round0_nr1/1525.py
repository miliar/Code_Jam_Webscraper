def process_input(input):
    input = input.split()
    pk = list(input[0])
    k = int(input[1])
    n = len(pk)

    output = 0

    for i in range(n):
        if pk[i] == "+":
            continue
        else:
            if i+k <= n:
                ul = i+k
            else:
                break
            for j in range(i, ul):
                if pk[j] == "+":
                    pk[j] = "-"
                else:
                    pk[j] = "+"
            output += 1
    if "-" in pk:
        output = "IMPOSSIBLE"

    return output

if __name__ == "__main__":

    file_name = "A-large.in"
    output_lines = []
    with open(file_name) as f:
        first_input_line = True
        for input_line in f:
            if first_input_line:
                t = int(input_line.strip())
                first_input_line = False
                continue

            input = input_line.strip()
            output = process_input(input)
            print("{} -> {}".format(input, output))
            output_lines.append(output)

    # write output file:
    f = open('sample.out', 'w')
    i = 1
    for l in output_lines:
        f.write("Case #{}: {}\n".format(i, l))
        i += 1
