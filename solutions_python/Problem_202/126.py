# I run this with python 3.4.3

##       - fix finalUpdateCheck

import numpy as np # used for arrays; Can be downloaded from www.numpy.org

# I use filenames for input/output
debug=False
#filename = 'sample.in'
filename = 'D-small-attempt1.in'
#filename = 'D-large.in'
outputFilename = filename.replace('in','out')


# free: 0
# +: 1
# x: 2
# o: 3
MODEL={'.':0,'+':1,'x':2,'o':3}
        
class Field:
    def __init__(self, N, M):
        self.N = N
        self.field = np.zeros( (N,N) ) # saves the state of the field
        self.freeForX = np.ones( (N,N) )
        self.freeForPlus = np.ones( (N,N) )
        self.history=[]
        self.score = 0
        self.M = M # the first M models are already determined, they can be upgraded
    def addModel( self, model, x, y ):
        if debug:
            print( (model, x, y) )
        if model == 'x':
            #print( self.freeForX )
            assert self.freeForX[x,y] == 1
            assert self.field[x,y] == 0
            self.field[x,y] = MODEL['x']
            self.history.append( ('x', x, y) )
            self.score += 1
            for z in range(self.N):
                self.freeForX[x,z] = 0;
                self.freeForX[z,y] = 0;
            #self.freeForPlus[x,y] = 0;
        elif model == '+':
            assert self.freeForPlus[x,y] == 1
            assert self.field[x,y] == 0
            self.field[x,y] = MODEL['+']
            self.history.append( ('+', x, y) )
            self.score += 1
            for z in range(self.N):
                if 0<= x+y-z < self.N:
                    self.freeForPlus[z,x+y-z] = 0;
                if 0<= z+y-x < self.N:
                    self.freeForPlus[z,z+y-x] = 0;
            #self.freeForX[x,y] = 0;
        elif model == 'o':
            assert self.freeForX[x,y] == 1
            assert self.freeForPlus[x,y] == 1
            assert self.field[x,y] == 0
            self.field[x,y] = MODEL['o']
            self.history.append( ('o', x, y) )
            self.score += 2
            for z in range(self.N):
                self.freeForX[x,z] = 0;
                self.freeForX[z,y] = 0
            for z in range(self.N):
                if 0<= x+y-z < self.N:
                    self.freeForPlus[z,x+y-z] = 0;
                if 0<= z+y-x < self.N:
                    self.freeForPlus[z,z+y-x] = 0;
            self.freeForX[x,y] = 0;
            self.freeForPlus[x,y] = 0;
        else:
            raise ValueError(model)
        
        #print( "free for +", self.freeForPlus )
        #print( "free for x", self.freeForX )
            
    def placePlusOnEdge(self):
        # my guess is, that "+"-models should be close to the edge
        # horizontal or vertical?
        allowedField = np.logical_and( (self.freeForPlus==1), (self.field==0) )
        if allowedField[:,0].sum() + allowedField[:,self.N-1].sum() > allowedField[0,:].sum() + allowedField[self.N-1,:].sum():
            # horizontal
            # search for free spot
            for x in range(self.N):
                if allowedField[x,0]==1:
                    self.addModel('+', x, 0)
                    return 1
                if allowedField[x,self.N-1]==1:
                    self.addModel('+', x, self.N-1)
                    return 1
            return 0
        else:
            # vertical
            # search for free spot
            for y in range(self.N):
                if allowedField[0,y]==1:
                    self.addModel('+', 0, y)
                    return 1
                if allowedField[self.N-1,y]==1:
                    self.addModel('+', self.N-1, y)
                    return 1
            return 0
    def placeXSomewhere(self):
        # I didn't see a best way, where to put these models

        allowedField = np.logical_and( (self.freeForX==1), (self.field==0) )
        indices = np.where(allowedField==True)
        if len(indices[0]) == 0:
            return 0
        #print(indices)
        x = indices[0][0]
        y = indices[1][0]
        self.addModel('x', x, y)
        return 1
    def finalUpdateCheck(self):
        #print( "free for +", self.freeForPlus )
        #print( "free for x", self.freeForX )
        for i in range(len(self.history)):
            model, x, y = self.history[i]
            if model == 'x':
                #print('update x')
                if self.freeForPlus[x,y] == 1:
                    if i < self.M:
                        self.field[x,y] = MODEL['o']
                        self.history.append( ('o', x, y) )
                        self.score += 1
                        for z in range(self.N):
                            if 0<= x+y-z < self.N:
                                self.freeForPlus[z,x+y-z] = 0;
                            if 0<= z+y-x < self.N:
                                self.freeForPlus[z,z+y-x] = 0;
                            self.freeForX[z,y] = 0;
                    else:
                        self.history[i] = ('o', x, y) # change history
                        self.field[x,y] = MODEL['o']
                        self.score += 1
                        for z in range(self.N):
                            if 0<= x+y-z <= self.N:
                                self.freeForPlus[z,x+y-z] = 0;
                            if 0<= z+y-x <= self.N:
                                self.freeForPlus[z,z+y-x] = 0;
                            self.freeForX[z,y] = 0;
            elif model == '+':
                #print('update +')
                if self.freeForX[x,y] == 1:
                    #print('yeah')
                    #print
                    if i < self.M:
                        self.field[x,y] = MODEL['o']
                        self.history.append( ('o', x, y) )
                        self.score += 1
                        for z in range(self.N):
                            self.freeForX[x,z] = 0;
                            self.freeForX[z,y] = 0;
                    else:
                        self.history[i] = ('o', x, y) # change history
                        self.field[x,y] = MODEL['o']
                        self.score += 1
                        for z in range(self.N):
                            self.freeForX[x,z] = 0;
                            self.freeForX[z,y] = 0;
            elif model == 'o':
                continue
            else:
                raise ValueError( model )    

# handle file input/output and call above algorithm for each case
open( outputFilename, 'w' ) # clear output file
with open(filename, 'r') as f:
    caseCount = int( f.readline().strip() )
    for i in range( 1, caseCount+1 ):
        print('i:', i) # show progress
        data = f.readline().strip().split(' ')
        N = int( data[0] )
        M = int( data[1] )
        if debug:
            print('N:', N)
            print('M:', M)
        myField = Field( N, M )
        for m in range(M):
            data = f.readline().strip().split(' ')
            model = data[0]
            x = int( data[1] ) - 1
            y = int( data[2] ) - 1
            myField.addModel( model, x, y )
        while myField.placePlusOnEdge() == 1:
            pass
        while myField.placeXSomewhere() == 1:
            pass
        myField.finalUpdateCheck()
        with open( outputFilename, 'a' ) as f2:
            outputLine = 'Case #{}: '.format(i) + '{} {}'.format(myField.score, len(myField.history)-myField.M)
            if debug:
                print(outputLine)
            f2.write( outputLine + '\n')
            for i2 in range(myField.M, len(myField.history)):
                h = myField.history[i2]
                f2.write( '{} {} {}\n'.format(h[0],h[1]+1,h[2]+1) )
            
