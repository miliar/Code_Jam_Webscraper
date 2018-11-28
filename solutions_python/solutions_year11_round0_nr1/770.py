import sys, re
class Robot:
    def __init__(self):
        self.position=1
        self.done = False
    def walkForward(self):
        self.position+=1
    def walkBackward(self):
        self.position-=1
    def getPosition(self):
        return self.position
    def nowDone(self):
        self.done = True
    def isDone(self):
        return self.done

p = sys.stdin
rowcount = 0
tot_cases = None
cases = []
for row in p:
    if rowcount==0:
        tot_cases = row
    else:
        cases.append(row)
    rowcount+=1

answers = []

for case in cases:
    working = case.split(' ')
    dir = int(working[0])
    instructions = ' '.join(working[1:]).split()
    pairs = []
    o_instruct = []
    b_instruct = []

    for i in range(0,len(instructions),2):
        tuple = (instructions[i], int(instructions[i+1]))
        pairs.append(tuple)
        if instructions[i]=='O':
            o_instruct.append(tuple)
        else:
            b_instruct.append(tuple)

    orange_bot = Robot()
    blue_bot = Robot()

    timestep = 0
    orange_current = 0
    blue_current =0
    turn = 0
    turn_change = False

    while not dir==0:
        #walk toward stuff
        o_pos = orange_bot.getPosition()
        if orange_current==len(o_instruct):
            orange_bot.nowDone()
            #orange is done
        else:
            o_goal= o_instruct[orange_current][1]
        b_pos = blue_bot.getPosition()
        if blue_current == len(b_instruct):
            blue_bot.nowDone()
            #blue is done
        else:
            b_goal = b_instruct[blue_current][1]

        if not orange_bot.isDone():
            if o_pos==o_goal:
                #press button if it's the turn
                if pairs[turn][0]=='O':
                    dir-=1
                    orange_current+=1
                    turn_change = True
                else:
                    #wait
                    pass

            else:
                #walk forward or backward
                diff = o_pos - o_goal
                if diff>0:
                    orange_bot.walkBackward()
                else:
                    orange_bot.walkForward()

        if not blue_bot.isDone():
            if b_pos==b_goal:
                if pairs[turn][0]=='B':
                    dir-=1
                    blue_current+=1
                    turn_change=True
                else:
                    pass
            else:
                diff = b_pos-b_goal
                if diff>0:
                    blue_bot.walkBackward()
                else:
                    blue_bot.walkForward()
        if turn_change:
            turn+=1
            turn_change=False
        timestep +=1

    answers.append(timestep)

case = 1
for answer in answers:
    st = 'Case #%d: '%case+str(answer)
    sys.stdout.write(st+'\n')
    case+=1
        






