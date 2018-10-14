class CentralSystem:
    
    def __init__(self, searchEngines):
        self.searchEngines = []
        self.bools = []
        self.engine = None
        self.switchs = 0
        
        for e in searchEngines:
            self.searchEngines.append(e)
            self.bools.append(False)
            
    
    def switch(self):
        self.switchs += 1
        oldengine = self.engine
        self.engine = None
        self.cleanBools()
        self.bools[self.searchEngines.index(oldengine)] = True
        
    def cleanBools(self):
        self.bools = []
        for i in range(len(self.searchEngines)):
            self.bools.append(False)
            
    def processQuery(self, q):
        #print 'Processing %s' % q
        
        index = self.searchEngines.index(q)
        

        if q == self.engine:
            self.switch()
        if not self.engine:
            #print 'Setting %s to True' % self.searchEngines[index]
            self.bools[index] = True
            
        onlyOneFalse = self.onlyOneLeft()
        if onlyOneFalse:
            #print 'Engine is now %s' % self.searchEngines[self.bools.index(False)]
            self.engine = self.searchEngines[self.bools.index(False)]

        
        #print 'Bools: %s' % str(self.bools)    
            
    def onlyOneLeft(self):
        n = 0
        
        for k in self.bools:
            if not k:
                n += 1
                
        if n == 1:
            return True
        
        return False
                    
if __name__ == "__main__":
    numberOfCases = int(raw_input())
    ans = 0
    for i in range(1, numberOfCases+1):
        numberOfSearchEngines = int(raw_input())
        
        searchEngines = []

        for j in range(1, numberOfSearchEngines+1):
            searchEngines.append(str(raw_input()))

        numberOfSearchs = int(raw_input())
        
        cs = CentralSystem(searchEngines)
        
        if numberOfSearchs != 0:
            for j in range(1, numberOfSearchs+1):
                querystr = str(raw_input())
                cs.processQuery(querystr)
                ans = cs.switchs
            print 'Case #%d: %s' % (i, ans)
        else:
            print 'Case #%d: %d' % (i, ans)