/***************************************************************************
                             problem_a.cpp  -
                             -------------------
    begin                : Fri 14 Apr 2017 19:53:27 CDT
    copyright            : (c) 2017 by Akarsh Simha
    email                : akarsh.simha@kdemail.net
 ***************************************************************************/


/* STL Includes */
#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <assert.h>
#include <utility>
#include <limits>
#include <tuple>
#include <functional>

int main() {
    unsigned int T;
    std::cin >> T;
    for ( int t = 0; t < T; ++t ) {
        std::cout << "Case #" << ( t + 1 ) << ":" << std::endl;

        int R, C;
        std::cin >> R;
        std::cin >> C;
        std::vector<std::vector<char>> cake( R, std::vector<char>( C, '?' ) );
        std::vector<std::vector<bool>> processed( R, std::vector<bool>( C, false ) );
        for ( int r = 0; r < R; ++r )
            for ( int c = 0; c < C; ++c ) {
                char cakeEntry;
                std::cin >> cakeEntry;
                cake[r][c] = cakeEntry;
            }

        // Greedy
        auto spreadRow = [&cake, R, C, &processed]( int r, int c ) {
            assert( 0 <= r && r < R );
            assert( 0 <= c && c < C );
            char initial = cake[r][c];
            int k = r - 1;
            processed[r][c] = true;
            while ( k >= 0 && cake[k][c] == '?' )
                ( processed[k][c] = true, cake[k--][c] = initial );
            k = r + 1;
            while ( k < R && cake[k][c] == '?' )
                ( processed[k][c] = true, cake[k++][c] = initial );
        };


        auto spreadCol = [&cake, R, C,  &processed]( int r, int c ) {
            assert( 0 <= r && r < R );
            assert( 0 <= c && c < C );
            char initial = cake[r][c];
            int k = c - 1;
            processed[r][c] = true;
            while ( k >= 0 && cake[r][k] == '?' )
                ( processed[r][k] = true, cake[r][k--] = initial );
            k = c + 1;
            while ( k < C && cake[r][k] == '?' )
                ( processed[r][k] = true, cake[r][k++] = initial );
        };


        for ( int r = 0; r < R; ++r ) {
            for ( int c = 0; c < C; ++c ) {
                if ( cake[r][c] == '?' || processed[r][c] )
                    continue;
                /*
                if ( ( r > 0 && cake[r - 1][c] == '?' ) || ( r != R - 1 && cake[R - 1][c] == '?' ) ) {
                    spreadRow( r, c );
                }
                else
                    spreadCol( r, c );
                */
                spreadCol( r, c );
            }
        }

        // Process ? rows
        for ( int r = 0; r < R; ++r ) {
            if ( cake[r][0] == '?' ) {
                // ? row
                for ( int c = 0; c < C; ++c ) {
                    assert( cake[r][c] == '?' );
                }
                if ( r != 0 ) {
                    for ( int c = 0; c < C; ++c )
                        cake[r][c] = cake[r - 1][c];
                }
                else {
                    // find subsequent non-? row
                    int rp = 0;
                    while ( cake[rp][0] == '?' ) {
                        assert( ++rp < R );
                    }
                    for ( int c = 0; c < C; ++c )
                        cake[r][c] = cake[rp][c];
                }
            }
        }

/*
        std::function<bool( int r, int c, std::vector<std::vector<char>> state )> recurse
            = [R, C]( int r, int c, std::vector<std::vector<char>> state ) -> bool {
        };
*/

        bool success = true;
        for ( int r = 0; r < R; ++r ) {
            for ( int c = 0; c < C; ++c ) {
                if ( cake[r][c] == '?' )
                    success = false;
                std::cout << cake[r][c];
            }
            std::cout << std::endl;
        }
        assert( success );

    }
}
