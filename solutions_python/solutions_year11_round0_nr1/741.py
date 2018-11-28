# Google Code Jam 2011
# Ertug Karamatli
# karamatli.com

import sys

cases = []

f = file(sys.argv[1])
for i, line in enumerate(f):
    if i > 0:
        line_arr = line.split()[1:]
        case = []
        for j in range(0, len(line_arr), 2):
            case.append((line_arr[j], int(line_arr[j+1])))
        cases.append(case)

#print cases
#print

class TestCase(object):
    def __init__(self, case):
        self.case = case
        self.t = 1
        self.step = 0
        self.stepcnt = len(case)
        self.bpos = 1
        self.opos = 1
        
    def move_blue(self, target):
        if target > self.bpos:
            self.bpos += 1
            #print 'bpos+1'
            return False
        elif target < self.bpos:
            self.bpos -= 1
            #print 'bpos-1'
            return False
        else:
            #print 'bpos'
            return True

    def move_orange(self, target):
        if target > self.opos:
            self.opos += 1
            #print 'opos+1'
            return False
        elif target < self.opos:
            self.opos -= 1
            #print 'opos-1'
            return False
        else:
            #print 'opos'
            return True

    def run(self):
        bnxtpos = 1
        onxtpos = 1
        while (True):
            for i in range(self.step, self.stepcnt):
                if self.case[i][0] == 'B':
                    bnxtpos = self.case[i][1]
                    break
            for i in range(self.step, self.stepcnt):
                if self.case[i][0] == 'O':
                    onxtpos = self.case[i][1]
                    break

            #print 'time:%s | step:%s | bpos:%s | opos:%s | bnxtpos:%s | onxtpos:%s' % (self.t, self.step, self.bpos, self.opos, bnxtpos, onxtpos)

            if self.case[self.step][0] == 'B':
                if self.move_blue(bnxtpos):
                    #print 'bpress'
                    self.step += 1
                self.move_orange(onxtpos)
            elif self.case[self.step][0] == 'O':
                if self.move_orange(onxtpos):
                    #print 'opress'
                    self.step += 1
                self.move_blue(bnxtpos)

            #print '*'*10
            
            if self.step >= self.stepcnt:
                return self.t
            
            self.t += 1

i = 1
for case in cases:
    t = TestCase(case).run()
    print 'Case #%s: %s' % (i, t)
    i += 1
