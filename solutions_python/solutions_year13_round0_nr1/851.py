'''
Created on Apr 12, 2013

@author: uglytroll
'''

def check_valid(a):
    for b in a:
        result = check_row(b)
        if result:
            return result
    for row in xrange(4):
        b = []
        for col in xrange(4):
            b.append(a[col][row])
        result = check_row(b)
        if result:
            return result
    b = [a[0][0], a[1][1], a[2][2], a[3][3]]
    result = check_row(b)
    if result:
        return result
    b = [a[0][3], a[1][2], a[2][1], a[3][0]]
    result = check_row(b)
    if result:
        return result
    if has_dot(a):
        return IN_COMP
    else:
        return DRAW
        
def check_row(b):
    x_count = 0
    o_count = 0
    t_count = 0
    for x in b:
        if x == 'T':
            t_count += 1
        elif x == 'X':
            x_count += 1
        elif x == 'O':
            o_count += 1
    if x_count + t_count == 4:
        return X_WIN
    elif o_count + t_count == 4:
        return O_WIN

def has_dot(a):
    for b in a:
        for c in b:
            if c == '.':
                return True
            
f = open('/home/uglytroll/codejam/2013/qual/1a.in', 'r')
o = open('/home/uglytroll/codejam/2013/qual/1a.out', 'w')
DRAW = 'Draw'
O_WIN = 'O won'
X_WIN = 'X won'
IN_COMP = 'Game has not completed'

T = int(f.readline().strip())

for t in xrange(T):
    a = []
    for x in xrange(4):
        b = list(f.readline().strip())
        a.append(b)
    result = check_valid(a)
    s = "Case #%d: %s\n" % (t+1, result)
    f.readline()
    o.write(s)
    

            