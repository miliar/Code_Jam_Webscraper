#include<bits/stdc++.h>

using namespace std;

int T,n;

bool check( int i ) {
  int lst = 9;
  while( i ) {
    if( i%10 > lst ) return false;
    lst = i%10;
    i /= 10;
  }
  return true;
}

int main() {
  ios_base::sync_with_stdio( 0 );
  cin.tie( 0 );
  freopen( "/Users/Daniel/Desktop/input", "r", stdin );
  freopen( "/Users/Daniel/Desktop/output", "w", stdout );
  cin >> T;
  for( int tc = 1; tc <= T; ++tc ) {
    cin >> n;
    int i;
    for( i = n; i >= 0; --i )
      if( check(i) ) break;
    cout << "Case #" << tc << ": " << i << '\n';
  }

}
