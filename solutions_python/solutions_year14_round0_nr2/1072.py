import sys
from math import floor

basename = "B-large"

input_filename = basename + ".in"
output_filename = basename + ".out"

input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

test_cases = int(input_file.readline().rstrip())

for case in range(1, test_cases+1):
    C, F, X = [float(i) for i in input_file.readline().rstrip().split(" ")]
   
    n = max(floor( (F*X-2*C) / (C*F)), 0)
    time = sum([C/(2+i*F) for i in range(n)]) + X/(n*F+2)
    solution = str(time)

    # Output all goes below here. Make sure to define var 'solution' 
    output_file.write("Case #" + str(case) + ": " + str(solution))
    if case < test_cases:
        output_file.write('\n')

