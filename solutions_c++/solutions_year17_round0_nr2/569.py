
#include <iostream>
#include <string>

typedef long long ll;

int main()
{
    int T;
    std::cin >> T;

    for ( int testID = 1 ; testID <= T ; ++testID ) {
        std::string dat;
        std::cin >> dat;
        std::cout << "Case #" << testID << ": ";

        int N = dat.size();

        // find the first slot where the digits decrease.
        int firstDecrease = -1;
        for ( int i = 0 ; i < N-1 ; ++i ) {
            if ( dat[i] > dat[i+1] ) {
                firstDecrease = i;
                break;
            }
        }

        if ( firstDecrease == -1 ) {
            std::cout << dat << '\n';
            continue;
        }

        // Now go back and find the closest place that isn't a tie.
        int closestNonTie = firstDecrease-1;
        while ( closestNonTie >= 0 && dat[ closestNonTie ] == dat[ firstDecrease ] )
            --closestNonTie;

        --dat[ closestNonTie + 1 ];
        for ( int i = closestNonTie + 2 ; i < N ; ++i )
            dat[ i ] = '9';

        // watch out for leading 0s.
        // No need to do anything fast here.
        int firstChar = 0;
        if ( dat[ firstChar ] == '0' )
            ++firstChar;

        for ( int i = firstChar ; i < N ; ++i )
            std::cout << dat[i];
        std::cout << '\n';
    }

    return 0;
}
