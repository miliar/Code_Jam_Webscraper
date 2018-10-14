# coding: utf-8
isdebug = False

class Robot:
    def __init__(self):
        self.at = 1
        self.msg = ''

ntcase = int(raw_input())
for tcase in range(ntcase):
    # read
    a = raw_input().split()[1:]
    lst = zip(map(lambda n: 'OB'.index(n), a[0::2]), map(int, a[1::2]))
    # init
    # Orange/Blue
    state = [Robot(), Robot()]
    if isdebug:
        print lst
        print '+------+--------------------------+--------------------------+----------------+-------+----------------+'
        print '| Time | Orange                   | Blue                     | value          | index | value          |'
        print '+------+--------------------------+--------------------------+----------------+-------+----------------+'
    # calc
    index = 0
    turn = 0
    while index != len(lst):
        r,k = lst[index]
        
        pushed = False
        for si in [0, 1]:
            robot = state[si]
            if r == si:
                # push or move
                if robot.at == k:
                    pushed = True
                    robot.msg = 'Push button %d' % k
                else:
                    robot.at += 1 if robot.at < k else -1
                    robot.msg = 'Move-to-button %d' % robot.at
            else:
                # wait or move
                nextk = None
                for i in range(index + 1, len(lst)):
                    if lst[i][0] == si:
                        nextk = lst[i][1]
                        break
                if nextk != None and robot.at != nextk:
                    robot.at += 1 if robot.at < nextk else -1
                    robot.msg = 'Move to button %d' % robot.at
                else:
                    robot.msg = 'Stay at button %d' % robot.at
        if pushed:
            index += 1
        turn += 1
        if isdebug:
            print '| %4d | %s | %s | %s | %5d | %s |' % (turn,state[0].msg.ljust(24),state[1].msg.ljust(24), str((r, k)).ljust(14), index, (str(lst[index]) if index != len(lst) else '').ljust(14))
           
    if isdebug:
        print '+------+--------------------------+--------------------------+----------------+-------+----------------+'
    
    # result
    print 'Case #%d: %d' % (tcase + 1, turn)
