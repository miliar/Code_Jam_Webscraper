import sys
import bisect as bi

forms = ['1a1', '2a2', '1a1a1', '1a2a1', '2a1a2', '1a1b1a1', '1a1b2b1a1', '1a1b1b1a1',
         '1a1b1c1b1a1', '1a1b1c1c1b1a1', '1a1b1c1d1c1b1a1', '1a1b1c1d1d1c1b1a1']
fair_square = set([1, 4, 9])

for form in forms:
    for a in range(50):
        for b in range(50 - a):
            for c in range(50 - a - b):
                for d in range(50 - a - b - c):
                    form = form.replace('a', '0' * a)
                    form = form.replace('b', '0' * b)
                    form = form.replace('c', '0' * c)
                    form = form.replace('d', '0' * d)
                    number = int(form)**2
                    if number <= 10**100:
                        fair_square.add(number)

fair_square = sorted(fair_square)

f = open(sys.argv[1])
T = int(f.readline())
for t in range(T):
    A, B = map(int, f.readline().split())
    i, j = bi.bisect_left(fair_square, A), bi.bisect_right(fair_square, B)
    print "Case #%d:" % (t + 1), j - i
