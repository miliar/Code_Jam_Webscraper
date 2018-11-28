#include <cstdio>
#include <algorithm>
#include <cstring>
#include <vector>

#define MAXN 55

#define pb push_back

using namespace std;

typedef unsigned long long llu;

int N ,P, R[ MAXN + 1 ], Q[ MAXN + 1 ][ MAXN + 1 ];
vector< int > val[ MAXN + 1 ];

int valid( int serve, int r, int c ) {
    llu l = 9LLU * (llu)serve * ( llu )R[ r ], right = 11LLU * ( llu )serve * ( llu)R[ r ];
    if( l <= 10LLU * ( llu )val[ r ][ c ] && 10LLU * (llu)val[ r ][ c ] <= right ) return 1; // within bounds
    else if( 10LLU * (llu)val[ r ][ c ] > right ) return 0; // too big
    else if( l > 10LLU * ( llu )val[ r ][ c ] ) return -1; // too small
    return 100;
}

int main( void ) {
    int T;
    scanf("%d", &T );
    for( int t = 1; t <= T; t++ ) {
        scanf("%d%d", &N, &P );
        for( int i = 1; i <= N; i++ ) {
            scanf("%d", &R[ i ] );
        }
        for( int i = 1; i <= N; i++ ) {
            for( int j = 1; j <= P; j++ ) {
                scanf("%d", &Q[ i ][ j ] );
                val[ i ].pb( Q[ i ][ j ] );
            }
            sort( val[ i ].begin(), val[ i ].end() );
        }
        int ans = 0;
        for( int serve = 1;; ) {
            bool status = true;
            int cnt = 0;
            for( int i = 1; i <= N; i++ ) {
                do {
                    if( val[ i ].empty() ) {
                        status = false;
                        break;
                    }
                    int V = valid( serve, i, 0 );
                    if( V == 1 ) {
                        cnt++;
                        break;
                    }
                    else if( V == -1 ) {
                        val[ i ].erase( val[ i ].begin() );
                    } else {
                        break;
                    }
                } while( true );
            }
            if( cnt == N ) {
                for( int i = 1; i <= N; i++ ) {
                    val[ i ].erase( val[ i ].begin() );
                }
                ans++;
            }
            else serve++;
            if( !status ) break;
        }
        printf("Case #%d: %d\n", t, ans );
        for( int i = 1; i <= N; i++ ) val[ i ].clear();
        fprintf(stderr,"done with test %d\n", t );
    }
    return 0;
}
