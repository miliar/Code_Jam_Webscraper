
#include <iostream>
#include <string>
#include <vector>
#include <string>

int main()
{
    int T;
    std::cin >> T;
    for ( int testID = 1 ; testID <= T ; ++testID ) {
        std::cout << "Case #" << testID << ":\n";

        int R;
        int C;
        std::cin >> R >> C;

        std::vector< std::string > dat;
        for ( int i = 0 ; i < R ; ++i ) {
            std::string row;
            std::cin >> row;
            dat.push_back( row );
        }

        // solve each row separately.
        std::vector<int> todoLater;
        std::vector<int> done;
        for ( int r = 0 ; r < R ; ++r ) {
            // is there anything in this row?
            int empty = true;
            int firstNonempty = 0;
            for ( ; firstNonempty < C ; ++firstNonempty )
                if ( dat[ r ][ firstNonempty ] != '?' ) {
                    empty = false;
                    break;
                }
            if ( firstNonempty == C ) {
                todoLater.push_back( r );
                continue;;
            } else {
                done.push_back( r );
            }
            for ( int c = 0 ; c < firstNonempty ; ++c )
                dat[ r ][ c ] = dat[ r ][ firstNonempty ];

            int mostRecentNonempty = firstNonempty;
            int curr = firstNonempty + 1;
            while ( curr < C ) {
                if ( dat[ r ][ curr ] != '?' )
                    mostRecentNonempty = curr;
                else
                    dat[ r ][ curr ] = dat[ r ][ mostRecentNonempty ];

                ++curr;
            }
        }

        // now go back and fill in the rows that were empty.
        if ( todoLater.size() > 0 ) {
            // first do all rows before the first nonempty one.
            for ( int r = 0 ; r < done[ 0 ] ; ++r )
                dat[ r ] = dat[ done[0] ];

            // Now just fill in based on most recent row we saw.
            done.push_back( R );
            for ( int i = 0 ; i < done.size() - 1 ; ++i ) {
                // fill in the rows between done[i] and done[i+1].
                for ( int r = done[i] + 1 ; r < done[ i+1 ] ; ++r )
                    dat[ r ] = dat[ done[i] ];
            }
        }

        for ( int r = 0 ; r < R ; ++r )
            std::cout << dat[ r ] << '\n';            
    }
    return 0;
}
