import operator
import sys


def combs(s):

    def _combs(s):
        if len(s) == 1:
            return [s]
        res = []
        res.append([s[0]])
        for subs in _combs(s[1:]):
            res.extend([subs, [s[0]] + subs])
        return res
    return _combs(s)

def solve(n, tn):
    sums = {}
    for c in combs(tn):
        s = sum(c)
        if not s in sums:
            sums[s] = c
        else:
            return c, sums[s]

    return "Impossible"

def main(input_filename, output_filename):
    
    input_f = open(input_filename, "r")
    output_f = open(output_filename, "w")
    
    try:
        TEST_CASES_NUM = int(input_f.readline())
        
        for test_case_i in xrange(TEST_CASES_NUM):

            # print test_case_i
            
            inp = [int(_) for _ in input_f.readline().strip().split(' ')]
            n, tn = inp[0], inp[1:]
            
            res = solve(n, tn)
            if isinstance(res, str):
                output_f.write("Case #%d: %s\n" % (test_case_i + 1, res))
            else:
                output_f.write("Case #%d:\n%s\n%s\n" % (test_case_i + 1, 
                                                        ' '.join([str(x) for x in res[0]]),
                                                        ' '.join([str(x) for x in res[1]])))
            
    finally:
        input_f.close()
        output_f.close()


main(sys.argv[1], sys.argv[2])
