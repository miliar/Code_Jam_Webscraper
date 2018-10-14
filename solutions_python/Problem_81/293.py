LOSS, WIN, NONE = "01."

from fractions import Fraction

def calculate_rpi(sched, n):
    games = [Fraction(0) for i in range(n)]
    wp = [Fraction(0) for i in range(n)]
    owp = [Fraction(0) for i in range(n)]
    oowp = [Fraction(0) for i in range(n)]
    for i, row in enumerate(sched):
        for j, col in enumerate(row):
            if col != NONE:
                games[i] += 1
                if col == WIN:
                    wp[i] += 1
        wp[i] /= games[i]
    for i in range(n):
        for j in range(n):
            if sched[j][i] == NONE:
                continue
            did_win = 1 if sched[j][i] == WIN else 0
            partial_wp = (games[j] * wp[j] - did_win) / (games[j] - 1)
            owp[i] += partial_wp
        owp[i] /= games[i]
    for i in range(n):
        for j in range(n):
            if sched[j][i] == NONE:
                continue
            oowp[i] += owp[j]
        oowp[i] /= games[i]

    return [float((wp[i]/4) + (owp[i]/2) + (oowp[i]/4))
            for i in range(n)]

            
if __name__ == '__main__':
    number_of_tests = int(raw_input())
    for t in range(1, number_of_tests+1):
        n = int(raw_input())
        sched = [raw_input().strip()
                 for i in range(n)]
        answers = calculate_rpi(sched, n)
        print 'Case #%d:' % t
        for rpi in answers:
            print '%f' % rpi
