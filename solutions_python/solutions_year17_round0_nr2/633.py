def is_sorted(l):
    return all(l[i] <= l[i+1] for i in xrange(len(l)-1))

def base_factors(n, base):
    l = []
    while n > 0:
        l.insert(0, n % base)
        n = n / base
    return l

def is_tidy(n):
    factors = base_factors(n, 10)
    return is_sorted(factors)


def solve(N):
    if is_tidy(N):
        return N
    small_N = N / 10
    small_sol = solve(small_N)
    if small_sol < small_N:
        return (small_sol*10) + 9
    small_sol = solve(small_N - 1)
    return (small_sol*10) + 9

def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        N = int(raw_input())
        sol = solve(N)
        print "Case #{}: {}".format(i, sol)
    

if __name__ == "__main__":
    main()
