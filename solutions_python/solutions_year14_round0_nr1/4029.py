'''

Google Code Jam 2014
Qualification Round
Problem A - Magic Trick

Notes:
  * Focus only on the rows picked, the rest can be discarded
  * basic procedure:
    if len(dissect(row1, row2)) == 1: display
    elif len(dissect(row1, row2)) > 1 "Bad magician!"
    elif len(dissect(row1, row2)) < 1 "Volunteer cheated!"

'''

from sys import stdin, stdout

def main(n):
    for case in xrange(1,n+1):
        result = get_next_result()
        stdout.write("Case #%s: %s\n" % (case, result))

def get_next_result():
    turn1, turn2 = [get_turn() for _ in xrange(2)]
    return get_output(turn1, turn2)

def get_output(t1, t2):
    o = t1 & t2

    if len(o) == 1:
        return str(next(iter(o)))
    elif len(o) > 1:
        return "Bad magician!"
    elif len(o) < 1:
        return "Volunteer cheated!"

def get_turn():
    row_num = int(stdin.readline())
    return get_row(row_num)

def get_row(row_num):
    rows = get_cards()
    return frozenset(rows[row_num-1])

def get_cards():
    return [stdin.readline().split() for _ in xrange(4)]

if __name__ == '__main__':
    main(int(stdin.readline()))
