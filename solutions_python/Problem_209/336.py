import math

if __name__ == '__main__':
    t = int(raw_input())
    for t in xrange(1, t + 1):
        # print t
        n, k = map(int, raw_input().split(' '))

        dims = []
        for i in xrange(n):
            dims.append(map(float, raw_input().split(' ')))
        dims.sort(key=lambda x: x[0], reverse=True)
        # print dims

        sides = []
        for i in xrange(n):
            sides.append(2 * math.pi * dims[i][0] * dims[i][1])

        max_val = 0.0
        for i in xrange(n-k+1):
            surface = math.pi * dims[i][0] ** 2 + 2 * math.pi * dims[i][0] * dims[i][1]
            # now pick the k-1 pancakes with biggest sides
            sub_sides = sides[i+1:]
            # print "sub_sides", sub_sides
            sub_sides.sort(reverse=True)
            for j in xrange(k-1):
                surface += sub_sides[j]
            if surface > max_val:
                max_val = surface

        print "Case #%d: %.10f" % (t, max_val)
