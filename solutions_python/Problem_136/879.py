INPUT = r'D:\Repository\CodeJamQualification\B.in'
OUTPUT = r'D:\Repository\CodeJamQualification\B.out'

def get_opt_time(t, a, C, F, X):
    tc = 0.0
    while True:

        # Choose strategy.
        dtp = C / a
        ti = C / F + dtp
        if ti * a >= X:
            tc += X / a
            break
        else:
            tc += dtp
            a += F

    # Return result.
    return tc

def process_single_case(index, input, output):
    print 'Case #', (index + 1)

    # Read.
    line = input.readline()
    if line[-1] == r'\n':
        line = line[0:len(str) - 1]
    temp = line.split(' ')

    # Decode.
    C = float(temp[0])
    F = float(temp[1])
    X = float(temp[2])

    # Decide.
    tc = get_opt_time(0.0, 2.0, C, F, X)
    print 't =', tc
    output.write('Case #' + str(index + 1) + ': ' + str(tc) + '\n')

with open(INPUT, 'r') as input:
    input.seek(0)
    with open(OUTPUT, 'w') as output:
        cases = int(input.readline())
        print 'Cases:', cases
        for i in xrange(cases):
            process_single_case(i, input, output)
