'''
Created on 07.05.2011

@author: shelajev
'''

def solve(l):
    l = map(lambda x: x - 1, l)
    n = len(l)
    sum = 0
    v = [False]*n
    for i in range(n):
        if v[i]: continue
        cur = i
        count = 1
        while l[cur] != i:
            v[l[cur]] = True
            count += 1
            cur = l[cur]
        if count != 1:
            sum += count
    return sum

if __name__ == '__main__':
    problem = 'D'
#    name = problem + '-sample'
#    name = problem + '-small-attempt%d' % 0
    name = problem + '-large'
    f = open(name + '.in', 'r')
    out = open(name + '.out', 'w')
    T = int(f.readline())
    for t in range(1, T+1):
        f.readline()
        values = map(int, f.readline().split())
        ans = solve(values)
        print('Case #%s: %s' % (t, ans))
        out.write('Case #%s: %s\n' % (t, ans))
    out.close()