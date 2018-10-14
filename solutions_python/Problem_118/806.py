import sys
from math import sqrt, floor

def is_palindrome(line):
    for i in range(0, len(line)/2):
        if line[i] != line[-i-1]:
            return False
    return True

def count_palindromes(A, B):
    res = 0
    for N in range(int(floor(sqrt(A))), int(floor(sqrt(B)))+1):
        NN = N * N
        if is_palindrome(str(N)) and is_palindrome(str(NN)) and NN >= A and NN <= B:
            res = res + 1
    return res

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for case in range(1,T+1):
        (A, B) = map(int, f.readline().split(' '))
        print 'Case #%i: %i' % (case, count_palindromes(A, B))
