import math
import fractions

def int_input():
    return int(raw_input())

def list_int_input():
    return map(int, raw_input().split())

def list_char_input():
    return list(raw_input())

def table_int_input(h):
    return [list_int_input() for i in range(h)]

def table_char_input(h):
    return [list_char_input() for i in range(h)]

def is_prime(n):
    global primes
    limit = math.sqrt(n)
    for prime in primes:
        if n % prime == 0:
            return False
        elif prime >= limit:
            return True
    return True

def lcm(a, b):
    return a * b / fractions.gcd(a, b)

def get_primes(l):
    global primes
    for n in range(3, l+1):
        if is_prime(n):
            primes.append(n)

def get_min_calls(n):
    return max(1, len([i for i in primes if i <= n]))

def get_max_calls(n):
    calls = 1
    current_lcm = 1
    for i in range(1, n+1):
        new_lcm = lcm(current_lcm, i)
        if current_lcm != new_lcm:
            calls += 1
            current_lcm = new_lcm
    return calls

def solve(case):
    n = int_input()
    min_calls = get_min_calls(n)
    max_calls = get_max_calls(n)
    print 'Case #%d: %d' % (case, max_calls - min_calls)

def main():
    for i in range(int_input()):
        solve(i+1)

primes = [2]
get_primes(1000)
main()

