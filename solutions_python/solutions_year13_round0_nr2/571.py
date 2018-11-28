import sys

basename  = sys.argv[0][0:-3]

#basename = basename + "-practice"
#basename = "B-small-attempt0"
basename = "B-large"

input_filename = basename + ".in"
output_filename = basename + ".out"

input_file = open(input_filename, 'r')
output_file = open(output_filename, 'w')

test_cases = int(input_file.readline().rstrip())

for case in range(1, test_cases+1):
    N, M = [int(i) for i in input_file.readline().rstrip().split()]
    lawn = [[int(i) for i in input_file.readline().rstrip().split()] for j in range(N)]

    mowedlawn = [[100 for col in range(M)] for row in range(N)]

    for row in range(N):
        height = max(lawn[row])
        mowedlawn[row] = [min(i, height) for i in mowedlawn[row]]

    for col in range(M):
        height = max([lawn[row][col] for row in range(N)])
        for row in range(N):
            mowedlawn[row][col] = min(mowedlawn[row][col],height)
    
    if mowedlawn == lawn:
        result = "YES"
    else:
        result = "NO"

    output_file.write("Case #" + str(case) + ": " + result)
    if case < test_cases:
        output_file.write('\n')

