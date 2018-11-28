input_file = "B-large.in"
output_file = "result.out"

with open(input_file) as in_file, open(output_file, 'w') as out_file:
    testcases = int(in_file.readline())
    for i in range(1, testcases + 1):
        n = in_file.readline()

        n = [int(j) for j in n if j != '\n']

        pos = len(n) - 2

        while pos >= 0:
            if n[pos] > n[pos +1] :
                n[pos] -= 1
                n = n[:pos+1] + ([9] * (len(n) - pos - 1))
            pos -= 1

        while n[0] == 0:
            n = n[1:]

        out_file.write('Case #{}: {}\n'.format(i, ''.join([str(j) for j in n])))
