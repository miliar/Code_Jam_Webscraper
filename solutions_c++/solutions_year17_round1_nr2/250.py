
#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
    int T;
    std::cin >> T;
    for ( int testID = 1 ; testID <= T ; ++testID ) {

        int numIngredients;
        int numPackages;
        std::cin >> numIngredients >> numPackages;

        std::vector<double> cost( numIngredients );
        for ( int i = 0 ; i < numIngredients ; ++i )
            std::cin >> cost[ i ];

        std::vector< std::vector<int> > dat( numIngredients , std::vector<int>( numPackages ) );
        for ( int i = 0 ; i < numIngredients ; ++i ) {
            for ( int j = 0 ; j < numPackages ; ++j )
                std::cin >> dat[ i ][ j ];
            std::sort( dat[i].begin() , dat[i].end() );
        }

        // vector of pointers for traversing each package.
        std::vector<int> idx( numIngredients , 0 );
        int targetServings = 1;
        int out = 0;

        int done = false;
        while ( true ) {
            for ( int i = 0 ; i < numIngredients ; ++i ) {
                // while we don't have enough of this ingredient...
                double min = targetServings * cost[i] * 0.9;
                while ( idx[i] < numPackages && dat[ i ][ idx[i] ] < min )
                    ++idx[i];
                if ( idx[i] == numPackages ) {
                    done = true;
                    break;
                }
            }
            if ( done )
                break;
            bool usable = true;
            for ( int i = 0 ; i < numIngredients ; ++i ) {
                if ( dat[ i ][ idx[i] ] > targetServings * cost[i] * 1.1 ) {
                    usable = false;
                    break;
                }
            }

            if ( usable ) {
                ++out;
                for ( int i = 0 ; i < numIngredients ; ++i ) {
                    ++idx[i];
                    if ( idx[i] == numPackages ) {
                        done = true;
                        break;
                    }
                }
            } else {
                ++targetServings;
            }
            if ( done )
                break;
        }
        
        std::cout << "Case #" << testID << ": " << out << '\n';
    }
    return 0;
}
