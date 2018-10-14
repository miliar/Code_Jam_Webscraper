#!/usr/bin/python
import sys
import copy

#2009 GCJ qual B
##szfile = './B-test.in.txt'
##szfile_output = './B-test.output.txt'
##szfile = './B-small-attempt1.in'
##szfile_output = './B-small.output.txt'
szfile = './B-large.in'
szfile_output = './B-large.output.txt'

l_dx = [ 0, -1, 1, 0 ]
l_dy = [ -1, 0, 0, 1 ]

l_alpha = 'abcdefghijklmnopqrstuvwxyz'

class Price:
    def __init__(self):
        pass

    def RunFile(self) :
# using file set
        f = open(szfile,'rb')
        s = f.read()
# ---
        l_s = s.splitlines()

        ncase = int(l_s[0])
        l_s = l_s[1:]
##        print ncase
##        print l_s

        l_output = []
        for c in xrange(ncase):
            print c
            self.m_area = []
            str_r_h = l_s[0]
            l_s = l_s[1:]
            r = int(str_r_h.split()[0])
            h = int(str_r_h.split()[1])
##            print r, h
            m_eval = [ [0] * h for x in xrange(r) ]
            for i in xrange(r):
                str_line = l_s[0]
                l_s = l_s[1:]
                l_data = str_line.split()
                for j in xrange(h):
                    m_eval[i][j] = int(l_data[j])
##            print m_eval
            m_area = self.GetArea(m_eval, r, h)
            num = c+1
            l_output.append('Case #%(num)d:' %locals())
            for j in xrange(r):
                l_output.append(' '.join(m_area[j]))
##        print l_output

# using file set
        f = open(szfile_output,'wb')
        f.write('\n'.join(l_output))
# ----

    def GetArea(self, D, r, h):
        self.m_area = [ ['-'] * h for x in xrange(r) ]
        self.ll_data = [ [False] * 4 for x in xrange(r*h) ]
        for i in xrange(r):
            for j in xrange(h):
                ny = i; nx = j;
                nd = -1
                for k in xrange(4):
                    dy = i+l_dy[k]
                    dx = j+l_dx[k]
                    if(dx < 0 or dx >= h or dy < 0 or dy >= r): continue
                    if(D[ny][nx] > D[dy][dx]):
                        ny = dy; nx = dx;
                        nd = k;
                if(nd != -1):
                        self.ll_data[i*h+j][nd] = True
                        self.ll_data[ny*h+nx][3-nd] = True
##        print self.ll_data

        k = 0
        for i in xrange(r):
            for j in xrange(h):
                if(self.m_area[i][j] == '-'):
                    self.Draw(i, j, r, h, k)
                    k += 1
##        print self.m_area
        return self.m_area

    def Draw(self, y, x, r, h, k):
        self.m_area[y][x] = l_alpha[k]
        for i in xrange(4):
            dy = y+l_dy[i]
            dx = x+l_dx[i]
            if(dx < 0 or dx >= h or dy < 0 or dy >= r):
                continue
            if(self.m_area[dy][dx] == '-' and self.ll_data[y*h+x][i] == True):
                self.Draw(dy, dx, r, h, k)


if __name__ == "__main__":
    cm = Price()
    cm.RunFile()



