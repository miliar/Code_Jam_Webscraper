'''
Created on 07.05.2011

@author: shelajev
'''


def solve(values):
    impossible = reduce(lambda x, y: x ^ y, values)
    if impossible:
        return 'NO'
    return sum(values) - min(values)

if __name__ == '__main__':
#    name = 'C-sample'
#    name = 'C-small-attempt%d' % 0
    name = 'C-large (1)'
    f = open(name + '.in', 'r')
    out = open(name + '.out', 'w')
    T = int(f.readline())
    for t in range(1, T+1):
        f.readline()
        values = f.readline().split()
        ans = solve(map(int, values))
        print('Case #%s: %s' % (t, ans))
        out.write('Case #%s: %s\n' % (t, ans))
    out.close()