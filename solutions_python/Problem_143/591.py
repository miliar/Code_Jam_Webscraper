import sys

def solve(a,b,k):
    n = 0
    for i in range(a):
        for j in range(b):
            if i&j < k:
                n += 1
    return n

def solver(f):
    cases = int(f.readline().strip())
    for i in range(cases):
        (a,b,k) = [int(x) for x in f.readline().strip().split()]

        num_winners = solve(a,b,k)
        print num_winners

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        solver(f)

