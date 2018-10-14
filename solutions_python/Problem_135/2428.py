infile = "A-small-attempt0.in.txt"
outfile = "A-small-attempt0.out"
cases = []


def process(c):
    s = set(set(c[0]) & set(c[1]))
    if  len(s) == 1:
        return list(s)[0]
    if  len(s) > 1:
        return 'Bad magician!'
    return 'Volunteer cheated!'


def parse(lines):
    ''' take one or more lines and parse to a specific case'''
    k = 1
    while k < len(lines):
        case = []
        g1 = int(lines[k].split()[0])
        g2 = int(lines[k + 5].split()[0])
        case.append(map(int, lines[k + g1].split()))
        case.append(map(int, lines[k + 5 + g2].split()))
        cases.append(case)
        k += 1 + 9


fin = open(infile, "r")
parse(fin.readlines())
fin.close()

fout = open(outfile, "w")

for i, c in enumerate(cases):
    fout.write('Case #{0}: {1}\n'.format(i + 1, process(c)))
    print 'Case #{0}: {1}'.format(i + 1, process(c))
fout.close()
