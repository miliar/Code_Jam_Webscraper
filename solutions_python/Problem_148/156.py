import sys

basename = "A-large"

input_filename = basename + ".in"
output_filename = basename + ".out"

input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

test_cases = int(input_file.readline().rstrip())

for case in range(1, test_cases+1):
    N, X = [int(i) for i in input_file.readline().rstrip().split()]
    files = [int(i) for i in input_file.readline().rstrip().split()]

    files.sort()
    count = 0
    while len(files) > 0:
        count += 1
        f1 = files.pop()
        j = -1
        while j+1 < len(files) and files[j+1] <= X - f1:
            j += 1
        if j >= 0:
            files.pop(j)

    solution = str(count)
    
    # Output all goes below here. Make sure to define var 'solution' 
    output_file.write("Case #" + str(case) + ": " + str(solution))
    if case < test_cases:
        output_file.write('\n')

