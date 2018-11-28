/***************************************************************************
                             problem_c.cpp  -
                             -------------------
    begin                : Sat 08 Apr 2017 02:59:16 CDT
    copyright            : (c) 2017 by Akarsh Simha
    email                : akarsh.simha@kdemail.net
***************************************************************************/

/* Project Includes */

/* STL Includes */
#include <iostream>
#include <queue>
#include <assert.h>

int main() {
    int T;
    std::cin >> T;
    typedef std::pair<unsigned long, unsigned long> split_t;
    auto split = []( unsigned long n ) -> split_t {
        if ( n == 1 )
            return split_t( 0, 0 );
        if ( ( n - 1 )%2 == 0 ) {
            return split_t( ( n - 1 )/2, ( n - 1 )/2 );
        }
        else
            return split_t( ( n - 1 )/2 + 1, ( n - 1 )/2 );
    };
    for ( int t = 0; t < T; ++t ) {
        unsigned long N, K;
        std::cin >> N;
        std::cin >> K;
        std::cout << "Case #" << ( t + 1 ) << ": ";

        // Handle trivial edge case
        if ( N == K ) {
            std::cout << "0 0" << std::endl;
            continue;
        }
        if ( K == 1 ) {
            auto s = split( N );
            std::cout << s.first << " " << s.second << std::endl;
                                                       continue;
        }

        unsigned long pow2 = 1;
        unsigned long power = 0;
        while ( 2 * pow2 - 1 < K ) {
            pow2 = 2 * pow2;
            ++power;
        }

        unsigned long splitCount = pow2;
        unsigned long availableSlots = N - ( splitCount - 1 );
        unsigned long shortIntervalSize = ( availableSlots / splitCount );
        unsigned long longIntervalCount = availableSlots - shortIntervalSize * splitCount;
        unsigned long shortIntervalCount = splitCount - longIntervalCount;
        split_t s;
        assert( K >= splitCount );
        if ( K - ( splitCount - 1 ) <= longIntervalCount )
            s = split( shortIntervalSize + 1 );
        else
            s = split( shortIntervalSize );
        std::cout << s.first << " " << s.second << std::endl;
    }
}
