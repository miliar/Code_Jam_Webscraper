import sys

inputFile = open( "input.in" )
outputFile = open( "output.out", "w" )

lineCount = int( inputFile.readline() )

for i in range( lineCount ):

    line = inputFile.readline()

    result = []

    charCount = len( line )
    for j in range( charCount ):
        if line[ j ] == " ":
            result.append( " " )
        elif line[ j ] == "a":
            result.append( "y" )
        elif line[ j ] == "b":
            result.append( "h" )
        elif line[ j ] == "c":
            result.append( "e" )
        elif line[ j ] == "d":
            result.append( "s" )
        elif line[ j ] == "e":
            result.append( "o" )
        elif line[ j ] == "f":
            result.append( "c" )
        elif line[ j ] == "g":
            result.append( "v" )
        elif line[ j ] == "h":
            result.append( "x" )
        elif line[ j ] == "i":
            result.append( "d" )
        elif line[ j ] == "j":
            result.append( "u" )
        elif line[ j ] == "k":
            result.append( "i" )
        elif line[ j ] == "l":
            result.append( "g" )
        elif line[ j ] == "m":
            result.append( "l" )
        elif line[ j ] == "n":
            result.append( "b" )
        elif line[ j ] == "o":
            result.append( "k" )
        elif line[ j ] == "p":
            result.append( "r" )
        elif line[ j ] == "q":
            result.append( "z" )
        elif line[ j ] == "r":
            result.append( "t" )
        elif line[ j ] == "s":
            result.append( "n" )
        elif line[ j ] == "t":
            result.append( "w" )
        elif line[ j ] == "u":
            result.append( "j" )
        elif line[ j ] == "v":
            result.append( "p" )
        elif line[ j ] == "w":
            result.append( "f" )
        elif line[ j ] == "x":
            result.append( "m" )
        elif line[ j ] == "y":
            result.append( "a" )
        elif line[ j ] == "z":
            result.append( "q" )

    outputFile.write( "Case #" )
    outputFile.write( str(i+1) )
    outputFile.write( ": " )
    outputFile.write( "".join(result) )

    if i < lineCount -1:
        outputFile.write( "\n" )

inputFile.close()
outputFile.close()
