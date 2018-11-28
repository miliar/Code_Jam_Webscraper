#!/usr/bin/env python3

import sys

if "__main__" == __name__:
    
    readline = sys.stdin.readline

    cases_count = int( readline( ) )

    for case_number in range( cases_count ):

        answer1 = int( readline( ) ) - 1
        matrix1 = [ ]

        for row_number in range( 4 ):
            
            row = readline( )
            matrix1.append( map( int, row.split( ) ) )
        
        set1 = set( matrix1[ answer1 ] )

        answer2 = int( readline( ) ) - 1
        matrix2 = [ ]

        for row_number in range( 4 ):
            
            row = readline( )
            matrix2.append( map( int, row.split( ) ) )
        
        set2 = set( matrix2[ answer2 ] )

        intersection = set1.intersection( set2 )

        if 0 == len( intersection ):
            print( "Case #{0}: Volunteer cheated!".format( case_number + 1 ) )
        elif 1 == len( intersection ):
            print( "Case #{0}: {1}".format( case_number + 1, intersection.pop( ) ) )
        else:
            print( "Case #{0}: Bad magician!".format( case_number + 1 ) )

# vim: set syntax=python ts=4 sts=4 sw=4 et tw=79:
