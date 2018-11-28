## Code by Preston Hamlin for CodeJam 2013
## prestonwhamlin@gmail.com

## If anyone ever does read this, say hello

class GameState():
    def __init__(self, ifile):
        self.line0 = ifile.readline()
        self.line1 = ifile.readline()
        self.line2 = ifile.readline()
        self.line3 = ifile.readline()
        
        self.vert0 = (self.line0[0] + self.line1[0] + self.line2[0] + self.line3[0])
        self.vert1 = (self.line0[1] + self.line1[1] + self.line2[1] + self.line3[1])
        self.vert2 = (self.line0[2] + self.line1[2] + self.line2[2] + self.line3[2])
        self.vert3 = (self.line0[3] + self.line1[3] + self.line2[3] + self.line3[3])
        
        self.m_diag = (self.line0[0] + self.line1[1] + self.line2[2] + self.line3[3])
        self.s_diag = (self.line0[3] + self.line1[2] + self.line2[1] + self.line3[0])
        
        self.lines = [self.line0, self.line1, self.line2, self.line3,
                      self.vert0, self.vert1, self.vert2, self.vert3,
                      self.m_diag, self.s_diag]
        
        self.state = 1
        
        self.set_state()
        
    def set_state(self):
        for line in self.lines:
            ##print line
            if 'T' in line:            ## only need 3 to match
                tmp = line.replace('T', '')
                if (tmp[0] == tmp[1] == tmp[2]):  ## all same plus T, victory
                    if (tmp[0] == 'X'):
                        self.state = 2
                        ##print "X wins"
                    elif (tmp[0] == 'O'):
                        self.state = 3
                        ##print "O wins"
            else:
                if (line[0] == line[1] == line[2] == line[3]):  ## all 4 match
                    if (line[0] == 'X'):
                        self.state = 2
                        ##print "X wins"
                    elif (line[0] == 'O'):
                        self.state = 3
                        ##print "O wins"    
        ## if game is not finished
        if self.state == 1:
            for line in self.lines:
                if '.' in line:
                    self.state = 0
    def get_state(self):
        return self.state
        
        
state_list = ["Game has not completed", "Draw", "X won", "O won"]
result_list = {}
        
ifile = open("input.txt", "r")
ofile = open("output.txt", "w")
        
num_cases = int(ifile.readline())

for case in range(num_cases):
    game = GameState(ifile)
    result_list[case] = game.get_state()
    ##print "game " + str(case) + " added"
    
    ifile.readline()
    
for case in range(num_cases):
    ofile.write("Case #" + str(case +1) + ": " + state_list[result_list[case]] + '\n')

print "FINISHED"

ifile.close()
ofile.close()

