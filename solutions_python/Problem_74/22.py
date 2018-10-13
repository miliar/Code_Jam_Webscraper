import sys

class Move:
    def __init__(self, bot, position, preceding_move):
        self.done = False
        self.bot = bot
        self.position = position
        self.preceding_move = preceding_move

class Bot:
    def __init__(self, bot, position, moves):
        self.bot = bot
        self.position = position
        self.moves = moves

    def should_move(self):
        if len(self.moves) == 0:
            return False
        
        move = self.moves[0]
        distance = move.position - self.position
        
        return distance != 0

    def move(self):
#        print "bot ", self.bot, " moving"
        move = self.moves[0]
        distance = move.position - self.position
        if distance > 0:
            self.position = self.position + 1
        if distance < 0:
            self.position = self.position - 1


    def can_execute(self):
        if len(self.moves) == 0:
            return False

        move = self.moves[0]
        distance = move.position - self.position

        return distance == 0 and (move.preceding_move == None or move.preceding_move.done == True)

    def execute(self):
        if not self.can_execute():
            return False

#        print "bot ", self.bot, " executing"
        move = self.moves[0]
        move.done = True

        self.moves = self.moves[1:]



numcases = int(sys.stdin.readline())
for casenumber in xrange(1,numcases+1):
    caseline = sys.stdin.readline().rstrip("\r\n").split(" ")
    seq_len = int( caseline[0] )
    caseline = caseline[1:]

    turns_taken = 0

    b_moves = []
    o_moves = []

    last_move = None
    for i in xrange(0, seq_len):
        bot = caseline[(2*i)]
        pos = int(caseline[(2*i)+1])

        move = Move(bot, pos, last_move)
        last_move = move

        if bot == "O":
            o_moves.append(move)
        if bot == "B":
            b_moves.append(move)

            
    b_bot = Bot("B", 1, b_moves)   
    o_bot = Bot("O", 1, o_moves)

    while len(o_bot.moves) > 0 or len(b_bot.moves) > 0:
#        print "at t = ", turns_taken
        o_moved = False
        b_moved = False
        o_executed = False
        b_executed = False

        if o_bot.should_move():
            o_moved = True
            o_bot.move()

        if not o_moved:
            if o_bot.can_execute():
                o_bot.execute()
                o_executed = True
                    
        if b_bot.should_move():
            b_moved = True
            b_bot.move()

        if not b_moved:
            if b_bot.can_execute() and not o_executed:
                b_bot.execute()
                b_executed = True

        if b_executed and (not o_executed) and (not o_moved):
            if o_bot.can_execute() and not b_executed:
                o_bot.execute()
        
        turns_taken = turns_taken + 1
                  

    print "Case #%d: %u" % (casenumber, turns_taken)

