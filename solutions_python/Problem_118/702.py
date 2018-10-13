import sys
import math

def is_palindrome(n):
    s = str(n)
    return (s == s[::-1])

def all_palindromes(l):
    # all palindromes of length l
    assert l > 0
    if l == 1:
        for n in range(1,10):
            yield long(n)
    else:
        root_len = l/2
        root_low = int('1'+'0'*(root_len-1))
        root_high = int('9'*root_len)
        for i in range(root_low, root_high+1):
            root = str(i)
            if l%2 == 0:
                yield long(root + root[::-1])
            else:
                for j in range(0,10):
                    yield long(root + str(j) + root[::-1])

def palindromes_between(a, b):
    # print "palindromes_between({},{})".format(a,b)
    for i in range(len(str(a)),len(str(b))+1):
        # print "doing palindromes of len {}".format(i)
        for n in all_palindromes(i):
            # print n
            if n < a:
                # print "   too small"
                continue
            if n > b:
                # print "   too large"
                break
            # print "   good"
            yield n

def solve(a, b):
    res = 0
    low = long(math.ceil(math.sqrt(a)))
    high = long(math.floor(math.sqrt(b)))
    for i in palindromes_between(low, high):
        if is_palindrome(i*i):
             res += 1
    return res

if len(sys.argv) != 2:
    print "usage: main.py <input_file>"
    exit(1)

f = open(sys.argv[1])
if not f:
    print "usage: main.py <input_file>"
    exit(1)

for i,line in enumerate(f):
    if i == 0:
        continue
    A,B = map(long, line.split())
    print 'Case #{}: {}'.format(i, solve(A,B))

