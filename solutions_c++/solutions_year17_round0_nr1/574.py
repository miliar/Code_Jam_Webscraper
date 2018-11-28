
#include <iostream>
#include <string>
#include <vector>

int main()
{
    int T;
    std::cin >> T;
    for ( int testID = 1 ; testID <= T ; ++testID ) {

        std::string datStr;
        std::cin >> datStr;
        int k;
        std::cin >> k;

        int N = datStr.size();
        std::vector<bool> dat( N , 0 );
        for ( int i = 0 ; i < N ; ++i )
            if ( datStr[ i ] == '+' )
                dat[ i ] = 1;


        int flips = 0;

        for ( int start = 0 ; start + k <= N ; ++start ) {
            if ( dat[ start ] == 0 ) {
                // need to flip starting at "start".
                ++flips;
                for ( int i = 0 ; i < k ; ++i )
                    dat[ start+i ] = !dat[ start+i ];
            }
        }
        // the remaining slots had better just be fine already or else there's no hope.
        bool ok = true;
        for ( int start = N - k ; start < N ; ++start )
            if ( dat[ start ] == 0 ) {
                ok = false;
                break;
            }

        std::cout << "Case #" << testID << ": ";
        if ( ok )
            std::cout << flips;
        else
            std::cout << "IMPOSSIBLE";
        std::cout << '\n';
    }
    return 0;
}
