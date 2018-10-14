import string

def create_mapping():
    res = {}
    al = list(string.ascii_lowercase)
    res = dict(zip(al, [None for x in al]))

    def add(i, o):
        res[i] = o
        try:
            al.remove(o)
        except ValueError:
            pass

    with file('sample-input') as inp, file('sample-output') as out:
        inp.readline()
        for i in inp:
            o = out.readline()[9:]
            for n in xrange(len(i) - 1):
                add(i[n], o[n])

    add('a', 'y')
    add('z', 'q')
    add('q', 'z')
    return res

def main():
    m = create_mapping()
    tc = int(raw_input())
    for i in xrange(tc):
        print('Case #{}: {}'.format(i+1, ''.join(map(lambda l: m[l],
            raw_input()))))

if __name__ == '__main__':
    main()
