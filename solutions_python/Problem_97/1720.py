import sys,string

                  
def ifile():
    filename = sys.argv[1]
    return open(filename, 'r').read()

def parse_cases(input, lines_per_case):
    lines = input.split('\n')
    numcases = lines[0]
    cases = []
    i = 1
    while i < (len(lines)-1):
        c = lines[i:(i + lines_per_case)]
        cases.append(tuple(c))
        i += lines_per_case
    return cases

def print_answers(answers):
    """Accepts a list of answers. 
            Each answer can be string, or list of integer.
            Prints Case #n: x y z , etc where [x y z] is a list of integers, 
                                            or 'x y z' is a string.
    """
    for case,a in enumerate(answers):
        if isinstance(a, basestring):
            output = a
        else:
            output = ' '.join(str(i) for i in a)
        print 'Case #%s: %s' % (case + 1, output)

def solve(case):
    a,b = case[0].split()
    small   = int(a)
    big     = int(b)

    ans = 0
    #for c in a:
    for n in range(small, big+1):
        test_str = str(n)
        
        for i in range(len(test_str)):
            if test_str[i] == '0': continue
            r_str = test_str[i:] + test_str[:i]
            if int(r_str) == n: continue
            
            r = int(r_str)
            if r > big or r < small:
                continue
            else:
                ans += 1       
    
    return str(ans/2)
 
sys.argv.append('C-small-attempt0.in')
    
cases = parse_cases(ifile(), 1)

answers = [solve(c) for c in cases]
print_answers(answers)
