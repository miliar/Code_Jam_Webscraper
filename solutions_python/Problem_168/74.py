# from __future__ import division
from pprint import pprint
import time
inputfile = file("in", "rb")
outputfile = file("out", "wb")
out_s = "Case #%d: %s"
parse_line = lambda: [int(a) for a in inputfile.readline().split()]
rl = lambda: inputfile.readline().replace("\n","")
UP = '^'
DOWN = 'v'
RIGHT = '>'
LEFT = '<'
NOD = '.'
# def walk_ok(grid, y,x, R, C):
#     def ok(y,x): return 0 <= x < C and 0 <= y < R
#     walked = {}
#     d = NOD
#     # print 'ente'
#     while 1:
#         if (y,x) in walked:
#             return True # Loop
#         walked[(y,x)] = True
#         # print 'y,x,R,C', y, x, R, C
#         if grid[y][x] == NOD and d == NOD:
#             return True
#         d = grid[y][x] if grid[y][x] != NOD else d
#         if d == UP:
#             if not ok(y-1, x):
#                 return False
#             y -= 1
#             continue
#         if d == DOWN:
#             if not ok(y+1, x):
#                 return False
#             y += 1
#             continue
#         if d == RIGHT:
#             if not ok(y, x+1):
#                 return False
#             x += 1
#             continue
#         if d == LEFT:
#             if not ok(y, x-1):
#                 return False
#             x -= 1
#             continue

# def grid_ok(grid, R, C):
#     for x in xrange(C):
#         for y in xrange(R):
#             if grid[y][x] == NOD:
#                 continue
#             if not walk_ok(grid, y, x, R, C):
#                 return False
#     return True

# ways = [UP, DOWN, LEFT, RIGHT]
# def change_bt(grid, mint, R, C, changed):
#     if grid_ok(grid, R, C):
#         return changed
#     if mint >= R*C:
#         return 10**9
#     mincount = 10**9
#     for y in xrange(mint / C, R):
#         for x in xrange(mint % C, C):
#             if grid[y][x] == NOD:
#                 continue
#             oldway = grid[y][x]
#             for way in ways:
#                 if oldway == way:
#                     continue
#                 grid[y][x] = way
#                 mincount = min(mincount, change_bt(grid, y*C + x + 1, R, C, changed + 1))
#                 grid[y][x] = oldway
#     return mincount

ways = [UP, DOWN, LEFT, RIGHT]
def needs_change(grid, y, x, R, C):
    def ok(y,x): return 0 <= x < C and 0 <= y < R

    d = grid[y][x]
    if d == NOD:
        return 0
    oldy, oldx = y, x
    # try that direction
    def whatf(d):
        if d == UP:
            f = lambda y,x: (y-1, x)
        if d == DOWN:
            f = lambda y,x: (y+1, x)
        if d == RIGHT:
            f = lambda y,x: (y, x+1)
        if d == LEFT:
            f = lambda y,x: (y, x-1)
        return f

    f = whatf(d)
    while 1:
        newy, newx = f(y, x)
        if not ok(newy, newx):
            break
        if grid[newy][newx] == NOD:
            y, x = newy, newx
            continue
        return 0 # Got to a non NOD no need to change
    # If we're here need to change direction
    first_d = d
    for way in ways:
        if first_d == way:
            continue
        f = whatf(way)
        y, x = oldy, oldx
        while 1:
            newy, newx = f(y, x)
            if not ok(newy, newx):
                break
            if grid[newy][newx] == NOD:
                y, x = newy, newx
                continue
            # print 'changed y,x from to', y, x, d, way
            return 1 # Changed it
    return -1 # If we're here, impossible 



def do_case(ncase):
    R, C = parse_line()
    lines = []
    for i in xrange(R):
        lines.append(list(rl()))
        assert len(lines[-1]) == C

    count = 0
    for x in xrange(C):
        for y in xrange(R):
            imp = needs_change(lines, y, x, R, C)
            if imp == -1:
                print >>outputfile, out_s % (ncase, str('IMPOSSIBLE'))
                return
            count += imp
    
    print >>outputfile, out_s % (ncase, str(count))

start_time = time.time()
T = int(inputfile.readline())
for ncase in xrange(1,T+1):
    print "Doing case", ncase
    do_case(ncase)
    print "Done, time", time.time()-start_time
    