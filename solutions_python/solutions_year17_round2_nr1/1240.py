def process_input(d, n, arr):

    lst = []
    for i in arr:
        lst.append((d-i[0])/(i[1]*1.0))

    a = max(lst)

    return '%.6f'%(d/a)

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


            d, n = map(int, input_line.strip().split())
            arr = []
            for i in range(n):
                arr.append(map(int, f.next().split()))
            output = process_input(d, n, arr)
            print("{} -> {}".format(input, output))
            output_lines.append(output)

    # write output file:
    f = open('answer.out', 'w')
    i = 1
    for l in output_lines:
        f.write("Case #{}: {}\n".format(i, l))
        i += 1
