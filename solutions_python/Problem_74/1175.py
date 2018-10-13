#!/usr/bin/python
import sys, os

def usage():
    print("%s " % sys.argv[0] )

def calTime(line):
#    print "line=",line
    time = 0
    oq = []
    bq = []
    l = len(line)
    for seq in xrange(l/2):
        if line[seq*2] == 'B':
            bq.append( (seq, line[seq*2], int(line[seq*2+1])) )
        else:
            oq.append( (seq, line[seq*2], int(line[seq*2+1])) )

#    print 'bq=', bq, 'oq=',oq
    opos = 1
    bpos = 1
    while len(bq) > 0 or len(oq) >0:
#        print "time=", time, " opos=", opos, " bpos=", bpos
        if len(bq) == 0:
            seq, role, pos = oq.pop(0)
            time += abs(pos - opos)
            opos = pos
            time += 1
        elif len(oq) == 0:
            seq, role, pos = bq.pop(0)
            time += abs(pos - bpos)
            bpos = pos
            time += 1
        else:
            # need to move both
            odist = abs(oq[0][2] - opos)
            bdist = abs(bq[0][2] - bpos)
            # consider pri
            if (oq[0][0] < bq[0][0]):
                # move orange
                opos = oq[0][2]
                # blue may get next pos or not
                if (odist!=0):
                    if (bdist >= odist):
                        # cannot get there
                        if (bq[0][2] >= bpos):
                            bpos = bpos + odist
                        else:
                            bpos = bpos - odist
                    else:
                        # get there
                        bpos = bq[0][2]
                time += odist
                time += 1 # push
                if (bpos > bq[0][2]): bpos -= 1
                elif (bpos < bq[0][2]): bpos += 1
                oq.pop(0)
            else:
                # move blue
                bpos = bq[0][2]
                # blue may get next pos or not
                if (bdist!=0):
                    if (odist >= bdist):
                        # cannot get there
                        if (oq[0][2] >= opos):
                            opos = opos + bdist
                        else:
                            opos = opos - bdist
                    else:
                        # get there
                        opos = oq[0][2]
                time += bdist
                time += 1 # push
                if (opos > oq[0][2]): opos -= 1
                elif (opos < oq[0][2]): opos += 1
                bq.pop(0)
    return time;
if __name__ == '__main__':
    for no, line in enumerate(sys.stdin):
        if no == 0: continue
        f = line.split()
        data = f[1:]
        print "Case #%d: %d" % (no, calTime(data))
        
