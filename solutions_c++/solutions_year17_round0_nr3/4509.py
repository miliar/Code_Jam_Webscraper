#include <cstdio>
#include <algorithm>
#include <vector>
#include <functional>

#define MAXN 1000100

#define X first
#define Y second
#define mp make_pair
#define pb push_back

using namespace std;

typedef pair< int, int > pii;
typedef pair< pii, int > item;

vector< int > A;
vector< int > current;

int main( void ) {
    int T;
    scanf("%d", &T );
    for( int t = 1; t <= T; t++ ) {
        int N, K;
        scanf("%d%d", &N, &K );
        int level = 0;
        while( true ) {
            if( K - ( 1 << level ) <= 0 ) break;
            K -= ( 1 << level );
            level++;
        }
        A.pb( 0 );
        A.pb( N + 1 );
        int bound = ( 1 << ( level ) );
        for( int l = 0; l < level; l++ ) {
            vector< int > C;
            for( int i = 0; i < A.size() - 1; i++ ) {
                C.pb( ( ( A[ i ] + A[ i + 1 ] ) / 2 ) );
            }
            for( int i = 0; i < C.size(); i++ ) {
                A.pb( C[ i ] );
            }
            sort( A.begin(), A.end() );
        }
        vector< item > C;
        sort( A.begin(), A.end() );
        for( int i = 0; i < A.size() - 1; i++ ) {
            int val = ( A[ i ] + A[ i + 1 ] ) / 2;
            if( val == A[ i ] || val == A[ i + 1 ] ) continue;
            int d1 = val - A[ i ] - 1;
            int d2 = A[ i + 1 ] - val - 1;
            C.pb( mp( mp( min( d1, d2 ), max( d1, d2 ) ), val ) );
        }
        sort( C.begin(), C.end(), greater< item >() );
        int idx = C[ K - 1 ].Y, d1 = C[ K - 1 ].X.Y, d2 = C[ K - 1 ].X.X;
        printf("Case #%d: %d %d\n", t, d1, d2 );
        current.clear();
        A.clear();
    }
    return 0;
}
