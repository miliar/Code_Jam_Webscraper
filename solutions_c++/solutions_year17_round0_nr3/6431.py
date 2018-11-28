#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int ar[1005];

int main() {
    #ifdef CLown1331
        freopen( "C-small-1-attempt0.in", "r", stdin );
        freopen( "out.txt", "w+", stdout );
    #endif /// CLown1331
    int t, n, k, mn, mx, ind, cn;
    cin >> t;
    set < int > le, ri;
    for( int cs=1; cs<=t; cs++ ) {
        cin >> n >> k;
        memset( ar, 0, sizeof ar );
        ar[1] = 1;
        ar[n+2] = 1;
        le.clear();
        ri.clear();
        le.insert( -1 );
        le.insert( -(n+2) );
        ri.insert( 1 );
        ri.insert( (n+2) );
        while( k-- ) {
            mn = -1e9;
            mx = 1e9;
            ind = 0;
            cn = 0;
            for( int i=1; i<=n+2; i++ ) {
                if( ar[i] ) continue;
                int ls = -( *le.lower_bound( -i ) );
                ls = i - ls - 1;
                int rs = ( *ri.lower_bound( i ) );
                rs = rs - i - 1;
                int h = min( ls, rs );
                int h1 = max( ls, rs );
                if( h == mn ) cn++;
                if( h > mn ) {
                    cn = 1;
                    mn = h;
                    ind = i;
                    mx = h1;
                }
            }
            if( cn > 1 ) {
                cn = 0;
                mx = -1e9;
                for( int i=1; i<=n+2; i++ ) {
                    if( ar[i] ) continue;
                    int ls = -( *le.lower_bound( -i ) );
                    ls = i - ls - 1;
                    int rs = ( *ri.lower_bound( i ) );
                    rs = rs - i - 1;
                    int h = min( ls, rs );
                    int h1 = max( ls, rs );
                    if( h == mn ) {
                        if( h1 == mx ) cn++;
                        if( h1 > mx ) {
                            cn = 1;
                            mx = h1;
                            ind = i;
                        }
                    }
                }
//                if( cn > 1 ) {
//                    for( int i=1; i<=n+2; i++ ) {
//                        if( ar[i] ) continue;
//                        int ls = -( *le.lower_bound( -i ) );
//                        ls = i - ls - 1;
//                        int rs = ( *ri.lower_bound( i ) );
//                        rs = rs - i - 1;
//                        int h = min( ls, rs );
//                        int h1 = max( ls, rs );
//                        if( h == mn ) {
//                            if( h1 == mx ) {
//                                ind = i;
//                            }
//                        }
//                    }
//                }
            }
            ar[ind] = 1;
            le.insert( -ind );
            ri.insert( ind );
//            for( int i=1; i<=n+2; i++ ) cerr << ar[i] << " ";
//            cerr << "\n";
        }
        printf( "Case #%d: %d %d\n", cs, mx, mn );
    }
    return 0;
}
