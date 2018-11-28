#include<bits/stdc++.h>

using namespace std;

int T,n,k;

void update( int idx, int* l, int* r, bool* s ) {
  s[ idx ] = true;
  for( int i = 1; i <= n; ++i ) {
    if( s[ i ] ) {
      l[ i ] = r[ i ] = 0;
      continue;
    }
    for( int j = i-1, cnt = 0; j >= 0; --j, ++cnt )
      if( s[ j ] ) {
        l[ i ] = cnt;
        break;
      }
    for( int j = i+1, cnt = 0; ; ++j, ++cnt )
      if( s[ j ] ) {
        r[ i ] = cnt;
        break;
      }
  }
}

int main() {
  ios_base::sync_with_stdio( 0 );
  cin.tie( 0 );
  freopen( "/Users/Daniel/Desktop/input", "r", stdin );
  freopen( "/Users/Daniel/Desktop/output", "w", stdout );
  cin >> T;
  for( int tc = 1; tc <= T; ++tc ) {
    cin >> n >> k;
    int l[ n+2 ], r[ n+2 ];
    bool s[ n+2 ];
    memset( s, false, sizeof(s) );
    l[ 0 ] = r[ 0 ] = l[ n+1 ] = r[ n+1 ] = -1;
    s[ 0 ] = true;
    s[ n+1 ] = true;
    update( 0, l, r, s );
    int ans = 0;
    for( int ps = 0; ps < k; ++ps ) {
      ans = 0;
      for( int i = 1; i <= n; ++i ) {
        if( s[i] ) continue;
        int cur = min(l[i], r[i]);
        int prv = min(l[ans],r[ans]);
        if( cur > prv ) ans = i;
        else if( cur == prv )
          if( max(l[i],r[i]) > max(l[ans],r[ans]) )
            ans = i;
      }
      if( ps < k-1 ) update( ans, l, r, s );
    }
    /*for( int i = 0; i < n+2; ++i ) {
      if( s[i] ) cout << "1 ";
      else cout << "0 ";
    }
    cout << endl;*/
    cout << "Case #" << tc << ": " << r[ans] << " " << l[ans] << '\n';
  }

}
