

# TESTING
# inFileTXT = "3 5 4\nabc\nbca\ndac\ndbc\ncba\n(ab)(bc)(ca)\nabc\n(abc)(abc)(abc)\n(zyx)bc"

# first load up the input file, always stored in C:\temp\
inFile = open( "C:\\temp\\A-small-attempt0.in", 'r' )
inFileTXT = inFile.read()
inFile.close()

# and parse it
# first line is L D N
lines = inFileTXT.split( "\n" )
l = lines.pop( 0 )
L = int( l.split( " " )[ 0 ] )
D = int( l.split( " " )[ 1 ] )
N = int( l.split( " " )[ 2 ] )

# next D lines are known words
knownWords = []
for i in range( 0, D ):
    knownWords.append( lines.pop( 0 ) )

# the next N lines are test cases
testWords = []
for i in range( 0, N ):
    testWords.append( lines.pop( 0 ) )

# now the real work!
tNum = 1
for test in testWords:

    # need to take each word and find how many possible matches we have in the known words
    # make a list of all possible words, which will be trimmed as impossibles are determined in comparison to the dict
    # make a copy of our dict to trim as we find possible matches
    possibles = []
    matches = knownWords[:]
    
    # trim while we narrow our choices
    while( len( test ) > 0 ):

        # we start with either a condition ...
        if test[ 0 ] == "(":

            # extract the condition
            c = test[ 0 : test.find( ")" ) ]
            c = c.replace( "(", "" ).replace( ")", "" )
            # trim test here so we don't forget
            test = test[ test.find( ")" ) + 1 : ]
            
            # put these conditionals on the possibles
            p1 = []
            if len( possibles ) == 0:
                for c1 in c:
                    p1.append( c1 )
            else:
                for c1 in c:
                    for p in possibles:
                        p1.append( p + c1 )

            # replace the possibles list
            possibles = p1[:]


        # ... or a fixed sequence
        else:

            # this might end with a fixed sequence, or there might be more conditionals to consider
            if test.find( "(" ) != -1:
                
                # get the whole fixed sequence
                Fseq = test[ : test.find( "(" ) ]
                # trim test here, so we don't forget
                test = test[ test.find( "(" ) : ]

            else:

                Fseq = test
                # trim test here so we don't forget
                test = ""

            # and put the sequence on the possibles
            if len( possibles ) == 0:
                possibles.append( Fseq )
            else:
                for p in possibles:
                    p = p + Fseq


        # now we need to compare out possibles to the dict to filter any mathes this possibles cannot be\
        i = 0
        while i < len( matches ):

            dictKeep = False
            for p in possibles:

                # if there is a possible staritng combination that could be this dict word, keep it in the matches
                if matches[ i ].find( p ) == 0:
                    dictKeep = True
                    break

            if not dictKeep:
                matches.pop( i )
            else:
                i = i + 1


        # also filter the possibles to match what could be shown in the dict
        # to cut down on the possible size of the possibles list
        i = 0
        while i < len( possibles ):

            possKeep = False
            for d in matches:

                # if there is a possible staritng combination that could be this dict word, keep it in the matches
                if d.find( possibles[ i ] ) == 0:
                    possKeep = True
                    break

            if not possKeep:
                possibles.pop( i )
            else:
                i = i + 1

        
    # now we have our number, output
    outFile = open( "C:\\temp\\A-small-attempt0.out", 'a' )
    outFile.write( "Case #" + str( tNum ) + ": " + str( len( matches ) ) + "\n" )
    outFile.close()
    tNum = tNum + 1

















                    

                
