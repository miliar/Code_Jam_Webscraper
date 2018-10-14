'''
Created on 8 apr 2017

@author: algestam
'''

def all_ok(plates):
    for c in plates:
        if c == '-':
            return False
    return True

def solve(plates, size):
    plates = list(plates)
    flips = 0
    if all_ok(plates):
        return 0
    max_flips = 1 + (len(plates) - size)
    for i in range(max_flips):
        if plates[i] == '-':
            flips +=1
            for f in range(size):
                if plates[i+f] == '-':
                    plates[i+f] = '+'
                else:
                    plates[i+f] = '-'
    if all_ok(plates):
        return flips
    else:
        return -1

for case in xrange(input()):
    plates, size = raw_input().split()
    size = int(size)
    
    res = solve(plates, size)
    
    if res == -1:
        res = "IMPOSSIBLE"

    print "Case #%i: %s" % (case+1, res)