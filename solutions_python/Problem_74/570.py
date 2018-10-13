#!/usr/bin/python

# go by ticks

def doit():
    move = raw_input().strip().split()
    orange = []
    blue = []
    n = int(move[0])
    for x in xrange(n):
        a = (int(move[2 * x + 2]), x)
        if move[2 * x + 1] == 'O':
            orange.append(a)
        else:
            blue.append(a)
    tick = 0
    odone = 0
    ocur = 1
    bdone = 0
    bcur = 1
    done = [False] * n
    while odone + bdone < n:
        omark = -1
        #print 'tick', tick + 1, ':'
        if odone < len(orange):
            if ocur != orange[odone][0]: # move
                #print 'orange move'
                if ocur < orange[odone][0]:
                    ocur += 1
                else:
                    ocur -= 1
            else: # push
                x = orange[odone][1]
                if x > 0 and not done[x-1]: # wait
                    #print 'orange wait'
                    pass
                else:
                    #print 'orange press'
                    odone += 1
                    omark = x

        if bdone < len(blue):
            if bcur != blue[bdone][0]: # move
                #print 'blue move'
                if bcur < blue[bdone][0]:
                    bcur += 1
                else:
                    bcur -= 1
            else: # try to push
                x = blue[bdone][1]
                if x > 0 and not done[x-1]: # wait
                    #print 'blue wait'
                    pass
                else:
                    #print 'blue press'
                    bdone += 1
                    done[x] = True
        #print omark
        if omark >= 0:
            done[omark] = True
        tick += 1
    print tick


n = input()
for x in xrange(n):
    print 'Case #%d:' % (x+1),
    doit()
