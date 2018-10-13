import sys
from math import floor, log10, sqrt

def main():
    _, input_fn = sys.argv
    input = open(input_fn)
    T = int(input.readline())
    def rl():
        return input.readline().strip("\n")

    for t in range(T):
        A, B = (int(x) for x in rl().split())
        fs = fair_and_square(A, B)
        print "Case #%i: %i" % (t+1, fs)

palindromes_d = dict()
def palindromes(n):
    def generate(n):
        if n < 1:
            yield 0
        elif n == 1:
            for x in range(1,10):
                yield x
        else:
            for x in range(1,10):
                for p in palindromes(n-2):
                    yield x + x*10**(n-1) + p*10
    if n in palindromes_d:
        return palindromes_d[n]
    else:
        palindromes_d[n] = tuple(p for p in generate(n))
        return palindromes_d[n]

# we don't have to recognize palindromes larger than 10**14
# also, 0 is the only palindrome divisible by 10
def is_palindrome(n):
    if n < 10:
        return True
    if n < 10:
        return n/10 == n%10

    f, l = int(n/10**(floor(log10(n)))), n%10
    m = int((n % 10**(floor(log10(n))))/10)
    if f == l:
        return is_palindrome(m)
    else:
        return False

def fair_and_square(a, b):
    count = 0
    low = int(log10(a)/2)
    high = int(log10(b)/2)
    for n in range(low+1, high+2):
        for p in palindromes(n):
            if p*p > b:
                break
            if a <= p*p <= b and is_palindrome(p*p):
                count += 1
    return count

main()
