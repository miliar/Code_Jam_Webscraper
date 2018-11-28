#include<bits/stdc++.h>

using namespace std;

string s;
int k, T, ans;

void flip( int idx ) {
  for( int i = idx; i < idx+k; ++i ) {
    if( s[ i ] == '+' ) s[ i ] = '-';
    else if( s[ i ] == '-' ) s[ i ] = '+';
  }
}

int main() {
  ios_base::sync_with_stdio( 0 );
  cin.tie( 0 );
  freopen( "/Users/Daniel/Desktop/input", "r", stdin );
  freopen( "/Users/Daniel/Desktop/output", "w", stdout );
  cin >> T;
  for( int tc = 1; tc <= T; ++tc ) {
    cin >> s >> k;
    ans = 0;
    for( int i = 0; i <= s.size()-k; ++i ) {
      if( s[ i ] == '+' ) continue;
      flip( i );
      ++ans;
    }
    bool flag = true;
    for( int i = 0; i < s.size(); ++i )
      if( s[ i ] == '-' ) {
        flag = false;
        break;
      }
    cout << "Case #" << tc << ": ";
    if( flag ) cout << ans << '\n';
    else cout << "IMPOSSIBLE\n";
  }

}
