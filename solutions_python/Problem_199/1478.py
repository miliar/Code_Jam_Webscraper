input_file = "A-large.in"
output_file = "result.out"

with open(input_file) as in_file, open(output_file, 'w') as out_file:
    testcases = int(in_file.readline())
    for i in range(1, testcases + 1):
        help = in_file.readline().split()
        pancakes = list(help[0])
        size = int(help[1])

        l = len(pancakes)
        count = 0
        j = 0

        while j + size <= l:
            if pancakes[j] != '+':
                count += 1
                for k in range(0, size):
                    pancakes[j+k] = '+' if pancakes[j+k] == '-' else '-'
            j += 1

        while j < l:
            if pancakes[j] != '+':
                count = -1
                break
            j += 1

        out_file.write('Case #{}: {}\n'.format(i, str(count) if count >= 0 else 'IMPOSSIBLE'))
