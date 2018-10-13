def decindex(inp):

    prev = inp[0]
    for i in range(1,len(inp)):
        if inp[i] < prev:
            return i-1
        prev = inp[i]

def process_input(input):

    while True:
        i = decindex(input)
        if i is not None:
            t = int(input[i]) - 1
            s= ""
            for j in range(len(input) - i - 1):
                s += "9"
                input = input[0:i] + str(t) + s
        else:
            return input
    return 0

if __name__ == "__main__":

    file_name = "B-large.in"
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
            print("{} -> {}".format(input, output.strip("0")))
            output_lines.append(output.strip("0"))

    # write output file:
    f = open('sample.out', 'w')
    i = 1
    for l in output_lines:
        f.write("Case #{}: {}\n".format(i, l))
        i += 1
