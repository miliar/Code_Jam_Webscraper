#include <bits/stdc++.h>

using namespace std;

int T, K;
string s;

int main() {
  cin >> T;
  for ( int num = 1 ; num <= T ; ++num ) {
    int ans = 0;
    cin >> s >> K;
    for ( int i = 0 ; i < s.size() - K + 1 ; ++i ) {
      if ( s[ i ] == '+' ) continue;
      ++ans;
      for ( int j = 0 ; j < K ; ++j ) {
        if ( s[ i + j ] == '+' )
          s[ i + j ] = '-';
        else 
          s[ i + j ] = '+';
      }
    }
    bool flag = false;
    for ( int i = 0 ; i < s.size() ; ++i )
      if ( s[ i ] != '+' ) {
        cout << "Case #" << num << ": IMPOSSIBLE" << endl;
        flag = true;
        break;
      }
    if ( flag ) continue;
    cout << "Case #" << num << ": " << ans << endl;
  }
}
