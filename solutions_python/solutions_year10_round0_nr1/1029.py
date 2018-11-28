import sys

class node:
    
    def __init__(self, switch, power):
        
        self.switch = switch
        self.power = power

class snapper():
    
    def __init__(self):
        
        self.chain = []
        
        self.current = 0
    
    
    def generate_chain(self, size):
        self.current = 0
        self.chain = []
        
        self.chain.append(node(False,True))
        
        size = size - 1  #already inserted the first snap
        
        for i in range(size):
            self.chain.append(node(False, False))
            
        self.chain.append(node(False, False)) #now we add the last node which is the lightbulb
        
    def calculate_snaps(self, snaps):
        SWITCH = 1
        POWER = 2
        flag = 'right'
        
        for i in range(snaps):
            if(flag == 'right'):
                while(flag == 'right'):
                    current = self.chain[self.current]
                    if (self.isBack()):
                        self.switch(POWER)
                        flag = 'left'
                        break
                     
                    if (self.isFront()):
                        self.switch(SWITCH) 
                    else:
                        if(current.power):
                            self.switch(SWITCH)
                        else:
                            self.switch(POWER)
                    
                    if(current.power and current.switch):
                        self.current = self.current + 1
                        continue
                    #can no longer move
                    flag = 'left'
                    break
            else:
                
                while(flag == 'left'):
                    
                    if (self.isFront()):
                        self.switch(SWITCH)
                        flag = 'right'
                        break
                    
                    if(self.isBack()):
                        self.switch(POWER)
                        self.current = self.current - 1
                        continue
                    
                    self.switch(SWITCH)
                    self.switch(POWER)
                    self.current = self.current - 1
            
        return self.chain[-1].power
    
    def isBack(self):
        
        if (self.current == len(self.chain) -1):
            return True
        else:
            return False
        
    def isFront(self):
        
        if (self.current == 0):
            return True
        else:
            return False
    
    def switch(self, value):
        SWITCH = 1
        POWER = 2
        
        if value == SWITCH:
            
            if self.chain[self.current].switch:
                self.chain[self.current].switch = False
            else:
                self.chain[self.current].switch = True
        
        if value == POWER:
            
            if self.chain[self.current].power:
                self.chain[self.current].power = False
            else:
                self.chain[self.current].power = True
                
snap = snapper()
i = 1
file_name = sys.argv[1]
file = open(file_name, 'r')
for line in file:
    input = line.split(' ')
    
    try:
        n = int(input[0])
        k = int(input[1])
    except:
        continue
    
    snap.generate_chain(n)
    if snap.calculate_snaps(k):
        print 'Case #' + str(i) + ': ON'
    else:
        print 'Case #' + str(i) + ': OFF'
        
    i = i + 1

