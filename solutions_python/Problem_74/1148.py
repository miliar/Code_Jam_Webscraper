		# just for fun, my love
from sys import *		# just for fun, my love
		# just for fun, my love
           		# just for fun, my love
		# just for fun, my love
def getNextItem(items, i, X):		# just for fun, my love
		# just for fun, my love
    for j in range(i, len(items)):		# just for fun, my love
		# just for fun, my love
        if items[j][0] == X:		# just for fun, my love
		# just for fun, my love
            return items[j]		# just for fun, my love
		# just for fun, my love
    return None		# just for fun, my love
		# just for fun, my love
def solve(_, items):		# just for fun, my love
		# just for fun, my love
    num = 0		# just for fun, my love
		# just for fun, my love
    c = int(items[0])		# just for fun, my love
		# just for fun, my love
    items = [[items[i], int(items[i+1])] for i in range(1, c * 2, 2)]		# just for fun, my love
		# just for fun, my love
    posO, posB = 1, 1		# just for fun, my love
		# just for fun, my love
    for i in range(len(items)):		# just for fun, my love
		# just for fun, my love
        #print posO, posB, num		# just for fun, my love
		# just for fun, my love
        X, pos = items[i]		# just for fun, my love
		# just for fun, my love
        if X == 'O':		# just for fun, my love
		# just for fun, my love
            inc = abs(pos - posO) + 1		# just for fun, my love
		# just for fun, my love
            num += inc		# just for fun, my love
		# just for fun, my love
            posO = pos		# just for fun, my love
		# just for fun, my love
            item = getNextItem(items, i, 'B')		# just for fun, my love
		# just for fun, my love
            if item != None:		# just for fun, my love
		# just for fun, my love
                X1, pos1 = item		# just for fun, my love
		# just for fun, my love
                if pos1 != posB:		# just for fun, my love
		# just for fun, my love
                    #inc = abs(pos - posO) + 2		# just for fun, my love
		# just for fun, my love
                    if pos1 > posB:		# just for fun, my love
		# just for fun, my love
                        right = True		# just for fun, my love
		# just for fun, my love
                    else:		# just for fun, my love
		# just for fun, my love
                        right = False		# just for fun, my love
		# just for fun, my love
                    if right:		# just for fun, my love
		# just for fun, my love
                        posB += inc		# just for fun, my love
		# just for fun, my love
                        if posB > pos1:		# just for fun, my love
		# just for fun, my love
                            posB = pos1		# just for fun, my love
		# just for fun, my love
                    else:		# just for fun, my love
		# just for fun, my love
                        posB -= inc		# just for fun, my love
		# just for fun, my love
                        if posB < pos1:		# just for fun, my love
		# just for fun, my love
                            posB = pos1		# just for fun, my love
		# just for fun, my love
        else:		# just for fun, my love
		# just for fun, my love
            inc = abs(pos - posB) + 1		# just for fun, my love
		# just for fun, my love
            num += inc		# just for fun, my love
		# just for fun, my love
            posB = pos		# just for fun, my love
		# just for fun, my love
            item = getNextItem(items, i, 'O')		# just for fun, my love
		# just for fun, my love
            if item != None:		# just for fun, my love
		# just for fun, my love
                X1, pos1 = item		# just for fun, my love
		# just for fun, my love
                if pos1 != posO:		# just for fun, my love
		# just for fun, my love
                    #inc = abs(pos - posB) + 2		# just for fun, my love
		# just for fun, my love
                    if pos1 > posO:		# just for fun, my love
		# just for fun, my love
                        right = True		# just for fun, my love
		# just for fun, my love
                    else:		# just for fun, my love
		# just for fun, my love
                        right = False		# just for fun, my love
		# just for fun, my love
                    if right:		# just for fun, my love
		# just for fun, my love
                        posO += inc		# just for fun, my love
		# just for fun, my love
                        if posO > pos1:		# just for fun, my love
		# just for fun, my love
                            posO = pos1		# just for fun, my love
		# just for fun, my love
                    else:		# just for fun, my love
		# just for fun, my love
                        posO -= inc		# just for fun, my love
		# just for fun, my love
                        if posO < pos1:		# just for fun, my love
		# just for fun, my love
                            posO = pos1		# just for fun, my love
		# just for fun, my love
                            		# just for fun, my love
		# just for fun, my love
    print "Case #%d: %d" %(_+1, num)		# just for fun, my love
		# just for fun, my love
    return		# just for fun, my love
		# just for fun, my love
    		# just for fun, my love
		# just for fun, my love
cases = int(raw_input())		# just for fun, my love
		# just for fun, my love
for _ in xrange(cases):		# just for fun, my love
		# just for fun, my love
    items = stdin.readline()[:-1].split(' ')		# just for fun, my love
		# just for fun, my love
    solve(_, items)		# just for fun, my love
