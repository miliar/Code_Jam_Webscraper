from collections import defaultdict
from itertools import izip

def process(cmds):
    lastmove = None
    Opos = 1
    Oleft = 0
    Bpos = 1
    Bleft = 0
    step = 0
    for p,pos in cmds:
        pos = int(pos)
        if p == 'O':
            movstep = max(abs(Opos-pos)-Oleft,0) + 1
            step += movstep
            Oleft = 0
            Opos = pos
            Bleft += movstep
        if p == 'B':
            movstep = max(abs(Bpos-pos)-Bleft,0) + 1
            step += movstep
            Bleft = 0
            Bpos = pos
            Oleft += movstep
    return step

def main():
    for case in xrange(1,int(raw_input())+1):
        _inp = raw_input().split(' ')[1:]
        cmds = [(k,v) for k,v in izip(_inp[::2],_inp[1::2])]
        print 'Case #%d: %d' %(case,process(cmds))
    
if __name__ == "__main__":
    main()
