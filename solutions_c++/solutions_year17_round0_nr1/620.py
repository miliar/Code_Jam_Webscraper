#include <bits/stdc++.h>

#define PB          push_back
#define PF          push_front
#define MP          make_pair
#define FI          first
#define SE          second
#define SIZE( A )   int( ( A ).size( ) )
#define ALL( A )    ( A ).begin( ), ( A ).end( )
#define ALLR( A )   ( A ).rbegin( ), ( A ).rend( )

using namespace std;

typedef long long           ll;
typedef unsigned long long  ull;
typedef long double         lf;
typedef pair< int, int >    pii;
typedef pair< ll, ll >      pll;
typedef vector< bool >      vb;
typedef vector< lf >        vd;
typedef vector< ll >        vll;
typedef vector< int >       vi;
typedef vector< pii >       vpii;

typedef complex< lf >       pt;

const int MAXN = int( 1e5 );
const int MOD  = int( 360 );
const int oo   = INT_MAX;

int main( ) {

  #ifdef LOCAL
    freopen( "input", "r", stdin );
    freopen( "output", "w", stdout );
  #else
    //freopen( "input", "r", stdin );
    //freopen( "output", "w", stdout );
    ios_base::sync_with_stdio( 0 );
    cin.tie( 0 );
  #endif

  int n_test;
  cin >> n_test;

  for( int tc = 1; n_test--; tc++ ) {
    string s; int k; cin >> s >> k;
    int ans = 0;
    for( int i = 0; i+k <= SIZE( s ); i++ ) {
      if( s[ i ] == '-' ) {
        ans++;
        for( int j = 0; j < k; j++ ) {
          s[ i+j ] = s[ i+j ] == '+' ? '-' : '+';
        }
      }
    }
    for( int i = 0; i < SIZE( s ); i++ )
      if( s[ i ] == '-' )
        ans = -1;
    cout << "Case #" << tc << ": ";
    if( ans == -1 ) cout << "IMPOSSIBLE\n";
    else cout << ans << "\n";
  }

  return 0;
}
