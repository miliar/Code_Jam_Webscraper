_case = 0
def gout(s):
    global _case
    _case += 1
    print "Case #%d: %s" % (_case,s) 

def memoize(f):
    dict = {}
    def func(*n):
        if n in dict:
            return dict[n]
        else:
            dict[n] = f(*n)
            return dict[n]
    return func

for _ in xrange(int(raw_input())):
    r,c = (int(x) for x in raw_input().split())
    tiles = []
    for _ in xrange(r):
        tiles.append(list(raw_input()))
    broken = False
    for i in xrange(r):
        for j in xrange(c):
            if tiles[i][j] == '#':
                if i < r-1 and j < c-1 and tiles[i+1][j] == '#' and tiles[i][j+1] == '#' and tiles[i+1][j+1] == '#':
                    tiles[i][j] = tiles[i+1][j+1] = '/'
                    tiles[i+1][j] = tiles[i][j+1] = '\\'
                else:
                    gout('\nImpossible')
                    broken = True
                    break
        if broken: break
    if not broken:
        gout('\n'+'\n'.join((''.join(row) for row in tiles)))
