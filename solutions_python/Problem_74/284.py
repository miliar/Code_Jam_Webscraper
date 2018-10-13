import sys, os

class BotGame(object):
    
    def __init__(self, line):
        words = line.split(" ")
        self.buttons = int(words[0])
        self.pos_o = self.pos_b = 1
        self.index_o = self.index_b = 0
        self.moves = []
        self.moves_o = []
        self.moves_b = []
        for i in range(1, len(words)):
            if i % 2 == 1: continue
            self.moves.append(words[i-1])
            if words[i-1] == "O":
                self.moves_o.append(int(words[i]))
            else:
                assert(words[i-1] == "B")
                self.moves_b.append(int(words[i]))
    
    def current_target(self):
        return self.moves[self.index]
    
    def get_position(self, move):
        if move == "O": return self.pos_o
        else: return self.pos_b
        
    def get_index(self, move):
        if move == "O": return self.index_o
        else: return self.index_b
        
    def move_o(self):
        if self.index_o == len(self.moves_o): return
        
        target = self.moves_o[self.index_o]
        if self.pos_o == target and self.current_target() == "O":
            # we can push the button
            self.index_o += 1
            #print "pushing O at %s" % target
            return True
        elif self.pos_o == target:
            # we're in place but waiting for our turn    
            pass
        else:
            # get closer
            self.pos_o += (target - self.pos_o) / abs((target - self.pos_o))
        
    def move_b(self):
        if self.index_b == len(self.moves_b): return
        target = self.moves_b[self.index_b]
        if self.pos_b == target and self.current_target() == "B":
            # we can push the button
            self.index_b += 1
            #print "pushing B at %s" % target
            return True
        elif self.pos_b == target:
            # we're in place but waiting for our turn    
            pass
        else:
            # get closer
            self.pos_b += (target - self.pos_b) / abs((target - self.pos_b))
            
        
    def next_move(self):
        update = False
        moves = 0
        while not update:
            moves += 1
            update = self.move_o()
            update = self.move_b() or update
        self.rounds += moves
        # print "moves: %s, total: %s" % (moves, self.rounds)
        
    def play(self):
        self.rounds = 0
        self.index = 0
        for i in range(len(self.moves)):
            self.next_move()
            self.index += 1
        return self.rounds
            

    def __str__(self):
        return "order: %s\nmoves o: %s\nmoves b: %s" % (" ".join(self.moves), 
                                                        " ".join(str(m) for m in self.moves_o),
                                                        " ".join(str(m) for m in self.moves_b))
    
        
    
        
        
def solve(filename):
    fname = os.path.join(os.path.dirname(__file__), "data", filename)
    with open(fname) as data:
        first = True
        case = 1
        for line in data:
            if first:
                games = int(line)
                first = False
            else:
                game = BotGame(line)
                print "Case #%s: %s" % (case, game.play())
                case += 1
                
    

if __name__ == "__main__":
    solve("A-large.in")