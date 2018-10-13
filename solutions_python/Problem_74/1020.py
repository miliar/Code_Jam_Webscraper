import collections

# !!!!!!!!!!!! start at 1

def trust(fnin, fnout):
    filein = open(fnin, 'r')
    T = int(filein.readline())

    fileout = open(fnout, 'w')
    for casenum in range(T):
        case_desc = filein.readline()
##        print 'Case #%i' % (casenum+1)
        fileout.write('Case #%i: ' % (casenum+1))
        fileout.write(str(case(case_desc)))
        fileout.write('\n')

    filein.close()
    fileout.close()
    del filein
    del fileout


def case(desc):
    q = collections.deque(desc.split(' '))
    N = int(q.popleft())
    O = Robot('O')
    B = Robot('B')
    sched = collections.deque()
    while len(q) > 0:
        color = q.popleft()
        btn = int(q.popleft())
        if color == 'O':
            O.sched.append(btn)
        else:
            B.sched.append(btn)
        sched.append((color, btn))
##    print "O.sched: %s" % O.sched
##    print "B.sched: %s" % B.sched
##    print sched

    # check if in place; if not - step
    # if in place and next - push
    # else wait

    # !!! note if Xsch is empty

    time = 0
    O.set_targ()
    B.set_targ()
##    print "O\B targs: %i, %i" % (O.targ, B.targ)

    while len(sched) > 0:
        next = sched.popleft()
##        print "next: %c" % next[0]
##        print next,

        free = False
        while not free:
##            print "time %i" % time
            
            if next[0] == "O":
                nextR, otherR = O, B
            else:
                nextR, otherR = B, O

            if not (nextR.at_targ()):
                nextR.step()
            else:
                # pushing button
##                print 'btn pushed at %d' % (time + 1)
                nextR.set_targ()
                free = True

            if not otherR.at_targ():
                otherR.step()

            time += 1
##            free = True

    return time


class Robot:
    def __init__(self, color):
        self.color = color
        self.pos = 1
        self.targ = None
        self.sched = collections.deque()

    def set_targ(self):
        if len(self.sched) > 0:
            self.targ = self.sched.popleft()
        else:
            return None

    def at_targ(self):
##        print "%c targ: %i, pos %i" % (self.color, self.targ, self.pos)
        if (self.targ != None) and (self.targ - self.pos != 0):
##            print '%c at_targ false' % self.color
            return False
        else:
##            print '%c at_targ true' % self.color
            return True

    def step(self):
        diff = self.targ - self.pos
        self.pos += (diff/abs(diff))
##        print "step: %c now at %i" % (self.color, self.pos)
