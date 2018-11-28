#include<bits/stdc++.h>
using namespace std;
#define si( n ) scanf("%d",&n)
#define FOR( i, n ) for( int i = 0; i < n; i++ )
#define FOR1( i, n ) for( int i = 1; i <= n; i++ )
#define pb push_back

const int maxn = 1e3 + 10;
int a[ maxn ];
int n, k;

void trans( char *s ){
    FOR( i, n ){
        if( s[ i ] == '-' ) a[ i ] = 1;
        else a[ i ] = 0;
    }
}


int solve(){
    int cnt = 0;
    FOR( i, n - k + 1 ){
        if( a[ i ] % 2 ){
            cnt ++;
            FOR( j, k )
                a[ i + j ] ++;
        }
    }
    for( int i = n - k + 1; i < n; i++ ){
        if( a[ i ] % 2 ) cnt = -1;
    }
    return cnt;
}


int main(){
    int T; si( T );
    FOR1( tt, T ){
        char s[ maxn ]; cin >> s;
        si( k );
        n = strlen( s );
        trans( s );
        int ans = solve();
        printf("Case #%d: ", tt );
        if( ans == -1 ) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans );
    }
}
