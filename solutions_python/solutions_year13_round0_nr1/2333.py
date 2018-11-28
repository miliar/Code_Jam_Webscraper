from Queue import Queue
import sys

def _processQ(q, number):
    r1 = q[0:4]
    r2 = q[4:8]
    r3 = q[8:12]
    r4 = q[12:16]
    c1 = [ q[0], q[4], q[8], q[12] ]
    c2 = [ q[1], q[5], q[9], q[13] ]
    c3 = [ q[2], q[6], q[10], q[14] ]
    c4 = [ q[3], q[7], q[11], q[15] ]
    d1 = [ q[0], q[5], q[10], q[15] ]
    d2 = [ q[3], q[6], q[9], q[12] ]

    tot = [ r1, r2, r3, r4, c1, c2, c3, c4, d1, d2 ]
    dot_cnt = 0
    result = ""
    for char in ['X', 'O']:
        for lst in tot:
            if lst.count(char) == 3 and lst.count('T') == 1:
                result = "%s won"%char
                break
            elif lst.count(char) == 4:
                result = "%s won"%char
                break
            else:
                dot_cnt = dot_cnt + lst.count('.')
             
    if not result and dot_cnt == 0:
        result = "Draw"
    if not result and dot_cnt != 0:
        result = "Game has not completed"

    print "Case #%s: %s"%(number, result)


if __name__ == '__main__':
    try:
        num_of_input = int(raw_input())
    except:
        print "Enter valid input."
        sys.exit(1)
    cnt = 0
    Q = Queue()
    while cnt < num_of_input:
        size = 0
        temp = []
        while size < 16:
            a=sys.stdin.read(1)
            if a != "\n":
                temp.append(a.upper())
                size = size + 1
        Q.put( temp )
        cnt = cnt + 1
    number = 0
    while Q.qsize():
        q=Q.get()
        number = number + 1
        _processQ(q, number)

