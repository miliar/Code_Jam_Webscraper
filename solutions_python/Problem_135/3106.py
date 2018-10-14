
def solvegame(lines):
    ind1 = int(lines[0])
    ind2 = int(lines[5])
    row1 = lines[ind1].split()
    row2 = lines[ind2+5].split()
    if len(set(row1 + row2)) == 8:
        return 'Volunteer cheated!'
    elif len(set(row1 + row2)) < 7:
        return 'Bad magician!'
    else:
        return set(row1).intersection(set(row2)).pop()


f = file('a.in', 'r')
lines = f.readlines()
cases = int(lines[0])

g = file('a.out', 'w')
g.writelines(['Case #{}: {}\n'.format(i+1, solvegame(lines[10*i+1:10*i + 11])) for i in xrange(cases)])
