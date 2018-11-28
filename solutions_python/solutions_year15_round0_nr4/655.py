__author__ = 'Christian'

def analyze(X, R, C):
    if X >= 7:
        return 'RICHARD'

    m = min(R,C)

    if (m >=2 and m*2 <= X) or (m == 1 and X >= 3):
        return 'RICHARD'

    if R*C % X != 0:
        return 'RICHARD'

    return 'GABRIEL'





#fname = 'test_d.txt'
fname = 'D-small-attempt3.in'
#fname = 'D-large.in'

f = open(fname, 'r')
data = f.read().split('\n')
f.close()

res_file = open(fname + '.res', 'w')

N = int(data[0])
data = data[1:]

for i in range(N):
    X, R, C = data[i].split(' ')[:3]
    res = analyze(int(X), int(R), int(C))
    print >> res_file, 'Case #%s: %s' % (i+1, res)

res_file.close()


