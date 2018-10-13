import sys

DEBUG = True


def solver(n, x, file_sizes):
    file_sizes.sort()
    disc_count = 0
    while len(file_sizes) >= 2:
        if file_sizes[0] + file_sizes[-1] <= x:
            file_sizes = file_sizes[1:-1]
        else:
            file_sizes = file_sizes[:-1]
        disc_count += 1
    if len(file_sizes) == 1:
        disc_count += 1
    return disc_count


def ssi(s, func=int):
    """
    space separated integers
    """
    return map(func, s.strip('\n').split())


def rl():
    return sys.stdin.readline()


def debug(*args):
    if args[-1] is not False and DEBUG:
        msg = " ".join([str(m) for m in args])
        sys.stderr.write(msg + '\n')


def main():
    # open input file
    # input_file = open('infile.txt')

    cases = int(rl())
    output = []
    # loop through cases passing input to solver
    for c in xrange(cases):
        debug('Case #%d' % (c + 1))
        n, x = ssi(rl())
        file_sizes = ssi(rl())
        answer = solver(n, x, file_sizes)
        output.append('Case #%d: %s\n' % (c + 1, answer))
    # open output file
    output_file = sys.stdout
    # write ouput to file
    output_file.writelines(output)
    output_file.flush()


if __name__ == '__main__':
    main()
