import time

INPUT_FILE = __file__.replace('.py', '.input')
OUTPUT_FILE = __file__.replace('.py', '.output')


def solve(ps, u):
    ps = sorted(ps)
    n = len(ps)

    # Distribute u, try to bring each of the ps up to the max p. If you run out of u, distribute between the lowest ps.
    if u > 0:

        for i in xrange(1, n):

            d = ps[i] - ps[0]

            # If you run out of u, distribute amongst lowest ps
            if i*d > u:
                for j in xrange(i):
                    ps[j] += u/i
                u = 0
                break

            # Otherwise, bring the first i guys up to ps[i]
            else:
                for j in xrange(i):
                    ps[j] += d
                u -= i*d

    # Split the remainder up between all of them
    d = u/n
    ps = [p + d for p in ps]

    return reduce(lambda x, y: x*y, ps, 1.0)


def main():

    with open(INPUT_FILE, 'r') as f, open(OUTPUT_FILE, 'w') as h:
        t = int(f.readline().strip())
        for i in xrange(1, t+1):
            n, k = map(int, f.readline().strip().split())
            u = float(f.readline().strip())
            ps = map(float, f.readline().strip().split())
            soln = solve(ps, u)
            outline = 'Case #{i}: {soln}\n'.format(**locals())
            h.write(outline)
            print outline,


if __name__ == '__main__':
    main()
