import math

f = open('small_d.in', 'r')
g = open('d_small_out.txt', 'w')

data = [line for line in f]
T = data.pop(0)

for case, d in enumerate(data):
    X, R, C = [int(i) for i in d.split()]
    response = ''
    P = R*C
    if X > 6:
        response = 'RICHARD'
    elif P % X:
        response = 'RICHARD'
    elif not all(map(lambda x: x >= math.floor(X/2.) + 1, [R, C])) and X > 2:
        response = 'RICHARD'
    else:
        response = 'GABRIEL'
    print X, R, C, 'Case #%d: %s' %(case + 1, response)
    g.write('Case #%d: %s\n' %(case + 1, response))

f.close()
g.close()
    
