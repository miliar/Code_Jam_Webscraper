#!/usr/bin/env python.
#author: Chen Zhao

import os.path

finput = '/Users/chin/dev/codejam/2013/A-large.in'
finput = '/Users/chin/dev/codejam/2013/Round1/test.input'
finput = '/Users/chin/dev/codejam/2013/Round1/A-small.in'


def solve(init_size, motes):
    motes = sorted(motes)
    #print init_size, motes
    size = init_size
    if size==1:
        return len(motes)
    step = 0
    for idx, mote in enumerate(motes):
        if size>mote:
            #print size, '+', mote, '->', size+mote
            size+=mote
            continue
        if size<=mote:
            remain = len(motes)-idx
            fsize = size
            fstep = 0
            while True:
                fstep += 1
                fsize = fsize*2 - 1
                if fsize==size:
                    #print 'remove'
                    step+=remain
                    return str(step)
                if fsize>mote:
                    break
            if fstep<remain:
                #print size, '->', fsize+mote
                step+=fstep
                size = fsize+mote
                continue
            else:
                step+=remain
                break
    return str(step)

def main():
    f = file(finput)
    N = int(f.readline())
    for i in range(1, N+1):
        init_size = int(f.readline().split()[0])
        motes = map(int, f.readline().split())
        print 'Case #%d: %s'%(i, solve(init_size, motes))

if __name__=='__main__':
    main()

