import sys

def is_consonant(c):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    return c in consonants

def n_value(name, n):

    start_points = []
    for i in xrange(len(name) - n + 1):

        if (all(map(is_consonant, name[i: i+n]))):
            start_points.append(i)

    if not start_points:
        return 0

    num_substrings = 0
    for j, p in enumerate(start_points):
        if j > 0:
            last_point = start_points[j-1]
            num_substrings += (p - last_point) * (len(name) - (p + n - 1))
        else:
            num_substrings += (p + 1) * (len(name) - (p + n - 1))

    return num_substrings


if __name__ == '__main__':
    num_cases = int(sys.stdin.readline().strip())
    for c_n in xrange(num_cases):
        name, n = sys.stdin.readline().strip().split()
        n_val = n_value(name, int(n))
        print "Case #%d: %d" % (c_n+1, n_val)
