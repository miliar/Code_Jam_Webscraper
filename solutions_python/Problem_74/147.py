class Robot():
    
    def __init__(self, who):
        self.who = who
        self.curpos = 1
        self.nextcmd = None
        self.curcmd = 1
        self.idx = 0
        
    def getnextcmd(self, linelst):
        if self.who == "O":
            i = self.idx
            found = False
            while i < len(linelst) / 2:
                if linelst[2*i] == "O":
                    self.nextcmd = []
                    self.nextcmd.append(i + 1)
                    self.nextcmd.append(int(linelst[2*i+1]))
                    found = True
                    break
                i += 1
            if not found:
                self.nextcmd = None
        if self.who == "B":
            i = self.idx
            found = False
            while i < len(linelst) / 2:
                if linelst[2*i] == "B":
                    self.nextcmd = []
                    self.nextcmd.append(i + 1)
                    self.nextcmd.append(int(linelst[2*i+1]))
                    found = True
                    break
                i += 1
            if not found:
                self.nextcmd = None
            
    
        

def main():
    inpfile = open("A-large.in", 'r')
    outfile = open('outfile', 'w')
    casenum = int(inpfile.readline().strip())
    for case in range(1, casenum + 1):
        linelst = inpfile.readline().strip().split()
        numbutton = linelst[0]
        linelst.remove(numbutton)
        numbutton = int(numbutton)
        #print numbutton
        #print linelst
        
        O = Robot("O")
        B = Robot("B")
        
        O.getnextcmd(linelst)
        B.getnextcmd(linelst)
        #print O.nextcmd
        #print B.nextcmd
        #print "---------"
        counter = 0
        Round = 1
        while O.nextcmd != None or B.nextcmd != None:
            cmdexecuated = False
            if not O.nextcmd == None:
                if O.nextcmd[1] > O.curpos:
                    O.curpos += 1
                elif O.nextcmd[1] < O.curpos:
                    O.curpos -= 1
                elif O.nextcmd[1] == O.curpos:
                    if O.nextcmd[0] == Round:
                        O.idx += 1
                        B.idx += 1
                        O.getnextcmd(linelst)
                        cmdexecuated = True
                    
            if not B.nextcmd == None:
                if B.nextcmd[1] > B.curpos:
                    B.curpos += 1
                elif B.nextcmd[1] < B.curpos:
                    B.curpos -= 1
                elif B.nextcmd[1] == B.curpos:
                    if B.nextcmd[0] == Round:
                        O.idx += 1
                        B.idx += 1
                        B.getnextcmd(linelst)
                        cmdexecuated = True
            if cmdexecuated:
                Round += 1
            counter += 1
            #print O.nextcmd
            #print B.nextcmd
            #print "---------"
            
        
        result = "Case #" + str(case) + ": "  + str(counter) + "\n"
        outfile.write(result)
    inpfile.close()
    outfile.close()

    
if __name__ == "__main__":
    main()
    
