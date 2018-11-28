# -*- coding: utf-8 -*-
__author__ = 'mac'


def read_case():
    data = {}
    choose = int(raw_input())
    arrange = []
    for j in range(0, 4):
        row = []
        raw_row = raw_input().strip().split()
        for r in raw_row:
            row.append(int(r))
        arrange.append(row)
    data['choose'] = choose
    data['arrange'] = arrange
    return data

def solve():
    case_num = int(raw_input())

    for i in range(1, case_num + 1):
        #read case one
        data = read_case()
        one_row = data['arrange'][data['choose'] - 1]

        data2 = read_case()
        two_row = data2['arrange'][data2['choose'] - 1]
        num = None

        for d in one_row:
            for t in two_row:
                if d == t:
                    if num is None:
                        num = []
                    num.append(d)
                    break
            if num is not None and len(num) > 1:
                break
        if num is None:
            print "Case #%d: %s" % (i, "Volunteer cheated!")
        elif len(num) > 1:
            print "Case #%d: %s" % (i, "Bad magician!")
        else:
            print "Case #%d: %d" % (i, num[0])






if __name__ == "__main__":
    solve()
