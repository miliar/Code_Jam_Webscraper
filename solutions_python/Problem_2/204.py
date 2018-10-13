import sys
from datetime import datetime, date, time, timedelta

def find_min_trains(turn, a2b, b2a):
    events = []
    for x in a2b:
        x[1] += turn
        events.extend(((x[0], 'a train departs from A'),
                      (x[1], 'a new train is available at B')))

    for x in b2a:
        x[1] += turn
        events.extend(((x[0], 'a train departs from B'),
                      (x[1], 'a new train is available at A')))

    events.sort()
    na, nb = (0, 0)
    a_need, b_need = (0, 0)
    for t in events:
        if t[1] == 'a train departs from A':
            if na <= 0:
                a_need += 1
            else:
                na -= 1
        elif t[1] == 'a train departs from B':
            if nb <= 0:
                b_need += 1
            else:
                nb -= 1
        elif t[1] == 'a new train is available at A':
            na += 1
        elif t[1] == 'a new train is available at B':
            nb += 1
    return (a_need, b_need)

def main(path):
    f = open(path)
    n_case = int(f.readline())

    for i in range(n_case):
        m = int(f.readline())
        turn = timedelta(minutes=m)

        na, nb = map(int, f.readline().split())
        t = date(2008, 7, 17)

        a2b = []
        for j in range(na):
            d, a = f.readline().split()
            a2b.append(map(lambda x:
                           datetime.combine(t, time(*map(int, x.split(':')))),
                           (d, a)))

        b2a = []
        for j in range(nb):
            d, a = f.readline().split()
            b2a.append(map(lambda x:
                           datetime.combine(t, time(*map(int, x.split(':')))),
                           (d, a)))

        a_need, b_need = find_min_trains(turn, a2b, b2a)
        print "Case #%d: %d %d" % (i + 1, a_need, b_need)

    f.close()


if __name__ == "__main__":
    main(sys.argv[1])

