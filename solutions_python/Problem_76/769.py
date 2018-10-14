#!/usr/bin/python
# -*- coding: utf-8 -*-

#Created on 07.05.2011
#
#@author: pavlo


import os


def decToBin( n ):
    if n == 0: 
        return '';
    else:
        return decToBin( n / 2 ) + str( n % 2 );


def sum( first = '', second = '' ):
    first = first[ ::-1 ];
    second = second[ ::-1 ];
    if len( first ) > len( second ):
        second += '0' * ( len( first ) - len( second ) );
    else:
        if len( first ) != len( second ):
            first += '0' * ( len( second ) - len( first ) );
    result = '';
    for i in range( len( first ) ):
        if first[ i ] == second[ i ]:
            result += '0';
        else:
            result += '1';
    return result[ ::-1 ].lstrip( '0' );


inputFile = open( os.path.join( os.path.dirname( __file__ ), 'C-large.in' ) );
outputFile = open( os.path.join( os.path.dirname( __file__ ), 'output.txt' ), 'w' );
numCases = int( inputFile.readline( ) );
for case in range( numCases ):
    numCandies = int( inputFile.readline( ) );
    candies = [ ];
    candiesValues = inputFile.readline( ).split( ' ' );
    for j in range( numCandies ):
        candies.append( int( candiesValues[ j ] ) );
    candies.sort( reverse = True );
    answer = '';
    candiesBin = [ ];
    maxIndex = 0;
    for c in candies:
        candiesBin.append( decToBin( c ) );
        if len( decToBin( c ) ) > maxIndex:
            maxIndex = len( decToBin( c ) );
    print candiesBin;
    for i in range( maxIndex ):
        iCount = 0;
        for c in candiesBin:
            if len( c ) < i + 1:
                continue;
            if c[ len( c ) - i - 1 ] == '1':
                iCount += 1;
        if not iCount % 2 == 0:
            answer = 'NO';
            break;
    totalSum = 0;
    if not answer == 'NO':
        for i in range( len( candies ) ):
            if i != len( candies ) - 1:
                totalSum += candies[ i ];
        answer = str( totalSum );
    else:
        answer = 'NO';     
    print answer;
    outputFile.write( 'Case #%s: %s\n' % ( str( case + 1 ), answer ) );