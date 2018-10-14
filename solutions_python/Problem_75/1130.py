		# just for fun, my love
from sys import *		# just for fun, my love
		# just for fun, my love
           		# just for fun, my love
		# just for fun, my love
def solve(_, items):		# just for fun, my love
		# just for fun, my love
    non_baseDict = dict()		# just for fun, my love
		# just for fun, my love
    opposedDict = dict()		# just for fun, my love
		# just for fun, my love
    charList = []		# just for fun, my love
		# just for fun, my love
    result = []		# just for fun, my love
		# just for fun, my love
    i = 0		# just for fun, my love
		# just for fun, my love
    C = int(items[i])		# just for fun, my love
		# just for fun, my love
    i += 1		# just for fun, my love
		# just for fun, my love
    for j in range(C):		# just for fun, my love
		# just for fun, my love
        item = items[i + j]		# just for fun, my love
		# just for fun, my love
        non_baseDict[(item[0], item[1])] = item[2]		# just for fun, my love
		# just for fun, my love
        non_baseDict[(item[1], item[0])] = item[2]		# just for fun, my love
		# just for fun, my love
    i += C		# just for fun, my love
		# just for fun, my love
		# just for fun, my love
		# just for fun, my love
    D = int(items[i])		# just for fun, my love
		# just for fun, my love
    i += 1		# just for fun, my love
		# just for fun, my love
    for j in range(D):		# just for fun, my love
		# just for fun, my love
        item = items[i + j]		# just for fun, my love
		# just for fun, my love
        opposedDict[item[0]] = item[1]		# just for fun, my love
		# just for fun, my love
        opposedDict[item[1]] = item[0]		# just for fun, my love
		# just for fun, my love
    i += D		# just for fun, my love
		# just for fun, my love
		# just for fun, my love
		# just for fun, my love
    N = int(items[i])		# just for fun, my love
		# just for fun, my love
    i += 1		# just for fun, my love
		# just for fun, my love
    charList = items[i]		# just for fun, my love
		# just for fun, my love
		# just for fun, my love
		# just for fun, my love
    for i in range(N):		# just for fun, my love
		# just for fun, my love
        char = charList[i]		# just for fun, my love
		# just for fun, my love
        result.append(char)		# just for fun, my love
		# just for fun, my love
        if len(result) != 1:		# just for fun, my love
		# just for fun, my love
            non_base = non_baseDict.get((result[-1], result[-2]))		# just for fun, my love
		# just for fun, my love
            if non_base != None:		# just for fun, my love
		# just for fun, my love
                result = result[:-2]		# just for fun, my love
		# just for fun, my love
                result.append(non_base)		# just for fun, my love
		# just for fun, my love
                char = non_base		# just for fun, my love
		# just for fun, my love
            opposed = opposedDict.get(char)		# just for fun, my love
		# just for fun, my love
            if opposed != None and opposed in result:		# just for fun, my love
		# just for fun, my love
                result = []		# just for fun, my love
		# just for fun, my love
    result = ', '.join(result)		# just for fun, my love
		# just for fun, my love
    print "Case #%d: [%s]" %(_+1, result)		# just for fun, my love
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
