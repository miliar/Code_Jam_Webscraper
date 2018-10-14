import sys
import math

f = open(sys.argv[1], 'r')
o = open(sys.argv[1]+'_output', 'w')

T = int(f.readline())

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def num_fairsquare(A, B):
    min_sqrt, max_sqrt = int(math.ceil(math.sqrt(A))), int(math.sqrt(B))
    counter = 0
    for i in xrange(min_sqrt, max_sqrt+1):
        if is_palindrome(i) and is_palindrome(i**2): counter +=1
    return counter

to_write = ''
for i in range(T):
    A, B = f.readline().split()
    to_write += 'Case #'+str(i+1)+': '+str(num_fairsquare(int(A), int(B)))
    if i<T-1: to_write += '\n'

o.write(to_write)