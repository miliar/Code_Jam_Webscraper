import fileinput
import copy

import psyco
psyco.full()

class BotsState(object):
    def __init__(self):
        self.bot_last_press_loc = copy.deepcopy([(1,0),(1,0)])
    def advance_to_next_state(self,bot_to_move,target):
        #print "Moving bot:",bot_to_move,"to",target
        #print "Current state:",self.bot_last_press_loc
        time_to_target = max(self.bot_last_press_loc[bot_to_move][1]+(abs(target-self.bot_last_press_loc[bot_to_move][0])+1),
                             self.bot_last_press_loc[(bot_to_move+1)%2][1]+1)
        self.bot_last_press_loc[bot_to_move] = (target,time_to_target)
    def get_time_to_finish(self,move_seq):
        for m in move_seq:
            self.advance_to_next_state(*m)
        return max([x[1] for x in self.bot_last_press_loc])

it = fileinput.input()
num_cases = int(it.next())

for i,l in enumerate(it):
    raw_ops = l.split()
    ops = [(x[0] == 'B',int(x[1])) for x in zip(raw_ops[1::2],raw_ops[2::2])]
    state = BotsState()
    print "Case #%d: %d" % (i+1, state.get_time_to_finish(ops))

    
