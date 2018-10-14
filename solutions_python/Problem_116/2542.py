import re

f = open('input.txt')

s = f.read().split('\n')
s.append('')

DOWN = r'(%s|T)....(%s|T)....(%s|T)....(%s|T)'
ACROSS = r'(%s|T)(%s|T)(%s|T)(%s|T)'
DIAGR = r'(%s|T).....(%s|T).....(%s|T).....(%s|T)'
DIAGL = r'(%s|T)...(%s|T)...(%s|T)...(%s|T)'

T = int(s[0])
rec = []

for x in range(0,T):
    grid = ';'.join([s[1 + 5*x], s[2 + 5*x], s[3 + 5*x], s[4 + 5*x]])
    player = ['X', 'O']
    win = '.'
    for p in player:    
        # across
        a = re.search(ACROSS % (p,p,p,p), grid)
        if a:
            win = p + ' won'
            break
        # down
        d = re.search(DOWN % (p,p,p,p), grid)
        if d:
            win = p + ' won'
            break
        # diag-r
        dr = re.search(DIAGR % (p,p,p,p), grid)
        if dr:
            win = p + ' won'
            break
        # diag-l
        dl = re.search(DIAGL % (p,p,p,p), grid)
        if dl:
            win = p + ' won'
            break
    if win == '.':
        if '.' in grid:
            win = 'Game has not completed'
        else:
            win = 'Draw'

    rec.append(win)
            
k = 1
o = open('output', 'w')
for r in rec:
    o.write('Case #%d: %s\n' % (k, r))
    k += 1

o.close()
