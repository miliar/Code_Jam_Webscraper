log = open('log.txt', 'w')

def writeLog(s):
    pass
    #writeLog(s)
    
def next_button(seq, ch):
    for i, e in enumerate(seq):
        if e[0] == ch:
            return e[1]
    return None

class Robot(object):
    def __init__(self, ch):
        self.ch = ch
        self._pos = 1
        self.des = None
        self.doneAction = False
        
    def getNextDest(self, instructions):
        self.des = next_button(instructions, self.ch)
        
    @property
    def pos(self):
        return self._pos
        
    def move(self):
        assert not self.doneAction
        if not self.des:
            writeLog('%s has no dest\n' % (self.ch))
            return
        self.doneAction = True
        if self.des > self.pos:
            self._pos += 1
            writeLog('%s moved from %d to %d\n' % (self.ch, self.pos-1, self.pos))
        elif self.des < self.pos:
            self._pos -= 1
            writeLog('%s moved from %d to %d\n' % (self.ch,self.pos-1, self.pos))

if __name__=='__main__':    
    input_file = open('A-large-0.in', 'r')
    output_file = open('A-large-0.out', 'w')
    
    for line_num, line in enumerate(input_file.readlines()[1:]):
        button_data = line.split()[1:]
        
        writeLog('\n\nnew %s seq\n' % (line[0]))

        instructions = []
        for i in range(0, len(button_data), 2):
            instructions.append((button_data[i], int(button_data[i+1])))
                    
        time = 0
        O = Robot('O')
        B = Robot('B')
        
        skip=False
        for i, instruct in enumerate(instructions):
            if skip:
                skip = False
                continue
            
            robot, dest = instruct
            writeLog('instruct: robot %s, dest %d, B at %s O at %s\n' % (robot, dest, B.pos, O.pos))
            if robot == 'O': 
                curr_bot, other_bot = O, B
            else:
                curr_bot, other_bot = B, O
            
            curr_bot.des = dest
            other_bot.getNextDest(instructions[i:])
            

            bots_moving= True
                
            while(bots_moving):
                time += 1
                writeLog('## Time %d ##\n' % (time))

                curr_bot.doneAction=False
                other_bot.doneAction=False
                
                if curr_bot.pos == curr_bot.des:
                    assert curr_bot.des == dest
                    curr_bot.doneAction=True
                    writeLog('robot %s press at %s\n' % (curr_bot.ch, dest))
                        
                    bots_moving = False
                else:
                    curr_bot.move()
                    
                other_bot.move()
                    
            
            
        
        
        print >>output_file, 'Case #%s: %d' % (line_num+1, time)
    log.close()
    input_file.close()
    output_file.close()
