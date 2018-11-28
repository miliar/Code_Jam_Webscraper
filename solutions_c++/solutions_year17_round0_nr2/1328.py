/***************************************************************************
                             problem_b.cpp  -
                             -------------------
    begin                : Sat 08 Apr 2017 01:41:23 CDT
    copyright            : (c) 2017 by Akarsh Simha
    email                : akarsh.simha@kdemail.net
***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/


/* Project Includes */

/* STL Includes */
#include <iostream>
#include <assert.h>
#include <string>

int main() {
    int T;

    std::cin >> T;

    for ( int k = 0; k < T; ++k ) {
        std::string N;
        std::cin >> N;
        int nDigits = N.length();

        auto findFirstViolation = [&N]( int end ) {
            char prev = N[0];
            for ( int j = 1; j < end; ++j ) {
                if ( N[j] < prev )
                    return j;
                prev = N[j];
            }
            return -1;
        };

        auto fixAt = [&N]( int startIndex ) {
            assert( N[startIndex] > '0' );
            N[startIndex] = N[startIndex] - 1;
            for ( int j = startIndex + 1; j < N.length(); ++j )
                N[j]  = '9';
        };

        auto trim = []( const std::string &str ) {
            int j = 0;
            while ( str[j] == '0' )
                ++j;
            return str.substr( j );
        };

        int end = N.length();
        while ( end > 0 ) {
            int j = findFirstViolation( end );
            if ( j < 0 ) {
                std::cout << "Case #" << ( k + 1 ) << ": " << trim( N ) << std::endl;
                break;
            }
            fixAt( j - 1 );
            end = j;
        }
    }
}
