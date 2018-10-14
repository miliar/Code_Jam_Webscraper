#!/usr/bin/python
import sys,os

Tfile = "valT.dat"
args = sys.argv

class robot:
    def __init__(self, but, seq, col):
        self.but = but
        self.seq = seq
        self.col = col
        self.dir = True

    def move(self, color):
        if len(self.seq) == 0: return False
        if self.but == self.seq[0]:
            if color == self.col:
                return self.push()
            else:
                return False
        else:
            if self.dir:
                self.but += 1
            else:
                self.but -= 1

    def push(self):
        self.seq.pop(0)
        if len(self.seq) > 0:
            if self.but < self.seq[0]:
                self.dir = True
            else:
                self.dir = False
        #print "Robot %s pushed at %d."%(self.col,self.but)
        return True

def align( val ):
    rval = []
    for i in range(0,(len(val))/2):
         c = i*2
         rval.append(val[c]+val[c+1])
    return rval

def parse( val ):
    valO = []
    valB = []
    valOB = []
    for k in val:
        if k[0] == 'O':
            valO.append( int(k[1:]) )
            valOB.append( 'O' )
        elif k[0] == 'B':
            valB.append( int(k[1:]) )
            valOB.append( 'B' )
        else:
            # raise
            pass
    return valOB,valO,valB

valT = 0
while valT == 0:
    #valT = raw_input("T : ")
    valT = raw_input("")
    try:
        valT = int("".join(valT))
    except:
        raise

cntT = 0
while cntT < valT:
    #valNRP = raw_input("N B ? O ? : ")
    valNRP = raw_input("")
    valNRP = "".join(valNRP).split(' ')
    if len(valNRP) > 2:
        valN = int(valNRP[0])
        valRP = valNRP[1:]
        if len(valRP)/2 <> valN:
            #print "The length is wrong. Exit."
            continue
    else:
        continue


    valRP = align( valRP )
    valOB,valO,valB = parse( valRP )

    # initialize instances
    _robotO = robot(1,valO,'O')
    _robotB = robot(1,valB,'B')

    time = 0
    for v in valOB:
        while True:
            #print v,time
            time += 1
            resO = _robotO.move(v)
            resB = _robotB.move(v)
            if resO: mesO = "Push"
            else: mesO = "Move"
            if resB: mesB = "Push"
            else: mesB = "Move"
            #print "%d |O %s %d|B %s %d"%(time,mesO,_robotO.but,mesB,_robotB.but)
            if resO or resB: break

    cntT += 1
    print "Case #%d: %d"%(cntT,time)
