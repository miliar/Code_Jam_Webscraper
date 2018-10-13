if __name__ == '__main__':
    for caseno in xrange(int(raw_input())):
        row0 = int(raw_input())
        poss0 = set([raw_input().split(' ') for _ in xrange(4)][row0 - 1])

        row1 = int(raw_input())
        poss1 = set([raw_input().split(' ') for _ in xrange(4)][row1 - 1])

        sols = poss0.intersection(poss1)

        if not sols:
            sol = "Volunteer cheated!"
        elif len(sols) > 1:
            sol = "Bad magician!"
        else:
            sol = sols.pop()

        print 'Case #%d: %s' % (caseno + 1, sol)
