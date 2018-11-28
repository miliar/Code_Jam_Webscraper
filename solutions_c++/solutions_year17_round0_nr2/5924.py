#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool isTidy( long long int x )
{
    bool isTidy = true;
    int curBit;
    int preBit = x % 10;
    x /= 10;
    while ( x ) {
        curBit = x % 10;
        if ( curBit > preBit ) {
            isTidy = false;
            break;
        }
        preBit = curBit;
        x /= 10;
    }
    return isTidy;
}

vector< int > toVec( long long int x )
{
    vector< int > xdigits;
    while ( x ) {
        xdigits.push_back( x % 10 );
        x /= 10;
    }
    return xdigits;
}

long long int tidyNum( long long int x )
{

    vector< int > xdigits = toVec( x );

    while ( !isTidy( x ) ) {
        // find first untidy digit
        int t = xdigits.size() - 1;
        while ( t > 0 && xdigits[ t ] <= xdigits[ t - 1 ] ) {
            t--;
        }
        // update x
        if ( t != 0 ) {
            int tmp = t;
            while ( tmp-- ) {
                x /= 10;
            }
            //x--;
            tmp = t;
            while ( tmp-- ) {
                x *= 10;
            }
            x--;
        }
        // to string
        xdigits = toVec( x );
    }
    return x;
}

int main( int argc, char *argv[] )
{
    int t;
    long long int x;
    cin >> t;
    for ( int i = 0; i < t; ++i ) {
        cin >> x;
        //cout << sizeof( x ) << " " << x << endl;

        cout << "Case #" << i + 1 << ": " << tidyNum( x ) << endl;
    }
    return 0;
}