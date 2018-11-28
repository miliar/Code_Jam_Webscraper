def le(first, second):
    return int(first) <= int(second)

def solve(numstring, builtstring, lowerbound):
    if len(numstring) == len(builtstring):
        return builtstring
    cmpstring = numstring[:len(builtstring) + 1]
    for i in xrange(9, lowerbound - 1, -1):
        if le(builtstring + str(i), cmpstring):
            #check if others work
            restans = solve(numstring, builtstring + str(i), i)
            if restans:
                return restans
    return False

numtests = input()
for i in xrange(1, numtests + 1):
    print "Case #%d:" % i, int(solve(raw_input(), "", 0))