def solve(n, k, pancakes):
    r = [p[0] for p in pancakes]
    h = [p[1] for p in pancakes]
    top =  [i ** 2 for i in r]
    side = [2 * a * b for (a, b) in zip(r, h)]
    p = sorted(zip(r, h, top, side), reverse = True)
    maxA = 0
    for i in range(n):
        a = p[i][2] + p[i][3] + sum([q[3] for q in sorted(p[i+1:], key = lambda x:x[3], reverse = True)][:k-1])
        maxA = max(maxA, a)
    return maxA

def main():
    pi = 3.14159265359

    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n, k = [int(c) for c in raw_input().split(" ")]
        pancakes = []
        for j in xrange(0, n):
            pancakes.append([int(c) for c in raw_input().split(" ")])
        sol = solve(n, k, pancakes)
        print "Case #{}: {:.9f}".format(i, sol * pi)


if __name__ == "__main__":
    main()


# max top[0] + side[0] + side[1:10]
