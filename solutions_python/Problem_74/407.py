filename="samp.txt"
filename="A-small-attempt0.in"
filename="A-large.in"
data_sets = [line.strip().split(" ")[1:] for line in open(filename,'r').readlines()[1:]]
class Robot:
    def __init__(self):
        self.free = 0
        self.pos  = 1
for (num,data_set) in enumerate(data_sets):
    count = 0
    robots = {'O':Robot(),'B':Robot()}
    last_rob = ''
    for (robot,move) in zip(data_set[0::2],map(int,data_set[1::2])):
        other = ['O','B'][robot == 'O']
        rob =  robots[robot]
        count += 1 if rob.free > abs(move-rob.pos) else max(0,abs(move-rob.pos) - rob.free) +1
#        print abs(move-rob.pos) - rob.free 
        robots[other].free += max(0,abs(move-rob.pos) - rob.free) + 1
#        if last_rob == other:
#            robots[other].free = 0
#        if rob.free - abs(move-rob.pos) < 0:
#            robots[other].free += -1*(rob.free - abs(move-rob.pos))
#        print robot,move,rob.pos,rob.free,count,robots[other].free
        rob.free = 0#min(0,rob.free - abs(move-rob.pos))
        last_rob = robot
        rob.pos = move
    print "Case #%d: %d"%(num+1,count)
        
# print data_sets[1]
