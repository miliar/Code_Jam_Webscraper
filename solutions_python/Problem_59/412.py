# -*- coding: utf-8 -*-

class Chick:
    def __init__(self):
        self.x = 0
        self.v = 0
        
    def set_x(self, x):
        self.x = x

    def set_v(self, v):
        self.v = v

    def is_reachable(self, b, t):
        if (b - self.x)/self.v <= t:
            return True
        else:
            return False

if __name__=="__main__":
    import time
    start = time.time()
    
    LINE_NEW_Q = 0
    LINE_POS = 1
    LINE_VELOCITY = 2
    
    status = LINE_NEW_Q
    cnt = 1
    is_first = True
    N = 0
    B = 0
    T = 0
    chicks = []
    out = open('B-small-attempt0.out', 'w')
    for l in open('B-small-attempt0.in'):
        if is_first:
            is_first = False
            continue
        line = l.rstrip("\n")
        data = line.split(' ')
        if status == LINE_NEW_Q:
            if len(data) != 4:
                print '[Error]not enough NKBT'
            N = long(data[0])
            K = long(data[1])
            B = long(data[2])
            T = long(data[3])
            status = LINE_POS
        elif status == LINE_POS:
            if len(data) != N:
                print '[Error]not enough POS'
            for x in data:
                chick = Chick()
                chick.set_x(int(x))
                chicks.append(chick)
            status = LINE_VELOCITY
        elif status == LINE_VELOCITY:
            if len(data) != N:
                print '[Error]not enough V'
            reachable_cnt = 0
            reachable_idx = []
            for i, x in enumerate(data):
                chicks[i].set_v(int(x))
                if chicks[i].is_reachable(B, T):
                    reachable_cnt += 1
                    reachable_idx.append(i)
            if reachable_cnt < K:
                out.write('Case #%d: IMPOSSIBLE\n' % (cnt))
                cnt += 1
            else:
                swap_cnt = 0
                for i in reachable_idx:
                    for j in xrange(i, N):
                        if not j in reachable_idx:
                            swap_cnt += 1
                out.write('Case #%d: %s\n' % (cnt, swap_cnt))
                cnt += 1
            status = LINE_NEW_Q
            chicks = []
    out.close()

    end = time.time()
    print 'time = %f' % (end - start)
