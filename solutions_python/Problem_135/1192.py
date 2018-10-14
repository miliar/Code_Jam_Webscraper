def run():
    T = int(raw_input())
    for i in xrange(T):
        A1 = int(raw_input())
        s1 = set([[int(x) for x in raw_input().split()] for j in xrange(4)][A1 - 1])
        A2 = int(raw_input())
        s2 = set([[int(x) for x in raw_input().split()] for j in xrange(4)][A2 - 1])
        s = s1.intersection(s2)
        if len(s) == 0:
            print 'Case #%d:' % (i + 1), 'Volunteer cheated!'
        elif len(s) == 1:
            print 'Case #%d:' % (i + 1), '%d' % list(s)[0]
        else:
            print 'Case #%d:' % (i + 1), 'Bad magician!'


if __name__ == '__main__':
    run()
