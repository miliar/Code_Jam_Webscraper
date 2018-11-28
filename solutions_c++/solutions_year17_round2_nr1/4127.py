#include <iostream>
#include <vector>

using namespace std;

double maxSpeed( vector< long long int > &k,
                 vector< long long int > &s,
                 long long int d )
{
    double maxS = 100000000000000.0; // max speed is 1e5
    double t1, t2;
    double m;
    double kslow;
    double sslow;
    if ( k.size() == 1 ) {
        return (double)d * s[ 0 ] / ( d - k[ 0 ] );
    }
    // compute mutually time
    // n~1000, O(n^2)
    for ( size_t i = 0; i < k.size(); ++i ) {
        for ( size_t j = i + 1; j < k.size(); ++j ) {
            t1 = ((double) d - k[ i ] ) / s[ i ];
            t2 = ( ( double ) d - k[ j ] ) / s[ j ];

            if ( t1 > t2 &&
                 k[ i ] < k[ j ] ) {
                // h1 is slow, go with h1
                if ( s[ i ] < maxS ) {
                    maxS = ( double ) d * s[ i ] / ( d - k[ i ] );
                }
            } else if ( t1 < t2 &&
                        k[ i ] > k[ j ] ) {
                // h2 is slow, go with h2
                if ( s[ j ] < maxS ) {
                    maxS = ( double ) d * s[ j ] / ( d - k[ j ] );
                }
            } else {
                kslow = t1>t2 ? k[i] : k[j];
                sslow = t1>t2 ? s[ i ] : s[ j ];
                // calculate intersection
                if ( s[ i ] == s[ j ] ) {
                    m = d;
                } else {
                    m = ( ( double ) s[ j ] * k[ i ] - s[ i ] * k[ j ] ) / ( s[ j ] - s[ i ] );
                }
                if ( m != k[ i ] &&
                     ( double ) m * s[ i ] / ( m - k[ i ] ) < maxS ) {
                    maxS = ( double ) m * s[ i ] / ( m - k[ i ] );
                }
                if ( m != k[ j ] &&
                     ( double ) m * s[ j ] / ( m - k[ j ] ) < maxS ) {
                    maxS = ( double ) m * s[ j ] / ( m - k[ j ] );
                }
                if ( d != kslow &&
                     ( double ) d / ( d - kslow )*sslow < maxS ) {
                    maxS = ( double ) d / ( d - kslow )*sslow;
                }
            }
        } // for j
    } // for i
    return maxS;
}

int main( int argc, char *argv[] )
{
    int t;
    cin >> t;

    long long int d;
    int n;
    double speed;
    cout.precision( 6 );
    cout.setf( ios::showpoint );
    std::cout << std::fixed;
    for ( int caseid = 0; caseid < t; ++caseid ) {

        // input
        cin >> d >> n;
        vector< long long int > k( n );
        vector< long long int > s( n );
        for ( int i = 0; i < n; ++i ) {
            cin >> k[ i ] >> s[ i ];
        }

        // process
        speed = maxSpeed( k, s, d );

        // output
        cout << "Case #" << caseid + 1 << ": ";

        cout << speed;

        cout << endl;
    }
    return 0;
}