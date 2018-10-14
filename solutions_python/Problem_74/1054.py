#!/usr/bin/env python

# Getting file descriptors

f = open('input-2.in', 'r')     # Replace with appropriate file name
s = open('outputfile', 'w')

# Defining classes

class bot (object):

    def __init__(self):
        self.seq = []
        self.pos = 1
    
    def move(self):
        if len(self.seq) > 0:
            if self.seq[0] < self.pos:
                self.pos -= 1
            elif self.seq[0] > self.pos:
                self.pos += 1
        else:
            pass
        
    def pb(self):
        del self.seq[0]
        
    def onb(self):
        if len(self.seq)>0:
            return (self.seq[0]==self.pos)
        else:
            return False
    
    def wait(self):
        pass

# Defining functions


def process(line):
    s = line.split()
    T = int(s[0])
    Flag = 0
    Orange = bot()
    Blue = bot()
    OrderT = []
    
    for n in range(1,2*T+1,1):
        if Flag == 1:
            Flag = 0
            continue
        elif s[n] == 'O':
            Orange.seq.append(int(s[n+1]))
            OrderT.append(2)
            Flag = 1
        elif s[n] == 'B':
            Blue.seq.append(int(s[n+1]))
            OrderT.append(1)
            Flag = 1
    
    Count = 0
    while len(OrderT)>0:
        if OrderT[0] == 1:
            if Blue.onb():
                Blue.pb()
                del OrderT[0]
            else:
                Blue.move()
            if Orange.onb():
                Orange.wait()
            else:
                Orange.move()
        elif OrderT[0] == 2:
            if Orange.onb():
                Orange.pb()
                del OrderT[0]
            else:
                Orange.move()
            if Blue.onb():
                Blue.wait()
            else:
                Blue.move()
        Count += 1
        
    return Count

# Getting input and processing

LineNum = 0

for line in f:
    if LineNum == 0:
        NumCases = int(line)
        LineNum += 1
    else:
        s.write("Case #%d: %s\n"%(LineNum,process(line)))
        LineNum += 1


# Closing files

f.close()
s.close()