__author__ = 'kenneth'


def magician():
    m = open('magician.txt')
    m_lines = m.readlines()[1:]
    qw = 1
    for q in [m_lines[x:x + 10] for x in xrange(0, len(m_lines), 10)]:
        w1 = int(q[0].strip()) - 1
        f_ = q[1:5][w1].split()
        w2 = int(q[5].strip()) - 1
        s_ = q[6:10][w2].split()
        answer = set(f_) & set(s_)
        if len(answer) == 1:
            print "Case #%d: %s" % (qw, list(answer)[0])
        elif len(answer) > 1:
            print "Case #%d: Bad Magician!" % qw
        elif len(answer) < 1:
            print "Case #%d: Volunteer cheated!" % qw
        qw += 1


if __name__ == '__main__':
    magician()