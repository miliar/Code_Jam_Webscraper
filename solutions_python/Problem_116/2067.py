#!/usr/bin/python
import sys

game_result = ["O won", "X won", "Game has not completed", "Draw"]

def solve(m):
    # Check 1
    for c in m:
        if c.count('O') + c.count('T') == 4:
            return 0
        if c.count('X') + c.count('T') == 4:
            return 1
    # Check 2
    for i in xrange(4):
        s = ""
        for j in xrange(4):
            s = s + m[j][i]
        if s.count('O') + s.count('T') == 4:
            return 0
        if s.count('X') + s.count('T') == 4:
            return 1

    # Check 3
    s = ""
    for i in xrange(4):
        s = s + m[i][i]
    if s.count('O') + s.count('T') == 4:
        return 0
    if s.count('X') + s.count('T') == 4:
        return 1

    # Check 4
    s = ""
    for i in xrange(4):
        s = s + m[i][3-i]
    if s.count('O') + s.count('T') == 4:
        return 0
    if s.count('X') + s.count('T') == 4:
        return 1

    # Check Draw    
    for c in m:
        for cc in c:
            if cc == '.':
                return 2
    return 3

def main(argv):
    if len(argv) != 2:
        print "Usage:", argv[0], "<input file>"
        return

    f = open(argv[1], "r")  
    cc = int(f.readline())  
    for c in xrange(cc):  
        m = []
        for i in xrange(4):
            m.append(list(f.readline()[:-1]))
        ret = solve(m)
        print "Case #%d: %s" % (c+1, game_result[ret])  
        f.readline()
    f.close()

if __name__ == "__main__":
    main(sys.argv)
