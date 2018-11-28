###
 # Uian Sol Gorgonio <sol.uian@gmail.com>
 # Apr 12 2013
 # Google Code Jam 2013 - Qualification Round
 # Problem B 
 ##/

def read_lawn(rows, cols):
    lawn = []
    for i in xrange(rows):
        lawn.append(map(int, raw_input().split()))
    return lawn


def max_in_col(lawn, col):
    max_height = lawn[0][col]
    for i in xrange(len(lawn)):
        if (lawn[i][col] > max_height):
            max_height = lawn[i][col]
    return max_height


def resolve_rows(lawn):
    grass = []
    for i in xrange(rows):
        max_height = max(lawn[i])
        grass.append([max_height for j in xrange(cols)])

    return grass


def resolve_cols(lawn, grass):
    for j in xrange(cols):
        max_height = max_in_col(lawn, j)
        for i in xrange(rows):
            if (grass[i][j] > max_height):
                grass[i][j] = max_height

    return grass


def resolve(lawn):
    grass = resolve_rows(lawn)
    grass = resolve_cols(lawn, grass)
    
    return grass



# main
tc = int(raw_input())
for nTC in xrange(1, tc + 1):
    rows, cols = map(int, raw_input().split())
    lawn = read_lawn(rows, cols)

    grass = resolve(lawn)

    if grass == lawn: print "Case #%d: YES" % nTC
    else: print "Case #%d: NO" % nTC
