'''
Created on Apr 13, 2013

@author: jirasch
'''

def solve(c):
    not_finished = False
    for i in range(4):
        if c[i].replace('T', 'X') == 'XXXX':
            return 'X won'
        if c[i].replace('T', 'O') == 'OOOO':
            return 'O won'
        if '.' in c[i]:
            not_finished = True
    for i in range(4):
        d = ''.join([x[i] for x in c])
        if d.replace('T', 'X') == 'XXXX':
            return 'X won'
        if d.replace('T', 'O') == 'OOOO':
            return 'O won'
    d = ''.join([c[i][i] for i in range(4)])
    if d.replace('T', 'X') == 'XXXX':
            return 'X won'
    if d.replace('T', 'O') == 'OOOO':
        return 'O won'
    d = ''.join([c[3-i][i] for i in range(4)])
    if d.replace('T', 'X') == 'XXXX':
            return 'X won'
    if d.replace('T', 'O') == 'OOOO':
        return 'O won'
    
    if not_finished:
        return 'Game has not completed'
    else:
        return 'Draw'

afile = file('A-large.in')
lines = afile.read().splitlines()
afile.close()

num = int(lines[0].strip())
cases = [lines[(1+ (i*5)):(1+ (i*5))+4] for i in range(num)]

i = 1
for c in cases:
    print 'Case #%d: %s' % (i, solve(c))
    i += 1
