string = [s.strip() for s in
          open('input1.txt').readlines()[1:] if len(s.strip())]


def get_chunk():
    for index, line in enumerate(string):
        r, t = line.split(' ')
        yield [int(r), int(t)]


def calc_area(i, r):
    return i * 2 * r + (4 + (i - 1) * 2) / 2 * i

MAX = 100000
def solve_small(r, t):
    total = 0
    j = 0
    start_radius = r + 1
    for i in xrange(r + 1, MAX):
        j += 1
        area = start_radius * start_radius - (start_radius - 1)*(start_radius - 1)
        start_radius += 2
        total += area
        if total == t:
            return j
        if total > t:
            return j - 1



def solve(chunk):
    r, t = chunk
    return solve_small(r, t)

for index, chunk in enumerate(get_chunk()):
    print 'Case #%s:' % (index + 1), solve(chunk)
    # break
