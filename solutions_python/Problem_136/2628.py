'''
Created on Apr 12, 2014

@author: Ardi
'''

class CookieClickerSolver(object):
    '''
    classdocs
    '''
    def __init__(self, C, F, X):
        '''
        Constructor
        '''
        self._C = C
        self._F = F
        self._X = X    
    
    def solve(self):
        nF = 0 #number of farms
        sunkCost = 0.0 #cost already spent so far       
        incomeRate = 2.0
                
        while True:
            marginalFarmCost = (self._C / incomeRate)                        
            heuristicCost = marginalFarmCost + (self._X / (incomeRate + self._F))
            defaultCost = self._X / incomeRate
            if heuristicCost < defaultCost:
                #then buy an additional farm
                nF += 1
                incomeRate += self._F
                sunkCost += marginalFarmCost
                continue
            else:
                sunkCost += defaultCost
                break
        
        #print('No.of farm: {0}'.format(nF))
        return sunkCost