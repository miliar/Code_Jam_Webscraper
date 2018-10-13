class AllDone: pass

import sys
sys.setrecursionlimit(10000)

class Map:
    def __init__(self,w,h,data):
        self.h = h
        self.w = w
        self.data = data
        self.m = 97
        
    def __str__(self):
        s = ''
        for l in self.data:
            for e in l:
                if e['m'] != '':
                    s = s + e['m'] + ' '
                else:
                    s = s + str(e['v']) + ' '
            s = s.strip() + '\n'
        return s.strip()
                    
        
    def find_free(self):
        for (i,l) in enumerate(self.data):
            for (j,e) in enumerate(l):
                if e['m'] == '':
                    return j,i
        raise AllDone()
    
    def find_flow(self,x,y):
        flow = self.data[y][x]
        x1, y1 = x, y
        fl = False
        if y < self.h-1:
            if self.data[y+1][x]['v'] < flow['v']:
                flow = self.data[y+1][x]
                y1 = y+1
                fl = True
        if x < self.w-1:
            if (self.data[y][x+1]['v'] < flow['v']) or ((self.data[y][x+1]['v'] == flow['v']) and fl):
                flow = self.data[y][x+1]
                y1 = y
                x1 = x + 1
                fl = True
        if x > 0:
            if (self.data[y][x-1]['v'] < flow['v']) or ((self.data[y][x-1]['v'] == flow['v']) and fl):
                flow = self.data[y][x-1]
                y1 = y
                x1 = x - 1
                fl = True
        if y > 0:
            if (self.data[y-1][x]['v'] < flow['v']) or ((self.data[y-1][x]['v'] == flow['v']) and fl):
                flow = self.data[y-1][x]
                x1 = x
                y1 = y - 1
                
        return flow, x1, y1

    def mark(self):
        try:
            x, y = self.find_free()
            bank = [self.data[y][x]]
   #         print x,y
   #         print self
            while 1:
    #            raw_input()
                flow, x1, y1 = self.find_flow(x,y)
    #            print flow, x1, y1
                bank.append(flow) 
                fl = flow['m'] != ''
                if (flow == self.data[y][x]) or fl:
                    if fl: 
                        m = flow['m']
                    else:
                        m = chr(self.m)
                        self.m += 1
                        
                    for node in bank:
                        node['m'] = m
                    
                    self.mark()
                    break
                else:
                    x, y = x1, y1
                
        except AllDone:
            return
  


with open("B-large.in") as f:
    n = int(f.readline())
    maps = []
    for i in range(n):
        h, w = [int(e) for e in f.readline().split(" ")]
        maps.append(Map(w,h,[[{'v':int(e),'m':''} for e in f.readline().split(" ")] for z in range(h)]))
        

out = open("out-large.txt", "w")
for (i,m) in enumerate(maps):
    m.mark()
    print >> out, "Case #%d:" % (i+1)
    print >> out, m
    
