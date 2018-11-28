import sys
from numpy import *

def main():
    f = open('A-small-attempt1.in')
    e = enumerate(f)

    count = int(e.next()[1])

    for i in range(count):
        res = test_it(i,e)
        print "Case #%d: %s"%(i+1, res)

def digest(string):
    digested = string[0]
    last = string[0]

    for c in string:
        if last != c:
            last = c
            digested += c

    return digested

def count(string):
    counts = []

    last = string[0]
    cur = 0

    for c in string:
        if last == c:
            cur = cur + 1
        else:
            counts.append(cur)
            cur = 1
            last = c

    counts.append(cur)

    return counts

def get_best(cnts):
    best = None
    total = len(cnts)
    size = len(cnts[0])

    case = zeros(size,int)
    for cnt in cnts:
        case = case + array(cnt)

    for idx in range(size):
        case[idx] = int(case[idx] / total)


    move = 0

    for cur in cnts:
        b = array(cur)
        c = case -b

        for v in c:
            move = move + abs(v)

    if not best or best > move:
        best = move

    return best



def test_it(idx, e):
    cnt = int(e.next()[1])
    cnts = []

    id = None

    for i in range(cnt):
        string = e.next()[1].strip()
        cur_id = digest(string)

        if not id:
            id = cur_id
        elif cur_id != id:
            return 'Fegla Won'

        cnts.append(count(string))

    return get_best(cnts)

main()
