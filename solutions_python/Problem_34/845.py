class Pro1:
    L = 0
    D = 0
    N = 0
    
    checkprecount = 2
    
    words = []
    testcases = []
    #chfliter = []
    #fliter1chs = ""
    #fliter2chs = ""

    singlechfilter = []
    prefilters = []
    
    def InitFilters( self ):
        fliterxchs = ""
       
        if self.L >=2:
            for i in range( 2, self.L ):
                fliterxchs = ""
                for word in self.words:
                    fliterxchs = fliterxchs + "#" + word[ 0 : i ]
                self.prefilters.append( fliterxchs )
        print self.prefilters, "\n"
        
        for i in range( 0, self.L ):
            filter1ch = ""
            for word in self.words:
                filter1ch = filter1ch + word[ i ]
            self.singlechfilter.append( filter1ch )
            
    def FilterSingletCh( self, tokens ):
        newtokens = []
        for i in range( 0, self.L ):
            newtoken = ""
            for c in tokens[ i ]:
                if self.singlechfilter[ i ].find( c ) != -1:
                    newtoken = newtoken + c
            if len( newtoken ) == 0:
                return None
            newtokens.append( newtoken )
        return newtokens;
    
    def FilterPreCh( self, pre ):
        prefilter = self.prefilters[ len( pre ) - 2 ]
        return prefilter.find( "#" + pre ) != -1
    
    
     
    def ParseInputFile( self ):
        inputfile = open( "A-small-attempt1.in", "r" )
        firstline = inputfile.readline()
        data = firstline.split()
        self.L = int( data[ 0 ] )
        self.D = int( data[ 1 ] )
        self.N = int( data[ 2 ] )
        for i in range( 0, pro.D ):
            self.words.append( inputfile.readline()[ : self.L ] )
        self.words.sort()
        for i in range( 0, pro.N ):
            self.testcases.append( inputfile.readline() )

        self.checkprecount = self.L
        self.InitFilters()
        
        
            
    #def InitChFliter( self ):
        #for word in self.word:
            #self.fliter1chs.append( word[ 0 ] )
            #self.fliter2chs.append( word[ 0 : 2 ] )
        
    def ParseTestCase( self, case ):
        tokens = []
        i = 0;
        while i < len( case ) and len( tokens ) < self.L:
            if case[ i ] != "(":
                tokens.append( case[ i ] )
            else:
                start = i + 1
                while case[ i ] != ")":
                    i = i + 1
                tokens.append( case[ start : i ] )
            i = i + 1
        return tokens
    
    def GeneratePatternsWith( self, tokens ):
        if not self.FilterTokens1Chs( tokens ):
            return None;
        patterns = [];
        subpatterns = [];
        mergedpattern = [];
        i = 0
        for i in range( 0, len( tokens[ 0 ] ) ):
            if self.chfliter[ self.L - len( tokens ) ].find( tokens[ 0 ][ i ] ):
                patterns.append( tokens[ 0 ][ i ] )
        if len( patterns ) == 0:
            return None;
        if len( tokens ) > 1:
            subpatterns = self.GeneratePatternsWith( tokens[ 1 : ] )
        if subpatterns == None:
            return None
        if len( subpatterns ) > 1:
            for n0 in patterns:
                for n1 in subpatterns:
                    mergedpattern.append( n0 + n1 )
            return mergedpattern
        else:
            return patterns
                   
    
    #def FilterTokens1Chs( self, s ):
        #return self.fliter1chs.find( s ) != -1
        
    #def FilterToken2Chs( self, s ):
        #s = "#" + token
        #return self.fliter2chs.find( s ) != -1
            
    def CalcCasePattern( self, case ):
        patterns = []
        tokens = self.ParseTestCase( case )
        
        #check the every character at first
        tokens = self.FilterSingletCh( tokens )
        if tokens == None:
            return 0
        
        #patterns  = self.GeneratePatternsWith( tokens )
        patterns = self.GeneratePatterns2( tokens )
        
        if patterns == None:
            return 0
        pattersinwordscount = 0
        for s in patterns:
            if self.FindWord( s ):
                pattersinwordscount = pattersinwordscount + 1
        return pattersinwordscount
    
    def FindWord( self, pattern ):
        for s in self.words:
            if s == pattern:
                return True
        return False
    
    def DoCacl( self ):
        outputfile = open( "output", "w" )
        i = 1
        for case in self.testcases:
            count = 0
            count = self.CalcCasePattern( case )
            outputfile.write( "Case #" + str( i ) + ": " + str( count ) + "\n" )
            i = i + 1
            

    
    def GeneratePatterns2( self, tokens, pre = "" ):
        #print "Pre: " + pre
        patterns = []
        if len( tokens ) == 1:
            for c in tokens[ 0 ]:
                patterns.append( c )
            return patterns
        
        subpattern = []
        mergedpattern = []
               
        for c in tokens[ 0 ]:
            pattern = c
            if len( pre + c ) < self.checkprecount and len( pre + c ) > 1 and ( not self.FilterPreCh( pre + c ) ):
                continue
            subpattern = self.GeneratePatterns2( tokens[ 1 : ], pre + c )
            if len( subpattern ) > 0:
                sp = ""
                for sp in subpattern:
                    patterns.append( c + sp )
                    print patterns
        
        return patterns

            

pro = Pro1()
pro.ParseInputFile()
pro.DoCacl()