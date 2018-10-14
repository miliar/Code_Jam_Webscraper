def solve(m1, m2, a1, a2):
    m1 = m(m1)
    m2 = m(m2)
    first = m1[a1-1]
    second =m2[a2-1]
    answer = set(first) & set(second)
    if len(answer) == 1:
        return answer.pop()
    elif len(answer) == 0:
        return 'Volunteer cheated!'
    else:
        return 'Bad magician!'

m1 = '''1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16'''
m2 = '''1 2 5 4
3 11 6 15
9 10 7 12
13 14 8 16'''
a1 = 2
a2 = 3

def m(s):
    l = iter(map(int, s.split()))
    return [[l.next() for i in range(4)] for i in range(4)]


def p(fn):
    f = open(fn)
    T = int(f.next())
    for i in range(T):
        a1 = int(f.next())
        m1 = ''
        for j in range(4):
            m1 += f.next()
        a2 = int(f.next())
        m2 = ''
        for j in range(4):
            m2 += f.next()
        print 'Case #{}: {}'.format(i+1, solve(m1, m2, a1, a2))

if __name__ == '__main__':
    p('A-small-attempt0.in')



