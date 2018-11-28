import sys
class StateMachine:
    def __init__(self, seq, color):
        self.Seq = seq
        self.Color = color
        self.Pos = 1
        if not seq:
            self.State = 2 #Finish
        else:
            if self.Seq[0] == self.Pos:
                self.State = 1 #Ready
                self.Seq.pop(0)
            else:
                self.State = 0 #Move

    def Advance(self, time):
        if self.State == 0:
            next = self.Seq[0]
            selfMoveTime = abs(next - self.Pos)
            if selfMoveTime <= time:
                self.State = 1
                self.Pos = next
                self.Seq.pop(0)
            else:
                if next > self.Pos:
                    self.Pos += time
                else:
                    self.Pos -= time
        #print >>sys.stderr, 'color : ', self.Color, 'state : ', self.State, 'pos : ', self.Pos, self.Seq

    def Action(self):
        totalTime = 0
        if self.State == 2:
            raise Exception('Error!')
        if self.State == 0:
            next = self.Seq[0]
            selfMoveTime = abs(next - self.Pos)
            self.Pos = next
            totalTime = selfMoveTime + 1
            self.Seq.pop(0)
        else:
            totalTime = 1

        if self.Seq:
            self.State = 0
        else:
            self.State = 2

        #print >>sys.stderr, 'color : ', self.Color, 'state : ', self.State, 'pos : ', self.Pos, self.Seq
        return totalTime


#    def Action(self, color):
#        if self.State == 1:
#            if (color == self.Color):
#                if self.Seq:
#                    self.State = 0
#                else:
#                    self.State = 2
#                ##print >>sys.stderr, 'color : ', self.Color, 'state : ', self.State, 'pos : ', self.Pos
#                return True
#            else:
#                ##print >>sys.stderr, 'color : ', self.Color, 'state : ', self.State, 'pos : ', self.Pos
#                return False
#        elif self.State == 2:
#            ##print >>sys.stderr, 'color : ', self.Color, 'state : ', self.State, 'pos : ', self.Pos
#            return False
#        else:
#            next = self.Seq[0]
#            ##print >>sys.stderr, 'color : ', self.Color, 'next : ', next, 'pos : ', self.Pos
#            if next > self.Pos:
#                self.Pos += 1
#            elif next < self.Pos:
#                self.Pos -= 1
#
#            if next == self.Pos:
#                self.State = 1
#                self.Seq.pop(0)
#
#            ##print >>sys.stderr, 'color : ', self.Color, 'state : ', self.State, 'pos : ', self.Pos
#            return False

def input():
    import sys
    case_num = int(sys.stdin.next())
    cases = []
    for i in range(case_num):
        seq = sys.stdin.next().strip().split()
        color_seq = seq[1::2]
        pos_seq = seq[2::2]
        pos_seq = [int(x) for x in pos_seq]
        o_list = []
        b_list = []
        for color, pos in zip(color_seq, pos_seq):
            if color == 'O':
                o_list.append(pos)
            else:
                b_list.append(pos)
        cases.append((color_seq, o_list, b_list))
    return cases

def output(times):
    for index, time in enumerate(times):
        print 'Case #%d: %d' % (index + 1, time)

def calc_one_case(case):
    actionList, seqO, seqB = case
    robotB = StateMachine(seqB, 'B')
    robotO = StateMachine(seqO, 'O')
    totalTime = 0
    while actionList:
        color = actionList[0]
        if color == 'B':
            time = robotB.Action()
            robotO.Advance(time)
        else:
            time = robotO.Action()
            robotB.Advance(time)

        actionList.pop(0)
        #print >>sys.stderr, "time", time
        totalTime += time
    ##print >>sys.stderr, time
    return totalTime

cases = input()
output([calc_one_case(case) for case in cases])
