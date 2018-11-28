import sys 

squares = [1, 4, 9, 121, 484, 12321, 14641, 44944, 1234321, 123454321, 125686521, 12345654321, 1234567654321, 123456787654321]; 

class ProblemSolver: 
    
    def readProblem( self , infile ):  
        (self.A, self.B) = infile.readline().split()  
        self.A = int( self.A ) 
        self.B = int( self.B )

    def findMin( self ):
        idxA = -1 
        for a in range( len( squares ) ): 
            if squares[a] >= self.A:
                return a 

        return idxA 

    def findMax( self ):
        idxB = len( squares )
        for b in range( 0, len( squares ) ): 
            if squares[b] > self.B:
                return b
        return idxB

    def solve( self ):
        idxA = self.findMin()
        idxB = self.findMax()
        self.result = idxB - idxA 

    def solution( self ): 
        return self.result
        
ncases = int( sys.stdin.readline().strip() ) 
solver = ProblemSolver() 

for n in range( ncases ): 
    solver.readProblem( sys.stdin ) 
    solver.solve() 
    print "Case #{0}:".format( n +1) , solver.solution()
