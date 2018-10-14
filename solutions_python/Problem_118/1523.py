import sys
import itertools

def is_palindrome(n):
    s = str(n)
    
    return s[::-1] == s

def pseudo_palindrome_generator(n):
    if n < 4:
        start = int(10**(n - 1))
        stop = 10**(n)
        
        for n in xrange(start, stop):
            if is_palindrome(n):
                yield n
    else:
        for p in large_pseudo_palindrome_generator(n):
            yield p

def large_pseudo_palindrome_generator(n):
    digits = ['12'] + ['10' for i in xrange(n / 2 - 1)]
    chunks = itertools.product(*digits)
    
    if n % 2 == 0:
        for chunk in chunks:
            start = ''.join(chunk)
            
            yield int(start + start[::-1])
    else:
        for chunk in chunks:
            start = ''.join(chunk)
            end = start[::-1]
            
            for i in xrange(3):
                yield int(start + str(i) + end)

def num_palindromes(a, b):
    total = 0
    
    start = len(str(int(a**0.5)))
    stop = len(str(int(b**0.5)))
    
    for n in xrange(start, stop + 1):
        for p in pseudo_palindrome_generator(n):
            p2 = p**2
            
            if a <= p2 <= b and is_palindrome(p2):
                total += 1
    
    return total

if __name__ == '__main__':
    next(sys.stdin)
    
    for i, line in enumerate(sys.stdin, start=1):
        try:
            start, stop = map(int, line.split(' '))
        except ValueError:
            break
        
        print 'Case #{0}: {1}'.format(i, num_palindromes(start, stop))