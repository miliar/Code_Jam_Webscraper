#include <iostream>
#include <string>

using namespace std;

int flipCake( const string &s, int w )
{
    string scopy = s;
    int res = 0;
    // scan from left to right and eliminate all '-'
    for ( size_t i = 0; i < scopy.size(); ++i ) {
        if ( scopy[ i ] == '-' ) {
            if ( i + w > s.size() ) {
                res = -1; // failed
                break;
            } else {
                res++;  // flip
                for ( int j = 0; j < w; ++j ) {
                    if ( scopy[ i + j ] == '+' ) {
                        scopy[ i + j ] = '-';
                    } else {
                        scopy[ i + j ] = '+';
                    }
                }
            }
        }
    }
    return res;
}

int main( int argc, char *argv[] )
{
    int t;
    string s;
    int w;
    cin >> t;
    for ( int i = 0; i < t; ++i ) {
        cin >> s >> w;
        //cout << s << " " << w << " ";
        int res = flipCake( s, w );
        if ( res < 0 ) {
            cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
        } else {
            cout << "Case #" << i + 1 << ": " << res << endl;
        }
    }
    return 0;
}