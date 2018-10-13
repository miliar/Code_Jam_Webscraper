#!/usr/bin/env python
import sys

fin = open(sys.argv[1], 'r')
fout = open(sys.argv[2], 'w')

lines = fin.readlines()
lines.append('')
index = int(lines.pop(0).rstrip())

for n in range(index):
    lists = []
    #read data - read 4 lines
    lists.append(lines.pop(0).rstrip())
    lists.append(lines.pop(0).rstrip())
    lists.append(lines.pop(0).rstrip())
    lists.append(lines.pop(0).rstrip())

	#look for possible win
    finish = True
    winner = False
    for i in range(4):
        x = []
        y = []
        da = []
        db = []
        for j in range(4):
            x.append(lists[i][j])
            y.append(lists[j][i])
            da.append(lists[j][j])
            db.append(lists[j][-(j+1)])
        # print 'x : ' + x
        # print 'y : ' + y
        # print 'da : ' + da
        # print 'db : ' + db
        if (x.count('.') or y.count('.') > 0):
            finish = False
        if (x.count('X') + x.count('T') == 4 or y.count('X') + y.count('T') == 4 or da.count('X') + da.count('T') == 4 or db.count('X') + db.count('T') == 4):
            fout.write('Case #' + str(n+1) + ': X won')
            winner = True
            break
        if (x.count('O') + x.count('T') == 4 or y.count('O') + y.count('T') == 4 or da.count('O') + da.count('T') == 4 or db.count('O') + db.count('T') == 4):
            fout.write('Case #' + str(n+1) + ': O won')
            winner = True
            break
	    
	#if no empty block -> draw
    if (winner == False):
        if (finish == True):
            fout.write('Case #' + str(n+1) + ': Draw')
        else:
            fout.write('Case #' + str(n+1) + ': Game has not completed')
	
    fout.write('\n')
    lines.pop(0) #skip empty line

fout.close()