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

int d;
int arr[ 20 ];
ll pot[ 20 ];

ll dp[ 20 ][ 10 ][ 2 ];

ll go( int i, int lst, int eq ) {
  if( i == d ) return 0;
  ll& r = dp[ i ][ lst ][ eq ];
  if( r != -1 ) return r;
  for( int nd = 9; nd >= lst; nd-- ) {
    if( eq && nd <= arr[ i ] ) {
      ll cur = go( i+1, nd, arr[ i ] == nd );
      if( cur != -2 ) return r = nd*pot[ d-i-1 ] + cur;
    }
    if( !eq ) {
      ll cur = go( i+1, nd, 0 );
      if( cur != -2 ) return r = nd*pot[ d-i-1 ] + cur;
    }
  }
  return r = -2;
}

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

  pot[ 0 ] = 1LL;
  for( int i = 1; i < 20; i++ )
    pot[ i ] = pot[ i-1 ]*10LL;

  int n_test;
  cin >> n_test;

  for( int tc = 1; n_test--; tc++ ) {
    ll n; cin >> n;
    for( d = 0; n; d++ ) {
      arr[ d ] = n%10LL;
      n /= 10LL;
    }
    reverse( arr, arr+d );
    memset( dp, -1, sizeof( dp ) );
    cout << "Case #" << tc << ": " << go( 0, 0, 1 ) << "\n";
  }

  return 0;
}
