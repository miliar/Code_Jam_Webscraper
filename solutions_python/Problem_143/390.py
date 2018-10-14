import sys, itertools

def test(a, b, k):
    anums, bnums, knums = list(range(0, a)), list(range(0, b)), set(range(0, k))
    abprod = itertools.product(anums, bnums)

    wins = 0

    for x, y in abprod:
        res = x&y
        if res in knums:
            wins += 1

    return wins

with open(sys.argv[-1], 'r') as infile:
    numcases = int(infile.readline())

    for x in range(0, numcases):
        testin = infile.readline()
        a, b, k = testin.split(' ')
        a, b, k = int(a), int(b), int(k)
        
        result = test(a, b, k)

        print "Case #{x}: {result}".format(x=x+1,result = result)
