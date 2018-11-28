#!/usr/bin/python
# -*- coding: utf-8 -*-

#Created on 07.05.2011
#
#@author: pavlo


import os


class Combine( ):
    base = [ ];
    result = '';
    
    def __init__( self, base = [ ], result = '' ):
        self.base = base;
        self.result = result;
        
        
class Opposoties( ):
    el = [ ];
    
    def __init__( self, elements = [ ] ):
        self.el = elements;


inputFile = open( os.path.join( os.path.dirname( __file__ ), 'B-large.in' ) );
outputFile = open( os.path.join( os.path.dirname( __file__ ), 'output.txt' ), 'w' );
numCases = int( inputFile.readline( ) );
for case in range( numCases ):
    inputLine = inputFile.readline( ).split( ' ' );
    combinesCount = int( inputLine[ 0 ] );
    combines = [ ];
    if combinesCount != 0:
        for i in range( combinesCount ):
            combines.append( Combine( base = [ inputLine[ i + 1 ][ 0 ], inputLine[ i + 1 ][ 1 ] ], result = inputLine[ i + 1 ][ 2 ] ) );
    oppositiesCount = int( inputLine[ combinesCount + 1 ] );
    opposities = [ ];
    if oppositiesCount != 0:
        for i in range( oppositiesCount ):
            opposities.append( Opposoties( elements = [ inputLine[ combinesCount + 2 + i ][ 0 ], inputLine[ combinesCount + 2 + i ][ 1 ] ] ) );
    elementsLength = int( inputLine[ combinesCount + oppositiesCount + 2 ] );
    elements = [ ];
    for i in range( elementsLength ):
        elements.append( inputLine[ combinesCount + oppositiesCount + 3 ][ i ] );
        count = len( elements );
        for j in range( count ):
            if j == count - 1:
                break;
            stopCombine = True;
            for comb in combines:
                if comb.base[ 0 ] == comb.base[ 1 ]:
                    if elements[ count - j - 1 ] in comb.base and elements[ count - j - 2 ] in comb.base:
                        elements.pop( );
                        elements.pop( );
                        elements.append( comb.result );
                        stopCombine = False;
                        break;
                else:
                    if elements[ count - j - 1 ] in comb.base and elements[ count - j - 2 ] in comb.base and elements[ count - j - 1 ] != elements[ count - j - 2 ]:
                        elements.pop( );
                        elements.pop( );
                        elements.append( comb.result );
                        stopCombine = False;
                        break;
            if stopCombine:
                break;
        for j in range( len( elements ) ):
            stopEmpty = False;
            if j == count - 1:
                break;
            for opp in opposities:
                if opp.el[ 0 ] == opp.el[ 1 ]:
                    if elements[ j ] in opp.el and elements[ len( elements ) - 1 ] in opp.el:
                        del elements[:];
                        stopEmpty = True;
                        break;
                else:
                    if elements[ j ] in opp.el and elements[ len( elements ) - 1 ] in opp.el and elements[ j ] != elements[ len( elements ) - 1 ]:
                        del elements[:];
                        stopEmpty = True;
                        break;
            if stopEmpty:
                break;
      
    output = '[';
    for i in range( len( elements ) ):
        if i != len( elements ) - 1:
            output += elements[ i ] + ', ';
        else:
            output += elements[ i ];
    output += ']';         
    outputFile.write( 'Case #%s: %s\n' % ( str( case + 1 ), output ) );