'''
Created on 22.05.2011

@author: pavlo
'''


import os

inputFile = open( os.path.join( os.path.dirname( __file__ ), 'A-large.in' ) );
outputFile = open( os.path.join( os.path.dirname( __file__ ), 'output.txt' ), 'w' );

numCases = int( inputFile.readline( ) );

for case in range( numCases ):
    caseInput = inputFile.readline(  ).split( ' ' );
    pictureHeight = int( caseInput[ 0 ] );
    pictureWidth = int( caseInput[ 1 ] );
    picture = [ ];
    for i in range( pictureHeight ):
        picture.append( list( inputFile.readline( ) ) );
    imposible = False;
    for i in range( pictureHeight - 1 ):
        for j in range( pictureWidth - 1 ):
            if picture[ i ][ j ] == '#':
                if picture[ i + 1 ][ j ] == '#' and picture[ i ][ j + 1 ] == '#' and picture[ i + 1 ][ j + 1 ] == '#':
                    picture[ i ][ j ] = '/';
                    picture[ i ][ j + 1 ] = '\\';
                    picture[ i + 1 ][ j ] = '\\';
                    picture[ i + 1 ][ j + 1 ] = '/';
                    continue;
                else:
                    imposible = True;
    for i in range( pictureHeight ):
        for j in range( pictureWidth ):
            if picture[ i ][ j ] == '#':
                imposible = True;
                break;
    print picture;
    if imposible:
        outputFile.write( 'Case #%s:\nImpossible\n' % str( case + 1 ) );
    else:
        outputFile.write( 'Case #%s:\n' % str( case + 1 ) );
        for i in range( pictureHeight ):
            for j in range( pictureWidth ):
                outputFile.write( picture[ i ][ j ] );
            outputFile.write( '\n' );