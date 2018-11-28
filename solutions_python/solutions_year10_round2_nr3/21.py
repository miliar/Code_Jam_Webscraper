from gmpy import comb, fac

MOD = 100003

# This works a little bit faster than dict based memoization :D
memoize = [[-1] * 1000 for i in range(1000)] 
memoize_comb = [[-1] * 1000 for i in range(1000)] 

def memoized_comb(x, n):
    if memoize_comb[x][n] == -1:
        memoize_comb[x][n] = comb(x, n) % MOD
    return memoize_comb[x][n]

def count(N, length):
    global memoize
    if length == 0:
        return 1
    if length == 1:
        return 1
    if memoize[N][length] != -1:
        return memoize[N][length]
    total = 0
    for start in range(length - 1):
        k = length - start - 2
        total += count(length, start + 1) * memoized_comb(N - length - 1, k)
        total = total % MOD
        
    memoize[N][length] = total
    return total

def solve(N):
    return sum([count(N, i) for i in range(1, N)]) % MOD
    
def main():
    file = open('C-large.in')
    output = open('output.txt', 'w')
    tests = int(file.readline().strip())
    for case in range(1, tests + 1):
        N = [int(x) for x in file.readline().split()][0]
        print >> output, 'Case #%d:' % case, solve(N)
    output.close()

if __name__ == '__main__':
    main()

    
