import os
import sys 


class ProblemSolver: 
    
    def readProblem( self , infile ):  
        (self.N, self.M) = infile.readline().split()  
        self.N = int(self.N)
        self.M = int(self.M)

        self.lawn = [] 
        self.result = "YES" 

        for n in range( self.N ): 
            ln = infile.readline().strip().split()
            for m in range( self.M ):
                self.lawn.append( int( ln[m] ) ) 

    def solve( self ):
        for n in range(self.N): 
            for m in range(self.M): 

                val = self.lawn[ n * self.M + m ] 
                foundpath = True 

                for h in range( self.M * n, self.M * (n+1) ): 
                    if self.lawn[ h ] > val: 
                        foundpath = False
                        break 

                if not foundpath:
                    foundpath = True
                    for v in range( m, self.N * self.M, self.M ): 
                        if self.lawn[ v ] > val: 
                            foundpath = False
                            break 
                    
                if not foundpath: 
                    self.result = "NO"
                    return 
                    
                    
    
    def solution( self ): 
        return self.result
        
ncases = int( sys.stdin.readline().strip() ) 
solver = ProblemSolver() 

for n in range( ncases ): 
    solver.readProblem( sys.stdin ) 
    solver.solve() 
    print "Case #{0}:".format( n +1) , solver.solution()

