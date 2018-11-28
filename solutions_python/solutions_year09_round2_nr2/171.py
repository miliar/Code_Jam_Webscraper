#!/usr/bin/python
from sys import stderr
from itertools import combinations, permutations

filenames=['B-test.in', 'B-small-attempt1.in', 'B-large.in']
f=open(filenames[1],'r')

T=int(f.readline())

def NPerms (seq):
    "computes the factorial of the length of "
    return reduce (lambda x, y: x * y, range (1, len (seq) + 1), 1)

def PermN (seq, index):
    "Returns the th permutation of  (in proper order)"
    seqc = list (seq [:])
    result = []
    fact = NPerms (seq)
    index %= fact
    while seqc:
        fact = fact / len (seqc)
        choice, index = index // fact, index % fact
        result += [seqc.pop (choice)]
    return result

for case in range(T):
	number=int(f.readline().rstrip())
	i=0
	while int(''.join(PermN(sorted('0'+str(number)), i))) <= number:
		i+=1

	answer=int(''.join(PermN(sorted('0'+str(number)), i))) 

	print 'Case #{0}: {1}'.format(case +1 ,answer )
