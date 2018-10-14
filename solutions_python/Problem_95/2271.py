import sys,string

str_before =    'ejp mysljylc kd kxveddknmc re jsicpdrysi'
str_before +=   'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
str_before +=   'de kr kd eoya kw aej tysr re ujdr lkgc jv qz'

str_after =     'our language is impossible to understand'
str_after +=    'there are twenty six factorial possibilities'
str_after +=    'so it is okay if you want to just give up zq'

table = string.maketrans(str_before, str_after)
                  
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
    name, = case
    return name.translate(table)
 
#if not sys.argv[1]:
#sys.argv.append('input.txt')
#sys.argv.append('A-small-attempt0.in')
sys.argv.append('A-small-attempt2.in')
    
cases = parse_cases(ifile(), 1)

answers = [solve(c) for c in cases]
print_answers(answers)



    

        


