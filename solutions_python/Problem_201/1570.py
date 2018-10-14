import math
from collections import defaultdict
def process_input(input):
    n, k = map(int, input.split())

    a = defaultdict(int)
    for i in range(k):
        ls = math.ceil(n/2) - 1
        rs = n - ls - 1
        a[ls] += 1
        a[rs] += 1
        n = max(a.keys())
        a[n] -= 1
        if a[n] == 0:
            del(a[n])

    return str(rs) + " " + str(ls)

if __name__ == "__main__":

    file_name = "C-small-2-attempt3.in"
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
            #print(1)
            #print (input, output)
            #print("{} -> {}".format(input, output))
            output_lines.append(output)

    # write output file:
    f = open('sample4.out', 'w')
    i = 1
    for l in output_lines:
        f.write("Case #{}: {}\n".format(i, l))
        i += 1
