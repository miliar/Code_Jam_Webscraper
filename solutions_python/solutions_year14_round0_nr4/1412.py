'''
Created on Apr 11, 2014

@author: Sean Groathouse
'''

class War:
    
    def __init__(self, blocksN, blocksK):
        self.NaomiBlocks = blocksN
        self.KenBlocks = blocksK
        self.NaomiBlocks.sort()
        self.KenBlocks.sort()
        self.KenScore = 0
        self.NaomiScore = 0
        
    def peekKenMove(self, NaomiMove):
        if NaomiMove > self.KenBlocks[len(self.KenBlocks - 1)]:
            return self.KenBlocks[0]
        else:
            for value in self.KenBlocks:
                if value > NaomiMove:
                    return value
                
    def KenMove(self, NaomiMove):
        if NaomiMove > self.KenBlocks[len(self.KenBlocks) - 1]:
            self.NaomiScore += 1
            return self.KenBlocks.pop(0)
        else:
            for (index, value) in enumerate(self.KenBlocks):
                if value > NaomiMove:
                    self.KenScore += 1
                    return self.KenBlocks.pop(index)
                
    def NaomiMove(self):
        return self.NaomiBlocks.pop()
    
    def NaomiCheat(self):
        toPlay = self.NaomiBlocks.pop(0)
        if (toPlay < self.KenBlocks[0]):
            return (self.KenBlocks[len(self.KenBlocks) - 1] - 0.0000001)
        else:
            return (0.9999999)
    
    def play(self):
        while (len(self.NaomiBlocks) > 0):
            self.KenMove(self.NaomiMove())
        return self.NaomiScore
    
    def playDeceit(self):
        while (len(self.NaomiBlocks) > 0):
            self.KenMove(self.NaomiCheat())
        return self.NaomiScore
            
        


if __name__ == '__main__':

    fin = open('D-large.in', 'r')
    finput = fin.readlines()
    fin.close()
    
    it = iter(finput)
    
    numbCases = int(it.next())
    
    output = ""
    
    for case in range(numbCases):
        numBlocks = int(it.next())
        nBlocks = [float(j) for j in (it.next()).split()]
        kBlocks = [float(j) for j in (it.next()).split()]
        
        honest = War(nBlocks[:], kBlocks[:])
        deceitful = War(nBlocks[:], kBlocks[:])
        output += "Case #%d: %d %d\n" % (case+1, deceitful.playDeceit(), honest.play())
        
        
    
    fout = open('large.txt', 'w')
    fout.write(output)
    fout.close