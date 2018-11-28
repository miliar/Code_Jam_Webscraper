def get_input():
    with open('C-small-attempt0.in') as f:
        return f.read()

def prepare_input(inp):
    lines = inp.splitlines()
    lines.pop(0)
    while lines:
        a, b = lines.pop(0), lines.pop(0)
        a = a.split()
        yield int(a[0]), int(a[1]), map(int, b.split())


def gooo(inp):
    for index, (rounds, k, groups) in enumerate(inp):
        benefit = 0
        for i in xrange(rounds):
            benefit += shift_until(groups, max_=k)
        print "Case #%d: %d" % (index+1, benefit)

def shift_until(array, max_):
    retval = 0
    to_append = []
    while True:
        ret = False
        try:
            x = array[0]
        except IndexError:
            ret = True
        retval += x
        if ret or retval > max_:
            # revert
            array.extend(to_append)
            return retval - x
        else:
            to_append.append(array.pop(0))

gooo(prepare_input(get_input()))
