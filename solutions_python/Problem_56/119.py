# -*- coding: utf-8 -*-

from numpy import array, size

STATUS_EMPTY = 0
STATUS_RED = 1
STATUS_BLUE = 2
class Board:
    def __init__(self, w, h, k):
        self.w = w
        self.h = h
        self.k = k
        self.status = array([STATUS_EMPTY]*self.w*self.h)
        
    def get_status(self, s):
        if s == '.':
            return STATUS_EMPTY
        elif s == 'R':
            return STATUS_RED
        elif s == 'B':
            return STATUS_BLUE
            
    def get_status_str(self, i):
        if i == STATUS_EMPTY:
            return '.'
        elif i == STATUS_RED:
            return 'R'
        elif i == STATUS_BLUE:
            return 'B'

    def set_row(self, s, row_cnt):
        for i, x in enumerate(s):
            self.status[row_cnt*self.w+i] = self.get_status(x)
        
    def print_status(self, target):
        s = ''
        for i in xrange(self.h):
            for j in xrange(self.w):
                s += self.get_status_str(target[i*self.w+j])
            s += '\n'
        print s
        
    def rotate(self):
        self.rotated = array([STATUS_EMPTY]*self.w*self.h)
        for i in xrange(self.h):
            for j in xrange(self.w):
                self.rotated[j*self.w+(self.w-i-1)] = self.status[i*self.w+j]
        #self.print_status(self.rotated)
        for i in xrange(self.w):
            g_s = 0
            g_e = 0
            in_empty = False
            is_end = False
            j = self.h-1
            while(j >= 0):
                if self.rotated[j*self.w+i] == STATUS_EMPTY:
                    if not in_empty:
                        g_s = j
                        in_empty = True
                    j -= 1
                else:
                    if in_empty:
                        g_e = j
                        in_empty = False
                        for k in reversed(xrange(0, g_e+1)):
                            self.rotated[(k+g_s-g_e)*self.w+i] = self.rotated[k*self.w+i]
                            self.rotated[k*self.w+i] = STATUS_EMPTY
                        #self.print_status(self.rotated)
                        j = self.h-1
                    else:
                        j -= 1
                            
        #self.print_status(self.rotated)
        
    def check_winner(self):
        is_blue_winner = False
        is_red_winner = False
        
        for i in xrange(self.h):
            for j in xrange(self.w):
                cur = self.rotated[i*self.w+j]
                if cur == STATUS_EMPTY:
                    continue
                elif cur == STATUS_BLUE and is_blue_winner:
                    continue
                elif cur == STATUS_RED and is_red_winner:
                    continue
                
                # 右
                if j+self.k <= self.w:
                    is_found = True
                    for x in xrange(self.k):
                        if self.rotated[i*self.w+(j+x)] != cur:
                            is_found = False
                            break
                    if is_found:
                        if cur == STATUS_BLUE:
                            is_blue_winner = True
                        elif cur == STATUS_RED:
                            is_red_winner = True

                # 左
                if j-self.k >= 0:
                    is_found = True
                    for x in xrange(self.k):
                        if self.rotated[i*self.w+(j-x)] != cur:
                            is_found = False
                            break
                    if is_found:
                        if cur == STATUS_BLUE:
                            is_blue_winner = True
                        elif cur == STATUS_RED:
                            is_red_winner = True

                # 上
                if i+self.k <= self.h:
                    is_found = True
                    for x in xrange(self.k):
                        if self.rotated[(i+x)*self.w+j] != cur:
                            is_found = False
                            break
                    if is_found:
                        if cur == STATUS_BLUE:
                            is_blue_winner = True
                        elif cur == STATUS_RED:
                            is_red_winner = True
                            
                # 下
                if i-self.k >= 0:
                    is_found = True
                    for x in xrange(self.k):
                        if self.rotated[(i-x)*self.w+j] != cur:
                            is_found = False
                            break
                    if is_found:
                        if cur == STATUS_BLUE:
                            is_blue_winner = True
                        elif cur == STATUS_RED:
                            is_red_winner = True

                # 右上
                if j+self.k <= self.w and i+self.k <= self.h:
                    is_found = True
                    for x in xrange(self.k):
                        if self.rotated[(i+x)*self.w+(j+x)] != cur:
                            is_found = False
                            break
                    if is_found:
                        if cur == STATUS_BLUE:
                            is_blue_winner = True
                        elif cur == STATUS_RED:
                            is_red_winner = True
                            
                # 右下
                if j+self.k <= self.w and i-self.k >= 0:
                    is_found = True
                    for x in xrange(self.k):
                        if self.rotated[(i-x)*self.w+(j+x)] != cur:
                            is_found = False
                            break
                    if is_found:
                        if cur == STATUS_BLUE:
                            is_blue_winner = True
                        elif cur == STATUS_RED:
                            is_red_winner = True

                # 左上
                if j-self.k >= 0 and i+self.k <= self.h:
                    is_found = True
                    for x in xrange(self.k):
                        if self.rotated[(i+x)*self.w+(j-x)] != cur:
                            is_found = False
                            break
                    if is_found:
                        if cur == STATUS_BLUE:
                            is_blue_winner = True
                        elif cur == STATUS_RED:
                            is_red_winner = True
                            
                # 左下
                if j-self.k >= 0 and i-self.k >= 0:
                    is_found = True
                    for x in xrange(self.k):
                        if self.rotated[(i-x)*self.w+(j-x)] != cur:
                            is_found = False
                            break
                    if is_found:
                        if cur == STATUS_BLUE:
                            is_blue_winner = True
                        elif cur == STATUS_RED:
                            is_red_winner = True

        if is_blue_winner and is_red_winner:
            return 'Both'
        elif is_blue_winner:
            return 'Blue'
        elif is_red_winner:
            return 'Red'
        else:
            return 'Neither'
                
        
if __name__=="__main__":
    import time
    start = time.time()
    
    board = None
    cnt = 1
    is_first = True
    row_cnt = 0
    out = open('A-large.out', 'w')
    for l in open('A-large.in'):
        if is_first:
            is_first = False
            continue
        line = l.rstrip("\n")
        data = line.split(' ')
        if len(data) == 2:
            board = Board(int(data[0]), int(data[0]), int(data[1]))
            row_cnt = 0
        else:
            if len(line) != board.w:
                print 'ERROR %s' % len(l)
                continue
            board.set_row(line, row_cnt)
            row_cnt += 1
            if row_cnt == board.h:
                board.rotate()
                #board.print_status(board.rotated)
                #print board.check_winner()
            
                out.write('Case #%d: %s\n' % (cnt, board.check_winner()))
                cnt += 1
    out.close()

    end = time.time()
    print 'time = %f' % (end - start)
