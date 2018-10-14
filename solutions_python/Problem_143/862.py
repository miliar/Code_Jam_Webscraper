## Magician
o_all=all
import numpy as np
import sys

from numpy import sort

def ifile():
    filename = sys.argv[1]
    return open(filename, 'r').read()

def parse_cases(input, lines_per_case):
    lines = input.split('\n')
    numcases = lines[0]
    cases = []
    i = 1
    while i < (len(lines) - 1):
        c = lines[i:(i + lines_per_case)]
        cases.append(tuple(c))
        i += lines_per_case
    return cases
	
def get_num_cases(input):
    lines = input.split('\n')
    numcases = lines[0]
    return numcases

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

cases = parse_cases(ifile(), 1)
numcases = get_num_cases(ifile())

f = open('sln.txt','w')

print cases
print numcases

numcases=int(numcases)

for n in range(numcases):
    A,B,K=cases[n][0].split(" ")
    A=int(A); B=int(B); K=int(K)
    print A,B,K
    total=A*B
    for i in range(K,A):
        for j in range(K,B):
            btw_and=np.bitwise_and(i,j)
            if(n==1):
                    print i,j,btw_and
            if(btw_and >= K):
                if(n==1):
                    print i,j,btw_and,K
                total=total-1
    to_print= r"Case #" + str(n+1) + ": " + str(total) + "\n"
    f.write(to_print)
#bitwise_and
f.close() 
