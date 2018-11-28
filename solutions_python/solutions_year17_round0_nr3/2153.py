class Stalls(object):
    
    FREE = 0
    TAKEN = 1
    
    FREE_CHAR = '_'
    TAKEN_CHAR = 'X'
    
    def __init__(self, N):
        self.N = N # number of stalls
        self.stalls = [self.FREE]*N # stalls[i] is FREE is stall i is free, is TAKEN if stall i is taken
        self.ls = self._get_l_dists() # ls[i] is the number of contiguous free stalls to the left of stall i 
        self.rs = self._get_r_dists() # rs[i] is the number of contiguous free stalls to the right of stall i
        self.m = 0 # num ppl in stalls (excluding the two guards at either end)
    
    def _get_l_dists(self):
        return range(self.N)
    def _get_r_dists(self):
        return list(reversed(range(self.N)))
        
    # next
    def n(self):
        
        if self.m == self.N:
            print ('All stalls are taken!'
                   ' The next person must wait FOREVER!')
            return
        
        max_min_l_r_soFar = -1 # first criteria
        max_max_l_r_soFar = -1 # tie breaker
        
        # TODO: rewrite as a oneliner using max and lambdas
        for i, l, r in zip(range(self.N), self.ls, self.rs):
            
            if self.stalls[i] == self.TAKEN:
                continue
            
            if min(l,r) > max_min_l_r_soFar:
                max_min_l_r_soFar = min(l,r)
                max_max_l_r_soFar = max(l,r)
                s = i
            elif min(l,r) == max_min_l_r_soFar:
                if max(l,r) > max_max_l_r_soFar:
                    max_max_l_r_soFar = max(l,r)
                    s = i
        
        self.stalls[s] = self.TAKEN
        
        # update self.ls
        i = s+1
        d = 0
        while i < self.N and self.stalls[i] == self.FREE:
            self.ls[i] = d
            i += 1
            d += 1
        
        # update self.rs
        i = s-1
        d = 0
        while i >= 0 and self.stalls[i] == self.FREE:
            self.rs[i] = d
            i -= 1
            d += 1
        
        self.m += 1
    
    # play
    def p(self):
        self.n()
        print self
    
    def __str__(self):
        r = lambda s : self.TAKEN_CHAR if s == self.TAKEN else self.FREE_CHAR
        return ' '.join( map( r, self.stalls ) )


# Play with it!
# 
# In the interative python shell,
# do
#   >>> from stalls import *
#   >>> s = Stalls(21)
#   >>> print s
#   
#   >>> s.p()
#   
#   >>> s.p()
#   
#   ...