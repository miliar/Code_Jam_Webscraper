#r = open('c:\\python27\\codejam\\Inputs.txt')
r = open('c:\\python27\\codejam\\A-small-attempt0.in')
cases = int(r.readline())

def solve(row1, row2):
    matches = 0
    for n in row1:
        if n in row2:
            x = n
            matches = matches + 1
    if matches == 0:
        return "Volunteer cheated!"
    if matches == 1:
        return str(x)
    if matches > 1:
        return "Bad magician!"

with open('c:\\python27\\codejam\\outputs.out', 'w') as w:
    for case in range(1, cases+1):
        first = int(r.readline())
        for n in range(4):
            x = r.readline().split()
            if n+1 == first:
                row1 = x
        second = int(r.readline())
        for n in range(4):
            x = r.readline().split()
            if n+1 == second:
                row2 = x
        w.write('Case #{0}: {1}\n'.format(str(case), solve(row1, row2)))
r.close()
