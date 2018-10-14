from math import floor, ceil, sqrt

def is_palim(integer):
    s = str(integer)
    for i in xrange(len(s)/2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

def solve_0(small, large):
    return [(i, i*i) for i in xrange(small, large + 1) if is_palim(i) and is_palim(i*i)]

def solve(small, large):
    s = int(ceil(sqrt(small)))
    l = int(floor(sqrt(large)))
    return len(solve_0(s, l))

def main(f):
    T = int(f.readline().strip())
    for i in xrange(T):
        small, large = [int(j) for j in f.readline().strip().split()]
        print "Case #{0}: {1}".format(i+1, solve(small, large))


if __name__ == '__main__':
    with open("C-small-attempt0.in", 'r') as f:
        main(f)