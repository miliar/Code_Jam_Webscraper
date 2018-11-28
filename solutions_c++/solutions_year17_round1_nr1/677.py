#include <cstdio>
#include <algorithm>
#include <iostream>
#include <iostream>
#include <string>
#include <cstring>

#define MAXN 30

using namespace std;

int E[ MAXN + 1 ];
char grid[ MAXN + 1 ][ MAXN + 1 ];

int main( void ) {
    int T;
    scanf("%d", &T );
    for( int t = 1; t <= T; t++ ) {
        int N, M;
        scanf("%d%d", &N, &M );
        for( int i = 1; i <= N; i++ ) {
            scanf("\n");
            for( int j = 1; j <= M; j++ ) {
                scanf("%c", &grid[ i ][ j ] );
            }
        }
        for( int i = 1; i <= N; i++ ) {
            char current, first;
            bool empty = true;
            for( int j = 1; j <= M; j++ ) {
                if( !empty && grid[ i ][ j ] == '?' ) grid[ i ][ j ] = current;
                if( grid[ i ][ j ] != '?' ) {
                    if( empty ) {
                        empty = false;
                        first = grid[ i ][ j ];
                    }
                    current = grid[ i ][ j ];
                }
            }
            if( !empty ) {
                for( int j = 1; j <= M; j++ ) {
                    if( grid[ i ][ j ] != '?' ) break;
                    grid[ i ][ j ] = first;
                }
            } else {
                E[ i ] = true;
            }

        }
        E[ 0 ] = true;
        E[ N + 1 ] = true;
        for( int i = 1; i <= N; i++ ) {
            if( E[ i ] && !E[ i - 1 ] ) {
                for( int j = 1; j <= M; j++ ) {
                    grid[ i ][ j ] = grid[ i - 1 ][ j ];
                }
                E[ i ] = false;
            }
        }
        for( int i = N; i > 0; i-- ) {
            if( E[ i ] && !E[ i + 1 ] ) {
                for( int j = 1; j <= M; j++ ) {
                    grid[ i ][ j ] = grid[ i + 1 ][ j ];
                }
                E[ i ] = false;
            }
        }
        printf("Case #%d:\n", t );
        for( int i = 1; i <= N; i++ ) {
            for( int j = 1; j <= M; j++ ) {
                printf("%c", grid[ i ][ j ] );
            }
            printf("\n");
        }
        memset( E, 0, sizeof( E ) );
        memset( grid, 0, sizeof( grid ) );
    }
    return 0;
}
