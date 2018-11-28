import sys

filename = sys.argv[1]

def read_num_cases(f):
    return int(f.readline().strip())

def read_case(f):
    row = f.readline().strip().split(" ")
    return (int(row[0]), [int(d) for d in list(row[1])])

with open(filename, 'r') as f:
    num_cases = read_num_cases(f)
    for case in xrange(num_cases):
        s_max, s_vec = read_case(f)
        friends = 0
        accum = 0
        for idx in xrange(s_max+1):
            if accum < idx:
                friends += idx - accum
                accum = idx
            accum += s_vec[idx]
        print("Case #%d: %d" % (case + 1, friends))

