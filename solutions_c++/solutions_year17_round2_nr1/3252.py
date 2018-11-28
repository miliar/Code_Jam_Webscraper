#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <functional>
#include <limits>
#include <iomanip>

using namespace std;

//#define TEST

int main( int argc, char** argv )
{
#ifdef TEST
    istream& in = cin;
#else
    ifstream fin( argv[ 1 ] );
    istream& in = fin;
#endif

    ofstream fout( "A.out" );

    int testsNum;
    in >> testsNum;

    for ( int curTest = 1; curTest <= testsNum; ++curTest ) {
        cout << "Case #" << curTest << ": ";

        int distance, n;
        in >> distance >> n;

        map<int, int, std::greater<int>> m;
        for ( int i = 0; i < n; ++i ) {
            int K;
            in >> K;
            int S;
            in >> S;
            if ( m.count( K ) ) {
                m[ K ] = min( m[ K ], S );
            } else {
                m[ K ] = S;
            }
        }

        //map<int, double> timeToNext;

        double curTime = 0.;

        for ( auto p : m ) {
            curTime = std::max( double( distance - p.first ) / p.second, curTime );
        }

        cout << setprecision( 6 ) << fixed << ( distance / curTime );



        cout << "\n";
    }

    return 0;
}
