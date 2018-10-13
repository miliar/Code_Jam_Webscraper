
import math

debug = 0

class C(object):
    def __init__(self):
        
        self.f,\
        self.R,\
        self.t,\
        self.r,\
        self.g = map(float,raw_input().split())
        
        self.RT = self.R-self.t-self.f
        self.R2 = self.R**2
        self.RT2 = self.RT**2
        
        
    def go(self):
        
        if self.g < 2*self.f:  return 1.0
        if self.f >=  self.RT: return 1.0
        
        
        total = (1.0/4.0) * math.pi * self.R2
        
        sum = 0
        full = 0
        
        off = self.r+(self.g/2.0)
        mul = self.g + 2*self.r
        
        
        d = self.g-2.0*self.f
        
        assert d < mul
        
        d2 = d**2
        w = d/2.0
        
        if debug:
            print
            print '#######################################################'
            print
            print 'f',self.f
            print 'R',self.R
            print 't',self.t
            print 'r',self.r
            print 'g',self.g
            print
            print 'RT',self.RT
            print 'RT2',self.RT2
            print 'w',w
            print 'd',d
            print 'off',off
            print 'mul',mul
            print
            
        
        
        for cx in     xrange(int((3+self.RT/mul))):
            for cy in xrange(int((3+self.RT/mul))):
                x = cx*mul+off
                y = cy*mul+off
                
                xs = x-w
                xe = x+w
                
                ys = y-w
                ye = y+w
                
                if debug: print 'xy',x,y
                
                if ((xs)**2 + (ys)**2) > self.RT2: continue
                if ((xe)**2 + (ye)**2) < self.RT2:
                    full += 1
                    continue
                
                if debug: print
                
                
                xs = x-w
                xe = x+w
                
                ys = y-w
                ye = y+w
                
                
                
                side1 = 0
                side2 = 0
                
                if (x+w)**2 + (y-w)**2 > self.RT2:  side1 = 1
                if (x-w)**2 + (y+w)**2 > self.RT2:  side2 = 1
                
                
                if side1 and side2:
                    
                    xmb = math.sqrt(self.RT2 - (ys)**2)
                    
                    area = self.chord(xs)
                    area-= (xmb-xs)*(ys)
                    assert abs((xmb**2 + ys**2)-self.RT2) < 0.001, (xmb**2 + ys**2)-self.RT2
                    assert area > 0, (self.chord(xs), (xmb-xs)*(ys))
                    area-= self.chord(xmb)
                    assert area > 0
                    assert area < d2
                    if debug:   print '11',area
                    sum += area
                    
                    continue
                    
                if (not side1) and (not side2):
                    xmt = math.sqrt(self.RT2 - (ye)**2)
                    assert xs < xmt < xe
                    area = self.chord(xmt)
                    area-= self.chord(xe)
                    assert area > 0, area
                    area-= (xe-xmt)*(ys)
                    assert area > 0, (self.chord(xmt), self.chord(xe), self.chord(xmt)-self.chord(xe), (xe-xmt)*(ye), area)
                    area+= (xmt-xs)*d
                    assert area > 0, area
                    #assert area <= d2, (area, d2)
                    if debug:   print '00',area
                    sum += area
                    
                    continue
                    
                if side1 and (not side2):
                    
                    xmt = math.sqrt(self.RT2 - (ye)**2)
                    xmb = math.sqrt(self.RT2 - (ys)**2)
                    assert xs < xmt < xmb < xe
                    area = self.chord(xmt)
                    area-= self.chord(xmb)
                    area-= (xmb-xmt)*(ys)
                    area+= (xmt-xs)*d
                    assert area > 0
                    assert area < d2
                    if debug:   print '10',area
                    sum += area
                    
                    continue
                    
                if side2 and (not side1):
                    
                    ymt = math.sqrt(self.RT2 - (xe)**2)
                    ymb = math.sqrt(self.RT2 - (xs)**2)
                    assert ys < ymt < ymb < ye
                    area = self.chord(ymt)
                    area-= self.chord(ymb)
                    area-= (ymb-ymt)*(xs)
                    area+= (ymt-ys)*d
                    assert area > 0
                    assert area < d2
                    if debug:   print '10',area
                    sum += area
                    
                    continue
        
        assert sum < total
        sum += full * d2
        assert sum < total, (sum,total)
        
        
        return 1.0-(sum/total)
    
    def chord(self, x):
        theta = math.acos(x/self.RT)*2.0
        
        r = ((self.RT2/2.0) * (theta-math.sin(theta)))/2.0
        
        assert r >= 0
        
        return r
        

if __name__ == '__main__':
    
    N = int(raw_input())
    for i in xrange(N):
        c = C()
        print 'Case #%d: %.6f' % (i+1, c.go())
        