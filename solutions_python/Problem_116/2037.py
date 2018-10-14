import sys
fname = sys.argv[1]

with open(fname) as fp:
    contents = [line for line in fp]

mag = int(contents[0])
contents = contents[1:]
lim = 4 # board size
inds = range(lim)

def solve(p, case):

    def checkwin(r):
        if '.' in r:
            return False
        if 'T' in r:
            r.remove('T')
        syms = len(r)
        if syms==1:
            s = r.pop()
            print "Case #%s: %s won" % ( case, s )
            return True
        return False


    # rows and cols
    for j in inds:
        if checkwin(set([p[j][k] for k in inds])):
            return
        if checkwin(set([p[k][j] for k in inds])):
            return
    if checkwin(set([p[j][j] for j in inds])):
        return
    if checkwin(set([p[j][lim-j-1] for j in inds])):
        return
    p = "".join(["".join(l) for l in p])
    if '.' in p:
        print "Case #%s: Game has not completed" % case
        return
    print "Case #%s: Draw" % case

for case in range(1,mag+1):
    p = [[c for c in line.strip()] for line in contents[:lim]]
    solve(p, case)

    contents = contents[lim+1:]
