/***************************************************************************
                             problem_b.cpp  -
                             -------------------
    begin                : Fri 14 Apr 2017 19:55:23 CDT
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
#include <cmath>

int main() {
    unsigned int T;
    std::cin >> T;
    for ( int t = 0; t < T; ++t ) {
        std::cout << "Case #" << ( t + 1 ) << ": ";

        // Code begins below
        int N, P;
        std::cin >> N;
        std::cin >> P;

        std::vector<int> R;
        R.reserve( N );
        for ( int i = 0; i < N; ++i ) {
            int Ri;
            std::cin >> Ri;
            R.push_back( Ri );
        }

        std::vector<std::vector<int>> Q( N, std::vector<int>( P, 0 ) );
        for ( int i = 0; i < N; ++i )
            for ( int k = 0; k < P; ++k ) {
                std::cin >> Q[i][k];
            }

        std::set<std::vector<int>> valid;
        std::vector<int> current;
        current.reserve( N );

        std::function<void( int, int )> findValid = [&findValid, &current, &valid, &P, &Q, &R]( int ingredient, int servings ) -> void {
            if ( ingredient >= R.size() ) {
                valid.insert( current );
                return;
            }

            if ( ingredient == 0 ) {
                for ( int j = 0; j < P; ++j ) {
                    double fracServings = double( Q[0][j] )/double( R[0] );
                    int maxServings = std::floor( double( Q[0][j] )/double( 0.90 * R[0] ) );
                    int minServings = std::ceil( double( Q[0][j] )/double( 1.10 * R[0] ) );
                    for ( int n = minServings; n <= maxServings; ++n ) {
                        current.push_back( j );
                        findValid( 1, n );
                        current.pop_back();
                    }
                }
            }
            else {
                for ( int j = 0; j < P; ++j ) {
                    const int n = servings;
                    if ( Q[ ingredient ][j] >= 0.90 * n * R[ ingredient ] && Q[ ingredient ][j] <= 1.10 * n * R[ ingredient ] ) {
                        current.push_back( j );
                        findValid( ingredient + 1,  n );
                        current.pop_back();
                    }
                }
            }
        };

        findValid( 0, 0 );

        std::vector<std::vector<int>> validVector;
        validVector.reserve( valid.size() );
        for ( const auto &x : valid )
            validVector.push_back( x );

        /*
        std::cerr << "Found " << validVector.size() << " combinations." << std::endl;
        for ( int k = 0; k < 10 && k < validVector.size(); ++k ) {
            for ( int j = 0; j < validVector[k].size(); ++j )
                std::cerr << "  " << validVector[k][j];
            std::cerr << std::endl;
        }
        */

        std::vector<std::vector<bool>> used( N, std::vector<bool>( P, false ) );

        int max = 0;
        std::function<int( int, int )> findMax = [&findMax, &validVector, N, &used]( int startIndex, int usedSoFar ) {
            int max = usedSoFar;
            for ( int i = startIndex; i < validVector.size(); ++i ) {
                bool usable = true;
                for ( int j = 0; j < N; ++j )
                    if ( used[j][validVector[i][j]] ) {
                        usable = false;
                        break;
                    }
                if ( !usable )
                    continue;
                for ( int j = 0; j < N; ++ j )
                    used[j][validVector[i][j]] = true;
                int altMax = findMax( i + 1, usedSoFar + 1 );
                if ( altMax > max )
                    max = altMax;
                for ( int j = 0; j < N; ++j )
                    used[j][validVector[i][j]] = false;
            }
            return max;
        };

        std::cout << findMax( 0, 0 ) << std::endl;
    }
}
