from optparse import OptionParser

def solve_b(ngooglers, nsurprise, pmax, total_scores):
    res = 0
    for s in total_scores:
        d, m = divmod(s, 3)
        if m == 0:
            max_nosurprise = d
        else:
            max_nosurprise = d + 1
        if m == 2:
            max_surprise = d + 2
        else:
            if d == 0:
                max_surprise = 0
            else:    
                max_surprise = d + 1
        if max_nosurprise >= pmax:
            res += 1
        elif max_surprise >= pmax and nsurprise > 0:
            res += 1
            nsurprise -= 1
    return res

def problem_B(filename):
    with open(filename, 'rU') as fin:
        lines = [l.rstrip("\n") for l in fin.readlines()]
        
    ntestcases = int(lines[0])
    
    for i in range(ntestcases):
        testcase = [int(j) for j in lines[i + 1].split(" ")]
        ngooglers = testcase[0]
        nsurprise = testcase[1]
        pmax = testcase[2]
        total_scores = testcase[3:]
        assert len(total_scores) == ngooglers
        print "Case #%d: %s" % (i+1, str(solve_b(ngooglers, nsurprise, pmax, total_scores)))





if __name__ == "__main__":
    parser = OptionParser()
    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("incorrect number of arguments")
    problem_B(args[0])