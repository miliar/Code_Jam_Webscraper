import sys

f = open("A.in").readlines()
sys.stdout = open("A.out", "w")
lines = (l for l in f)

tests = int(lines.next())

for test in xrange(1, tests + 1):
    print "Case #%d:" % test
    n = int(lines.next())
    rpi = [[0]*n for  i in xrange(n)]
    wins = [lines.next() for i in xrange(n)]
    wp = [[0]*n for i in xrange(n)]
    for i in xrange(n):
        played = 0
        won = 0
        for j in xrange(n):
            if wins[i][j] == '1':
                played += 1
                won +=1
            elif wins[i][j] == '0':
                played += 1
        for j in xrange(n):
            if wins[i][j] == '1':
                played -= 1
                won -= 1
                wp[i][j] = won/float(played)
                won += 1
                played += 1
            elif wins[i][j] == '0':
                played -= 1
                wp[i][j] = won/float(played)
                played += 1
    twp = [[0]*n for i in xrange(n)]
    owp = [0.5 for i in xrange(n)]
    oowp = [0.5 for i in xrange(n)]
    for it in xrange(100):
        for i in xrange(n):
            played = 0
            total_owp = 0
            for j in xrange(n):
                if wins[i][j] == '1' or wins[i][j] == '0':
                    played += 1
                    total_owp += wp[j][i]
            c_owp = total_owp/float(played)
            owp[i] = c_owp
        for i in xrange(n):
            played = 0
            total_oowp = 0
            for j in xrange(n):
                if wins[i][j] == '1' or wins[i][j] == '0':
                    played += 1
                    total_oowp += owp[j]
            c_oowp = total_oowp/float(played)
            oowp[i] = c_oowp
    actual_wp = [0 for i in xrange(n)]
    for i in xrange(n):
        played = 0
        won = 0
        for j in xrange(n):
            if wins[i][j] == '1':
                played += 1
                won +=1
            elif wins[i][j] == '0':
                played += 1
        actual_wp[i] = won/float(played)
    for i in xrange(n):
        print 0.25*actual_wp[i] + 0.50*owp[i] + 0.25*oowp[i]
                
    
    
