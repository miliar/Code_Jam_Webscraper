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
    ofstream fout( "B.out" );

    int T;
    fin >> T;
    for ( int testNum = 1; testNum <= T; ++testNum ) {
        fout << "Case #" << testNum << ": ";

        string n;
        fin >> n;

        for ( int i = n.size() - 1; i > 0; --i ) {
            if ( n[ i ] < n[ i - 1 ] ) {
                --n[ i - 1 ];
                for ( int j = i; n[ j ] != '9' && j < n.size(); ++j ) {
                    n[ j ] = '9';
                }
            }
        }
        int i = 0;
        while ( i < n.size() && n[ i ] == '0' ) {
            ++i;
        }
        for ( ; i < n.size(); ++i ) {
            fout << n[ i ];
        }

        fout << "\n";
    }

    return 0;
}
