import sys
import time
import re
import psyco
psyco.full()
def dbg(a): sys.stderr.write(str(a) + "\n")
def readint(): return int(raw_input())
def readfloat(): return float(raw_input())
def readarray(f): return map(f,raw_input().split())
def alloc(size, default = 0): return [default] * size
def dig(c): return ord(c) - 48

t00 = time.clock()


def search(col,X,Y,N,K,board):
    flg = {'R':1, 'B':2}

    flg2 = [0,0,0,0]
    for i in xrange(1,K):
        for j in xrange(1,K):
            if not i == j: continue
            if X+i >= N or Y+j >= N or \
               not board[X+i][Y+j] == col:
                flg2[0] = 1
            if X-i < 0 or Y+j >= N or \
               not board[X-i][Y+j] == col:
                flg2[1] = 1
            if X-i < 0 or Y-j < 0 or \
               not board[X-i][Y-j] == col:
                flg2[2] = 1
            if X+i >= N or Y-j < 0 or \
               not board[X+i][Y-j] == col:
                flg2[3] = 1

    dbg("%s %d %d %s" %(col,X,Y,str(flg2)))
    for f in flg2:
        if f == 0:
            return flg[col]
    return 0
        
def solve(N,K,board):
    flg = 0 # 0:n 1:r 2:bl 3:both

    for i in xrange(N):
        s = ""
        t = ""
        for j in xrange(N):
            t += board[j][i]
            s += board[i][j]
        dbg(s)
        if re.search("R"*K,t): flg |= 1
        if re.search("B"*K,t): flg |= 2
        if re.search("R"*K,s): flg |= 1
        if re.search("B"*K,s): flg |= 2
        dbg(flg)

    for x in xrange(N):
        if flg == 3: break
        for y in xrange(N):
            if flg == 3: break
            c = board[x][y]
            if c == '.': continue
            elif c == 'R':
                flg |= search('R',x,y,N,K,board)
            elif c == 'B':
                flg |= search('B',x,y,N,K,board)
            else:
                raise ValueError(c)

    if flg == 0:
        return "Neither"
    elif flg == 1:
        return "Red"
    elif flg == 2:
        return "Blue"
    elif flg == 3:
        return "Both"
    else:
        raise ValueError(flg)
    
    raise ValueError("something wrong")
    return None

    

for t in range(readint()):
    t0 = time.clock()
    dbg("Test #%d:" % (t+1))
    N,K = readarray(int)
    board = []
    for n in xrange(N):
        s = raw_input()
        s1 = ""
        s2 = ""
        for c in s:
            if c == '.':
                s1 += c
            else:
                s2 += c
        board.append(list(s1+s2)[:])

    for i in board:
        dbg(i)
    ans = solve(N,K,board)
    print "Case #%d: %s" % (t+1,ans)
    dbg("time %.2f sec" % (time.clock() - t0))

dbg("total time %.2f sec" % (time.clock() - t00))
