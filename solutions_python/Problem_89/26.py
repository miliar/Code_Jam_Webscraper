import sys
from math import log

def is_prime(i):
    if i <= 1: return False
    if i == 2 or i == 3 or i == 5: return True
    if i%2 == 0 or i%3 == 0 or i%5 == 0: return False
    if i < 49: return True
    s = int(i ** (0.5)) + 1
    for j in range(7, s, 2):
        if i % j == 0: return False
    return True

primes = [i for i in range(0, 1001) if is_prime(i)]

def expensive_dinner(n):
    if n <= 1: return '0'
    mx = 1 + sum(int(log(n, p)) for p in primes if p <= n)
    mn = len([1 for p in primes if p <= n])
    return str(mx - mn)

def main(filename):
    Input = open(filename, 'r').read().split('\n')
    Output = ""
    for i in range(1, int(Input[0]) + 1):
        n = int(Input[i])
        result = expensive_dinner(n)
        Output += "Case #" + str(i) + ": " + result + "\n"
    open(filename[:-3] + ".out", 'w').write(Output)

if __name__ == "__main__": main(sys.argv[1])
