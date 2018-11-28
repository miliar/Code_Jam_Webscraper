#include <bits/stdc++.h>

using namespace  std;

bool Tidy( int64_t x ) {

        int mod;
        int last = x % 10;

        x /= 10;

        while( x ) {
                mod = x % 10;
                if( last < mod )
                        return false;
                x /= 10;
                last = mod;
        }

        return true;
}

int main( ) {

        freopen( "input-B-small.txt", "r", stdin );
        freopen( "output-B-small.txt", "w", stdout );

        int t; cin >> t;

        for( int tt = 1; tt <= t; tt ++ ) {
                int64_t x; cin >> x;
                while( !Tidy( x ) ) x --;
                cout << "Case #" << tt << ": " << x << endl;
        }

        return 0;
}
