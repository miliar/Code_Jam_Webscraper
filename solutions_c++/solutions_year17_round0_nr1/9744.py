#include <bits/stdc++.h>

using namespace std;

int k, ans = ( 1 << 28 );

bool valid( string s ) {
        for( int i = 0; i < s.size( ); i ++ )
                if( s[ i ] == '-' )
                        return false;
        return true;
}

void call( string str, int idx, int fn ) {

        if( valid( str ) ) {
                //cout << "I am valid ! " << endl;
                ans = min( ans, fn );
        }

        if( idx >= str.size( ) ) return;

        call( str, idx + 1, fn );

        if( idx + k - 1 < str.size( ) ) {
                for( int i = idx; i <= idx + k - 1; i ++ ) {
                        str[ i ] = str[ i ] == '+' ? '-' : '+';
                }
                call( str, idx + 1, fn + 1 );
        }
}

int main( ) {

        freopen( "input-A-samll.txt", "r", stdin );
        freopen( "output-A-samll.txt", "w", stdout );

        int t; cin >> t;

        for( int i = 1; i <= t; i ++ ) {

                string str;
                cin >> str >> k;

                ans = ( 1<<28 );

                call( str, 0, 0 );

                if( ans == ( 1<<28 ) )
                        cout << "Case #" << i << ": IMPOSSIBLE\n";
                else
                        cout << "Case #" << i << ": " << ans << "\n";
        }

        return 0;
}
