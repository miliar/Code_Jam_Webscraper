#!/usr/bin/env python
import sys

def main():
    i = sys.stdin
    o = sys.stdout

    count = int(i.readline().strip())

    caseno = 1
    for line in i:
        if caseno > count:
            break

        ls = line.split()
        a = int(ls[0])
        b = int(ls[1])

        results = []

        digits = len(str(a))
        if digits > 1:
            for x in range(a,b):
                xs = str(x)
                if xs[0] == '0' or len(xs) != digits:
                    continue

                for c in range(len(xs)):
                    xs = xs[-1] + xs[0:-1]
                    if xs[0] == '0' or len(xs) != digits:
                        continue

                    test = int(xs)
                    if test > x and test <= b:
                        results.append((x,test))


        #make distinct
        results = list(set(results))

        o.write("Case #{0}: {1}\n".format(caseno, len(results)))
        caseno = caseno + 1


if __name__ == '__main__':
    main()