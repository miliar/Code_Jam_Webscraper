'''
Created on May 7, 2010

@author: randy
'''

class Snapper(object):
    
    def drawChain(self):
        for a in range(self.n):
            self.chain.append([ False, False ])        # tuple of current snapper sate  (power , On)
        self.chain[0][0] = True
    

    def snap(self):
        size = len(self.chain)
        for i in range(size):
            
            
            if i != 0:
                
                if self.chain[i][0] == True:
                    self.chain[i][1]  = not self.chain[i][1]
                
                if self.chain[i-1][0] == True and self.chain[i-1][1] == True:
                    self.chain[i][0] = True
                else:
                    self.chain[i][0] = False
                
                if self.chain[i][1] == False:
                    continue
                        
            else:
                self.chain[i][1] = not self.chain[i][1]
#                
#            
#            
#            
#            
#            if self.chain[i][0] == True:           # There is power!
#                self.chain[i][1] = not self.chain[i][1]             # toggle the switch    
#                
#                if i != 0 :
#                    if self.chain[i-1][1] == True :     # Because current button is on, there's power on the next 
#                        # print "There's power and button on"
#                        if (self.chain[i+1][0] == False):
#                            self.chain[i+1][0] =  True
#                            continue   # break the iteration, don't go further
#                        
#                    else:   # current button is off, there's no power on the next.
#                        if self.chain[i+1][0] == True:  # there was power on the next, toggle switch
#                            self.chain[i+1][1] = not self.chain[i+1][1]
#                        self.chain[i+1][0] = False
#                        
#            else:
#                pass
#                
    def run(self):
        for a in range(self.k):
            self.snap()
            print self.chain    
            #print self.chain, a
        if self.chain[-1][0] == True and self.chain[-1][1] == True:     # It's receiving power from the last snapper
            return not self.lightOn
        
        else:
            return self.lightOn
    
    def __init__(self, n, k):
        self.lightOn = False
        chain = []
        self.chain = chain
        self.n = eval(n) 
        self.k = eval(k)
        self.drawChain()
        
        


    
    
    