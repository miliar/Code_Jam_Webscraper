__author__ = 'Javier'


def main():
    lines = tuple(open('B-small-0.in', 'r'))
    num_inputs = int(lines[0])

    f = open('B.out', 'w')

    for k in xrange(num_inputs):
        values = map(int, lines[1 + k].split())
        A, B, K = values[0], values[1], values[2]

        count = 0
        for i in xrange(A):
            for j in xrange(B):
                if i&j < K:
                    count +=1

        print >> f, 'Case #%d: %d' % (k + 1, count)


if __name__ == "__main__":
    main()