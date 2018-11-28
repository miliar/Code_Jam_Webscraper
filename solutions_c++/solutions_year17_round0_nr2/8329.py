#include <bits/stdc++.h>
using namespace std;

using ll = long long;
ll mx, n;

void rec( ll h, int k ) {
    if( h > n ) return;
    mx = max( mx, h );
    for( int i=max( k, 1 ); i<10; i++ ) {
        rec( h * 10 + i, i );
    }
}


int main() {
    #ifdef CLown1331
        freopen( "B-large.in", "r", stdin );
        freopen( "out.txt", "w+", stdout );
    #endif /// CLown1331
//    memset( dp, -1, sizeof dp );
    int t;
    cin >> t;
    for( int cs=1; cs<=t; cs++ ) {
        cin >> n;
        mx = 0;
        rec( 0LL, 0 );
        printf( "Case #%d: %lld\n", cs, mx );
    }
    return 0;
}
