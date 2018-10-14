import sys
f = sys.stdin
T = int(f.readline().strip())
for i in range(1,T+1):
    tab = []
    a = int(f.readline().strip())
    for j in range(4):
        tab.append(f.readline().strip().split(' '))
    b = int(f.readline().strip())
    for j in range(4):
        tab.append(f.readline().strip().split(' '))
    res = set(tab[a-1]) & set(tab[4+b-1])
    r = ''
    if len(res) == 0:
        r = 'Volunteer cheated!'
    if len(res) == 1:
        r = list(res)[0]
    if len(res) > 1:
        r = 'Bad magician!'
    sys.stdout.write('Case #%d: %s\n' % (i, r))