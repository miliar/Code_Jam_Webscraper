#!/usr/bin/env python3

import sys

if "__main__" == __name__:

    readline = sys.stdin.readline

    for case_number in range( 1, int( readline( ) ) + 1 ):
        
        number_of_blocks = int( readline( ) )

        naomi_blocks = list( sorted( map( float, readline( ).split( ) ) ) )
        ken_w_blocks = list( sorted( map( float, readline( ).split( ) ) ) )
        ken_dw_blocks = list( ken_w_blocks )

        naomi_w_score = 0
        naomi_dw_score = 0

        for trial_number in range( number_of_blocks ):

            # TODO: Optimize.
            kendex = 0
            while naomi_blocks[ 0 ] > ken_w_blocks[ kendex ]:
                kendex += 1
                if kendex >= len( ken_w_blocks ):
                    naomi_w_score += 1
                    ken_w_blocks.pop( 0 )
                    break
            else:
                ken_w_blocks.pop( kendex )

            if naomi_blocks[ 0 ] > ken_dw_blocks[ 0 ]:
                naomi_dw_score += 1
                ken_dw_blocks.pop( 0 )
            else:
                ken_dw_blocks.pop( )

            naomi_blocks.pop( 0 )
            
        print( "Case #{0}: {1} {2}".format(
            case_number, naomi_dw_score, naomi_w_score )
        )

# vim: set syntax=python ts=4 sts=4 sw=4 et tw=79:
