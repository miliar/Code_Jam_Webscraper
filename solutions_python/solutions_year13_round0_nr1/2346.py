import sys

def chunks(l, n):
    return (l[i:i+n] for i in xrange(0, len(l), n))

def find_winner(l):
    first = l[0] if l[0] != 'T' else l[1]

    for x in l:
        if x == '.':
            return False
        if x != first and x != 'T':
            return False

    return first


if __name__ == '__main__':
    lines = [x.strip() for x in sys.stdin.readlines()]
    lines = [x for x in lines if x]

    for case_num, case in enumerate(chunks(lines[1:], 4)):
        diag = [case[i][i] for i in xrange(4)]
        reverse_diag = [case[4-1-i][i] for i in range(4-1,-1,-1)]

        winner = []

        #print ''.join(diag), find_winner(diag)
        #print ''.join(reverse_diag), find_winner(reverse_diag)

        winner.append(find_winner(diag))
        winner.append(find_winner(reverse_diag))

        # Row
        for row in case:
            #print row, find_winner(row)
            winner.append(find_winner(row))

        # Column
        for col in zip(*case):
            #print ''.join(col), find_winner(col)
            winner.append(find_winner(col))

        #print winner
        #print
        #print '\n'.join(case)

        result = [x for x in set(winner) if x]
        if len(result) == 1:
            print 'Case #%d: %s won' % (case_num + 1, result[0])
        elif len(result) > 1:
            print 'Case #%d: Draw' % (case_num + 1,)
        else:
            if ''.join(case).find('.') == -1:
                print 'Case #%d: Draw' % (case_num + 1,)
            else:
                print 'Case #%d: Game has not completed' % (case_num + 1,)
