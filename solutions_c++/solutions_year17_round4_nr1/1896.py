#include <cstdio>
#include <algorithm>
#include <cstdlib>

#define MAXN 110

using namespace std;

int A[ MAXN + 1 ];

int num[ 5 ];

int main( void ) {
    int T;
    scanf("%d", &T );
    for( int t = 1; t <= T; t++ ) {
        int N, P;
        scanf("%d%d", &N, &P );
        for( int i = 0; i < 5; i++ ) num[ i ] = 0;
        for( int i = 1; i <= N; i++ ) {
            scanf("%d", &A[ i ] );
            num[ A[ i ] % P ]++;
        }
        int ans = 0;
        if( P == 2 ) {
            ans = num[ 0 ] + num[ 1 ] / 2;
            if( num[ 1 ] % 2 != 0 ) ans++;
        }
        else if( P == 3 ) {
            ans = num[ 0 ];
            ans += min( num[ 1 ], num[ 2 ] );
            ans += abs( num[ 1 ] - num[ 2 ] ) / 3;
            if( abs( num[ 1 ] - num[ 2 ] ) % 3 != 0 ) ans++;
        }
        else if( P == 4 ) {
            ans = num[ 0 ];
        }
        printf("Case #%d: %d\n", t, ans );
    }
}
