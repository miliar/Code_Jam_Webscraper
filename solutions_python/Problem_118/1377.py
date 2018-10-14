# Google Code Jam (2013): Qualification Round

# Code Jam Utils
# Can be found on Github's Gist at:
# https://gist.github.com/Zren/5376385
from codejamutils import *
from math import sqrt, ceil, floor

problem_id = 'C'

#problem_size = 'sample'
problem_size = 'small'
#problem_size = 'large'

opt_args = {
    #'practice': True,
    'log_level': DEBUG,
}

def is_palindrome(n):
    s = str(n)
    s_r = "".join(reversed(s))
    return s == s_r

with Problem(problem_id, problem_size, **opt_args) as p:
    for case in p:
        info('Case', case.case)
        min, max = case.readints()
        min_sqrt = int(ceil(sqrt(min)))
        max_sqrt = int(floor(sqrt(max)))

        count = 0
        for i in xrange(min_sqrt, max_sqrt+1):
            if not is_palindrome(i):
                continue
            sq = i * i
            if is_palindrome(sq):
                log(sq)
                count += 1
        case.writecase(count)