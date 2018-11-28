#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const int sz = 1e5 + 10;
int n, fl, en, k;
int dp[1<<11];

int rec( int mask ) {
//    cerr << "\n";
//    for( int i=0; i<n; i++ ) cerr << ( ( mask & ( 1 << i ) ) ? 1 : 0 ) << " ";
    if( mask == en ) fl = 1;
    if( mask == en ) return 0;
    int &ret = dp[mask];
    if( ~ret ) return ret;
    ret = 1e7;
    for( int i=0; i<n; i++ ) {
        int h = mask;
        if( i + k > n ) continue;
        for( int j=i; j<i+k; j++ ) h ^= ( 1 << j );
        ret = min( ret, 1 + rec( h ) );
    }
    return ret;
}


int main() {
    #ifdef CLown1331
        freopen( "A-small-attempt0.in", "r", stdin );
        freopen( "out.txt", "w+", stdout );
    #endif /// CLown1331
//    memset( dp, -1, sizeof dp );
    int t, msk, ans;
    string s;
    cin >> t;
    for( int cs=1; cs<=t; cs++ ) {
        memset( dp, -1, sizeof dp );
        cin >> s >> k;
        n = int( s.size() );
        fl = 0;
        msk = 0;
        en = ( 1 << n ) - 1;
        for( int i=0; i<n; i++ ) {
            if( s[i] == '+' ) msk |= ( 1 << i );
        }
        printf( "Case #%d: ", cs );
//        cerr << "\n";
//        for( int i=0; i<n; i++ ) cerr << ( ( msk & ( 1 << i ) ) ? 1 : 0 ) << " ";
        ans = rec( msk );
        if( !fl ) puts( "IMPOSSIBLE" );
        else printf( "%d\n", ans );
    }
    return 0;
}
