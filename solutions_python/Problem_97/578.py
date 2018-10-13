'''
Created on Apr 14, 2012

@author: shelajev
'''
from math import log10
from os.path import abspath

def solve(a, b):
    pairs = set()
    for n in range(a, b + 1):
        l = int(log10(n)) + 1
        for i in range(1, l):
            d = 10**i
            x, y = n / d, n % d
            m =  y * 10**(l - i) + x
            if a <= n < m <= b:
                pairs.add((n, m))
    return len(pairs)

def main():
    problem = 'C'
    attempt = 0
#    filename = 'input-%s.sample' % problem
#    filename = '%s-small-attempt%s' % (problem, attempt)
    filename = '%s-large' % problem
    input_file = file('in/%s.in' % filename)
    output_path = 'out/%s.out' % filename
    output_file = open(output_path, 'w')
    num_cases = 0
    T = 0
    for line in input_file.readlines():
        if ' ' not in line:
            num_cases = int(line.rstrip())
            continue
        T+=1
        line = line.rstrip().split()
        a = int(line[0])
        b = int(line[1])
        line = 'Case #%s: %s' % (T, solve(a, b))
#        print line
        output_file.write('%s\n' % line)
    return output_path
        
if __name__ == '__main__':
    output = main()
    print 'Holy Batman! I finished crunching it! :)'
    print 'Time to submit!'
    print 'Output file: ', abspath(output)
        