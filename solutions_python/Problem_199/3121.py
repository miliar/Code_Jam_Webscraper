def flip(pan, loc, flipper):
    if loc + flipper > len(pan):
        return False

    for x in xrange(loc, loc+flipper):
        if pan[x] == '+':
            pan[x] = '-'
        else:
            pan[x] = '+'

    return True


def find_unhappy(pan):
    return pan.index('-')


def find_happy(pan):
    return pan.index('+')


def is_done(pan):
    return pan.count('+') == len(pan)


def solve(input, flipper):
    pan = list(input)
    orig_pan = list(input)

    i = 0
    while not is_done(pan):
        i+=1
        lindex = find_unhappy(pan)
        if flip(pan, lindex, flipper) is False:
            return "IMPOSSIBLE"

        if orig_pan == pan:
            return "IMPOSSIBLE"

    return i


def read_file():
    lines = [line.rstrip('\n') for line in open('C:\Users\Slava\input')]

    target = open('C:\Users\Slava\output', 'w')
    cases = lines[0]

    i = 1
    for x in lines[1:]:
        tokens = x.split(' ')
        pan = tokens[0]
        flipper = int(tokens[1])
        target.write("Case #{}: {}\n".format(i, solve(pan, flipper)))
        i += 1



read_file()