lines = [line.strip() for line in open('A-large.in')]
m = int(lines[0])
out = ''


def checkline(number, old, current):
    stop = False
    if current == 'T' or current == old:
        number += 1
    if old == '' and current != 'T' and current != '.':
        old = current
        number += 1

    return number, old, stop


for case in xrange(1, 5 * m, 5):
    dd_old = ''
    dd_number = 0
    db_old = ''
    db_number = 0

    done = True
    winner = False

    dv_number = [0, 0, 0, 0]
    dv_old = ['', '', '', '']

    for i in xrange(4):

        # check row
        dh_old = ''
        dh_number = 0
        for idx, pos in enumerate(lines[case + i]):
            dh_number, dh_old, dh_break = checkline(dh_number, dh_old, lines[case + i][idx])

            if dh_break or dh_number == 4:
                break

            if pos == '.':
                done = False

        #check diagonals
        dd_number, dd_old, dd_break = checkline(dd_number, dd_old, lines[case + i][i])
        db_number, db_old, db_break = checkline(db_number, db_old, lines[case + i][3 - i])

        #verticals
        for j in xrange(4):
            dv_number[j], dv_old[j], tmp = checkline(dv_number[j], dv_old[j], lines[case + i][j])

        if dh_number == 4:
            out += "Case #%d: %s won\n" % (case / 5 + 1, dh_old)
            winner = True
            break

        if dd_number == 4:
            out += "Case #%d: %s won\n" % (case / 5 + 1, dd_old)
            winner = True
            break


        if db_number == 4:
            out += "Case #%d: %s won\n" % (case / 5 + 1, db_old)
            winner = True
            break

        if 4 in dv_number:
            out += "Case #%d: %s won\n" % (case / 5 + 1, dv_old[dv_number.index(4)])
            winner = True
            break


    if not winner:
        if done:
            out += "Case #%d: Draw\n" % (case / 5 + 1)
        else:
            out += "Case #%d: Game has not completed\n" % (case / 5 + 1)

with open('output.txt', 'w') as fd:
    fd.write(out[:-1])