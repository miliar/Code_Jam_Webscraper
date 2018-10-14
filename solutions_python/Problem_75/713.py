import sys
import string

def check_base(current, base) :
    if (len(current) < 2) :
        return current

    postfix = current[-2] + current[-1]
    if postfix in base :
        replacement = base[postfix]
        answer = current[0:-2] + replacement
        return answer
    else :
        return current

def check_opposed(current, opposed) :
    for ele in opposed :
        if (len(ele) == 2) and (ele[0] in current) and (ele[1] in current) :
            return ""

    return current

def pretty_print(str) :
    if len(str) == 0 :
        return "[]" 
    elif len(str) == 1 :
        return "[%s]" % str
    else :
        return "[" + string.join(list(str), ", ") + "]"


def doit(base, opposed, str) :
    current = ""
    for ele in str :
        current += ele
        if len(current) >= 2 :
            current = check_base(current, base)
            current = check_opposed(current, opposed)

    return pretty_print(current)


# C [C base pair + non base], D [opposed], N, [N string]
def solve_case(problem_num, problem) :
    input = string.split(problem, " ")
    pos = 0
    C = int(input[pos])
    pos += 1
    base_pairs = {}

    for i in xrange(C) :
        s = input[pos]
        pos += 1
        base_pairs[s[0]+s[1]] = s[2]
        base_pairs[s[1]+s[0]] = s[2]
    
    D = int(input[pos])
    pos += 1
    opposed_pairs = []
    for i in xrange(D) :
        s = input[pos]
        pos += 1
        opposed_pairs.append(s)

    N = input[pos]
    pos += 1
    str = input[pos]

    print "Case #%d: %s" % (problem_num, doit(base_pairs, opposed_pairs, str))
    

data = file(sys.argv[1]).readlines()
num_cases = int(data[0])

for case in range(num_cases) :
    solve_case(case+1, string.strip(data[case+1]))

