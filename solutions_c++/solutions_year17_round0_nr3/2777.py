#include <iostream>
#include <fstream>
#include <map>

using namespace std;

typedef unsigned long long INT;

int main( int argc, char** argv )
{
    if ( argc < 2 ) {
        cout << "NG\n";
        return 0;
    }

    ifstream fin( argv[ 1 ] );
    ofstream fout( "C.out" );

    int T;
    fin >> T;
    for ( int testNum = 1; testNum <= T; ++testNum ) {
        fout << "Case #" << testNum << ": ";

        INT n, k;
        fin >> n >> k;

        INT iterations = 0;
        while ( ( 1ULL << ( iterations + 1 ) ) <= k ) {
            ++iterations;
        }

        //cout << iterations << " ";

        map<INT, INT, std::greater<INT>> state { { n, 1 } };
        for ( INT i = 0; i < iterations; ++i ) {
            std::map<INT, INT, std::greater<INT>> newState;
            for ( auto& p : state ) {
                INT cur = p.first - 1;
                INT first = cur / 2 + cur % 2;
                INT second = cur / 2;
                newState[ first ] += p.second;
                newState[ second ] += p.second;
            }
            state = newState;
        }

        //cout << state.begin()->first << " " << state.begin()->second << endl;

        INT curIndex = k - ( 1ULL << iterations );
        for ( auto& p : state ) {
            if ( p.second > curIndex ) {
                INT cur = p.first - 1;
                fout << ( cur / 2 + cur % 2 ) << " " << ( cur / 2 );
                break;
            }
            curIndex -= p.second;
        }

        fout << "\n";
    }
}
