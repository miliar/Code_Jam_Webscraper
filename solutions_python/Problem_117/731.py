import sys

f = open(sys.argv[1], 'r')
o = open(sys.argv[1]+'_output', 'w')

T = int(f.readline())

# reads dimension and yard, returns matrix
def load_yard():
    N, M = f.readline().split()
    N, M = int(N), int(M)
    matrix = [[0 for i in xrange(M)] for i in xrange(N)]
    for i in xrange(N):
        l = f.readline().split()
        for j in xrange(M):
            matrix[i][j] = int(l[j])
    return matrix

# returns the minimum value in the yard
def min_num(yard): return reduce(min, map(lambda x: reduce(min, x), yard))

# returns tuple ('c',m) or ('r', m) for mth row or col as all being n
def row_all(yard, m):
    row_all_m = map(lambda z: reduce(lambda x,y: (y==m and x),z,True), yard)
    for i in xrange(len(row_all_m)):
        if row_all_m[i]: return ('r', i)
    transpose = \
        [[yard[i][j] for i in xrange(len(yard))] for j in xrange(len(yard[0]))]
    col_all_m = map(lambda z: reduce(lambda x,y: (y==m and x),z,True), transpose)
    for i in xrange(len(col_all_m)):
        if col_all_m[i]: return ('c', i)

# returns a new yard but with the mth row or col removed
def remove_line(yard, m, r_or_c):
    if r_or_c == 'r': return [yard[i] for i in xrange(len(yard)) if i!=m]
    return [[yard[i][j] for j in xrange(len(yard[0])) if j!=m]
        for i in xrange(len(yard))]

def is_yard_possible(yard):
    if len(yard) == 0: return True 
    shortest = row_all(yard, min_num(yard))
    if shortest is None: return False
    return is_yard_possible(remove_line(yard, shortest[1], shortest[0]))

yards = [load_yard() for i in xrange(T)]

to_write = ''
case = 1
for yard in yards:
    result = 'YES' if is_yard_possible(yard) else 'NO'
    to_write += 'Case #'+str(case)+': '+result
    case += 1
    if case<=T: to_write += '\n'

o.write(to_write)