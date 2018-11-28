#include <iostream>
#include <fstream>

using namespace std;

int main( int argc, char** argv )
{
    if ( argc < 2 ) {
        cout << "NG\n";
        return 0;
    }

    ifstream fin( argv[ 1 ] );
    ofstream fout( "A.out" );

    int T;
    fin >> T;
    for ( int testNum = 1; testNum <= T; ++testNum ) {
        fout << "Case #" << testNum << ": ";

        string s;
        fin >> s;
        int k;
        fin >> k;

        int cntr = 0;

        for ( int i = 0; i <= s.size() - k; ++i ) {
            if ( s[ i ] == '-' ) {
                ++cntr;
                for ( int j = i; j < i + k; ++j ) {
                    s[ j ] = s[ j ] == '+' ? '-' : '+';
                }
            }
        }

        bool isPossible = true;
        for ( int i = s.size() - k; i < s.size(); ++i ) {
            if ( s[ i ] != '+' ) {
                isPossible = false;
                break;
            }
        }

        if ( isPossible ) {
            fout << cntr;
        } else {
            fout << "IMPOSSIBLE";
        }

        fout << "\n";
    }

    return 0;
}
