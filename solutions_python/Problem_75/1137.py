import sys

def process(in_file):
    basic = tuple('QWERASDF')

    in_line = in_file.readline().strip().split(' ')

    r = int(in_line[0])
    rs = in_line[1:r+1]
    recipes = {}
    for i in rs:
        recipes[''.join(sorted(i[:2]))] = i[2]

    o = int(in_line[r+1])
    ops = in_line[r+2:r+o+2]
    oppose = {}
    for i in ops:
        if not hasattr(oppose, i[0]):
            oppose[i[0]] = []
        if not hasattr(oppose, i[1]):
            oppose[i[1]] = []
        oppose[i[0]].append(i[1])
        oppose[i[1]].append(i[0])

    #print recipes, oppose
    s = list(in_line[o+r+3])
    ls = []

    try:
        i = s.pop(0)
        while True:
            if len(ls) > 0:
                # Check recipes
                r = ''.join(sorted(i+ls[-1]))
                if recipes.has_key(r):
                    #print 'Recipe found %s -> %s' % (r, recipes[r])
                    ls.pop()
                    i = recipes[r]
                    continue

                if oppose.has_key(i):
                    #print 'Oppose found %s -> %s' % (i, oppose[i])
                    for j in oppose[i]:
                        if j in ls:
                            ls = []
                            i = s.pop(0)
                            continue
            ls.append(i)
            i = s.pop(0)

    except IndexError:
        pass


    del recipes
    del oppose
    del s
    
    #print ls
    return '[%s]' % (', '.join(ls))


def main():
    if len(sys.argv) is not 2:
        print 'Pass in_file'
        return 1

    in_file = open(sys.argv[1], 'r')

    iterations = int(in_file.readline())

    for i in range(iterations):
        sys.stdout.write('Case #%d: %s\n' % (i+1, process(in_file)))

    
    in_file.close()
    sys.stdout.flush()

    return 0

if __name__ == '__main__':
    sys.exit(main())

