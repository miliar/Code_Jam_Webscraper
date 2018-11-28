#include <iostream>
#include <iomanip>
#include <algorithm>
#include <cmath>

using namespace std;

int N, K;
pair<long long, long long> P[ 1005 ];



long long findBest( const int x, const int k, const long long p ) {
    if( k == K ) return p;
    if( x == N ) return -1;

    const long long res1 = findBest( x + 1, k, p );

    long long actualR = P[ x ].first * P[ x ].first;
    long long actualH = P[ x ].first * P[ x ].second * 2;
    
    long long actual = actualH;
    if( k == 0)
        actual += actualR;
    const long long res2 = findBest( x + 1, k + 1, p + actual );

    if( res1 > res2 ) return res1;
    return res2;
}

int main() {

    int T;
    cin >> T;
    for( int t = 1; t <= T; ++t) {
        
        cin >> N >> K;

        int x, y;
        for( int i = 0; i < N; ++i ) {
            cin >> x >> y;
            P[ i ] = make_pair( x, y );
        }

        cout << "Case #" << t << ": ";
        
        sort( P, P + N );
        reverse( P, P + N );
        long long best = findBest( 0, 0, 0 );
        cout << fixed << setprecision( 9 ) << ( (double)best * M_PI );

        cout << "\n";
    }

    return 0;
}