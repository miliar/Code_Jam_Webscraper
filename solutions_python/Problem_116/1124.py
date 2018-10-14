import fileinput

f = fileinput.input()
# f = fileinput.input('sample-input.txt')

T = int(f.readline())


def check(a,p):
    a = [[p if x=='T' else x for x in r] for r in a]
    t = list(map(list, zip(*a))) # transposed
    diag = lambda a,p: a[0][0] == a[1][1] == a[2][2] == a[3][3] == p or \
                       a[0][3] == a[1][2] == a[2][1] == a[3][0] == p
    line = lambda a,p: any(all(x==p for x in r) for r in a)
    return diag(a,p) or diag(t,p) or line(a,p) or line(t,p)

for line in f:
    ln = fileinput.lineno()-1
    n = round(ln / 5)
    i = ln % 5
    if i == 0: continue
    if i == 1: a = []
    r = [x for x in line.strip()]
    a.append(r)
    if i == 4:
        if   check(a, 'X'): s = 'X won'
        elif check(a, 'O'): s = 'O won'
        elif any('.' in r for r in a): s = 'Game has not completed'
        else: s = 'Draw'
        print("Case #%s: %s"%(n,s))
