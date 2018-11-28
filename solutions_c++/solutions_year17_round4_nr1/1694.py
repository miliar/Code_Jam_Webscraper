#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100;

int N, P;
int G[ MAXN ];

signed main() {
  ios::sync_with_stdio( 0 );
  int T;
  cin >> T;
  for( int ti = 1; ti <= T; ++ti ) {
    cin >> N >> P;
    for( int i = 0; i < N; ++i ) {
      cin >> G[ i ];
    }
    vector< int > mod( P );
    for( int i = 0; i < N; ++i ) {
      ++mod[ G[ i ] % P ];
    }
    int ans = mod[ 0 ];
    if( P == 2 ) {
      ans += ( mod[ 1 ] + 1 ) / 2;
    } else if( P == 3 ) {
      ans += min( mod[ 1 ], mod[ 2 ] );
      int d = abs( mod[ 1 ] - mod[ 2 ] );
      ans += d / 3;
      d %= 3;
      if( d ) ++ans;
    } else {

    }
    cout << "Case #" << ti << ": " << ans << endl;
  }
  return 0;
}
