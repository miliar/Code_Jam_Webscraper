#!/usr/bin/env python
import sys
import multiprocessing
import itertools

log = sys.stderr

def doit(line):
    n = [int(i) for i in line.split()]
    n = n[1:n[0]+1]
    log.write("Case: {0}\n".format(n))

    for c in sorted([c for c in itertools.combinations(range(1, len(n)), 2)], key = lambda x: sum(x)):
        log.write("Sizes: {0}\n".format(c))

        for e1 in itertools.combinations(n, c[0]):
            sum_e1 = sum(e1)
            for e2 in itertools.combinations(n, c[1]):
                sum_e2 = sum(e2)
                if sum_e1 == sum_e2 and e1 != e2:
                    return (e1, e2)


    return ()

def main():
    input = sys.stdin
    output = sys.stdout

    worker = multiprocessing.Pool(multiprocessing.cpu_count())

    count = int(input.readline().strip())

    for caseno, result in enumerate(worker.map(doit,[line.strip() for line in input][:count])):
        output.write("Case #{0}:\n".format(caseno + 1))
        if len(result) > 0:
            for rl in result:
                output.write("{0}\n".format(" ".join([str(i) for i in rl])))
        else:
            output.write("Impossible\n")


if __name__ == '__main__':
    main()
