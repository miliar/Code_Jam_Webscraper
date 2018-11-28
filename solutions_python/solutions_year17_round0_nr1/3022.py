def check(clatite):
    for t in clatite:
        if t == '-':
            return False
    return True

def flip(array, start, end):

    while start < end:
        if array[start] == '-':
            array[start] = '+'
        else:
            array[start] = '-'
        start += 1
    return array


def intoarceClatita(clatite, intorcator):
    clatiteArray = [t for t in clatite]
    current = 0
    flips = 0
    while current <= len(clatiteArray) - int(intorcator):
        if clatiteArray[current] == '-':
            flips += 1
            clatiteArray = flip(clatiteArray, current, current + int(intorcator))
        current += 1
    if check(clatiteArray):
        return flips
    else:
        return 'IMPOSSIBLE'

def solve(fname):
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    content = content[1:]

    index = 0

    for t in content:
        index += 1
        clatiteArray = t.split()
        rezultat = intoarceClatita(clatiteArray[0], int(clatiteArray[1]))
        print "Case #%d: %s"%(index, rezultat)


solve("sample.txt")
