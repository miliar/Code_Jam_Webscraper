#!/usr/bin/env python
import sys
import itertools as it
#hsh = {}
def solveCase(line):
    (R, C, M) = map(int, line.split())
    #print "R = {}, C = {}, M = {}".format(R, C, M)
    board = [['.' for c in range(C)] for r in range(R)]
    assert len(board) == R and len(board[0]) == C
    dR = [-1, 1, -1,  0,  1, -1, 0, 1]
    dC = [ 0, 0, -1, -1, -1,  1, 1, 1] 
    def serialize_board():
        fstr = ""
        for r in range(R):
            fstr += "\n" + "".join(board[r])
        return fstr

    def cell(r, c):
        cnt = 0
        if board[r][c] == '*':
            return -1
        for i in range(len(dR)):
            if ((r + dR[i]) >= 0 and (c + dC[i]) >= 0 and (r + dR[i]) < R and (c + dC[i]) < C and board[r+dR[i]][c+dC[i]] == '*'):
                cnt = cnt+1
        return cnt

    def isValidBoard():
        #print "R = {}, C = {}, M = {}".format(R, C, M)
        fstr = ""
        for r in range(R):
            fstr += "\n" + "".join(board[r])
         
        #print "board = {}".format(fstr)
        
        valB = [[cell(r,c) for c in range(C)] for r in range(R)]
        seen = [[0 for c in range(C)] for r in range(R)]
        #print "valB = {} seen = {}, board={}".format(valB, seen,board)
        zv = (-1,-1)
        nz = [(-1, -1), 0]
        for r in range(R):
            if zv[0] != -1: break
            for c in range(C):
                if valB[r][c] == 0:
                    zv = (r,c)
                    break
                else:
                    if valB[r][c] != -1:
                        nz[1] += 1
                        nz[0] = (r,c)
        if zv[0] == -1 and nz[1] == 1:
            return (True, nz[0])

        if zv[0] == -1:
            return (False, zv)
        #print "zv = {}".format(zv)
        queue = [zv]
        while len(queue) > 0:
            cl = queue.pop(0)
            #print "cl = {}".format(cl)
            r = cl[0]
            c = cl[1]
            seen[r][c] = 1
            assert valB[r][c] != -1
            if valB[r][c] != 0:
                seen[r][c] = 2
                continue
            for i in range(len(dR)):
                #print "\ncell  =( {}, {}) seen = {} .. valB = {}".format(r+dR[i], c+dC[i], seen, valB)
                if ((r + dR[i]) >= 0 and (c + dC[i]) >= 0 and (r + dR[i]) < R and (c + dC[i]) < C and valB[r+dR[i]][c+dC[i]] != -1 and seen[r+dR[i]][c+dC[i]] == 0):
                    queue += [(r+dR[i], c+dC[i])]
            seen[r][c] = 2
            #print "queue = {}".format(queue) 
        valid = True
        for r in range(R):
            for c in range(C):
                if valB[r][c] >= 0 and seen[r][c] != 2:
                    valid = False
                    break
            if not valid:
                break
        #if valid:
            #print "seen = {}, valB = {}, val = {}, zv = {}, board = {}".format(seen, valB, valid, zv, serialize_board())
        return (valid, zv)

    for cmb in it.combinations(range(0,R*C), M):
        cmb = set(cmb)
        board = [['*' if r*C + c in cmb else '.' for c in range(C)] for r in range(R)]
        (val, cl) = isValidBoard()
        if val:
            board[cl[0]][cl[1]] = 'c'
            return serialize_board()

    return "\nImpossible"
#
#        assert m>=0
#        if m == 0:
#            sb = serialize_board()
#            if sb in hsh:
#                return hsh[sb] == 1
#            (isVal, zv) = isValidBoard()
#            if not isVal:
#                hsh[sb] = 0
#                return False
#            else:
#                board[zv[0]][zv[1]] = 'c'
#                hsh[sb] = 1
#                return True
#
#        for r in xrange(R):
#            for c in xrange(C):
#                #print "r,c = {},{}".format(r,c)
#                if board[r][c] == '.':
#                    board[r][c] = '*'
#                    sb = serialize_board()
#                    #print "\nboard = {}".format(sb)
#                    if sb not in hsh:
#                        hsh[sb] = 2
#                        if doIt(m-1):
#                            return True
#                        hsh[sb] = 0
#
#                    board[r][c] = '.'
#        return False
#
#    return (serialize_board() if doIt(M) else "\nImpossible")

lines = [line.strip() for line in sys.stdin]
T = int(lines.pop(0))
assert len(lines) == T
for i in range(0, T):
    print "Case #{}:{}".format(i+1, solveCase(lines.pop(0)))
