#include <iostream>
#include <map>
#include <string>

using namespace std;

void fillB( string *b, int r, int c, int *r_fill, char *r_first )
{
    // two pass: 1st pass from top to bottom, 2nd pass from bottom to top
    // 1st pass
    for ( int i = 0; i < r; ++i ) {

        if ( i != 0 && r_fill[i] == c ) { // empty row, copy previous row
            b[ i ] = b[ i - 1 ];
        } else {
            // fill based on config
            char fillC = r_first[ i ];
            for ( int j = 0; j < c; ++j ) {
                if ( b[ i ][ j ] == fillC ||
                     b[ i ][ j ] == '?' ) {
                    b[ i ][ j ] = fillC;
                } else {
                    fillC = b[ i ][ j ];
                }
            }
            r_fill[ i ] = 0;
        }
    }

    // 2nd pass
    for ( int i = r - 2; i >= 0; --i ) {
        bool containQ = false;
        for ( int j = 0; j < c; ++j ) {
            if ( b[ i ][ j ] == '?' ) {
                containQ = true;
                break;
            }
        }

        if ( containQ ) { // empty row, copy previous row
            b[ i ] = b[ i + 1 ];
        }
    }
}

int main( int argc, char *argv[] )
{
    int t;
    cin >> t;

    int r, c;
    string b[ 26 ];

    int r_fill[ 26 ];   // # of place for row to fill
    char r_first[ 26 ];  // first char of a row

    for ( int i = 0; i < t; ++i ) {

        // input
        cin >> r >> c;
        for ( int j = 0; j < r; ++j ) {
            cin >> b[ j ];

            r_fill[ j ] = 0;
            r_first[ j ] = '?';

            for ( int k = 0; k < c; ++k ) {
                if ( r_first[ j ] == '?' && b[ j ][ k ] != '?' ) {
                    r_first[ j ] = b[ j ][ k ];
                }
                if ( b[ j ][ k ] == '?' ) {
                    r_fill[ j ]++;
                }
            }
        }

        // process
        fillB( b, r, c, r_fill, r_first );

        // output
        cout << "Case #" << i + 1 << ": ";


        cout << endl;
        for ( int j = 0; j < r; ++j ) {
            cout << b[ j ] << endl;
        }
    }
    return 0;
}