import sys


def solve_problem(input):
    ret = []
    num_cases = int(input.readline())
    for idx in xrange(num_cases):
        try:
            max_shyness, case = input.readline().split(' ')
            needed = range(0, int(max_shyness) + 1)
            missing = []
            standing = []
            missing.append(0)
            standing.append(int(case[0]))
            for k in range(1, int(max_shyness)+1):
                try:
                    shy_count = int(case[k])
                    missing_count = needed[k]-standing[k-1]
                    if shy_count > 0 and missing_count > 0:
                        missing.append(missing_count)
                    else:
                        missing.append(0)
                    standing.append(standing[k-1] + shy_count + missing[k])
                except:
                    print k
                    raise
            total_missing = sum(missing)
        except:
            print idx
            raise
        else:
            ret.append('Case #%d: %d\n' % (idx+1, total_missing if total_missing > 0 else 0))
    return ret

with open(sys.argv[1], 'r') as input_file:
    result = solve_problem(input_file)
    f_out = open('standingovation.out', 'w+')
    f_out.writelines(result)
    f_out.close()



