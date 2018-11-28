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
    cerr << "In test case " << tc << '\n';
    ll n, k; cin >> n >> k;
    set< ll > q;
    map< ll, ll > cnt;
    q.insert( -n ); cnt[ n ] = 1LL;
    while( !q.empty( ) ) {
      ll x = -( *q.begin( ) ); q.erase( q.begin( ) );
      if( x <= 0 ) {
        cnt[ x ] = 0;
        break;
      }
      if( x&1 ) {
        cnt[ x/2LL ] += 2LL*cnt[ x ];
        q.insert( -( x/2LL ) );
      }
      else {
        cnt[ x/2LL ] += cnt[ x ];
        cnt[ x/2LL-1 ] += cnt[ x ];
        q.insert( -( x/2LL ) );
        q.insert( -( x/2LL-1LL ) );
      }
    }
    vector< pll > all;
    for( auto& it : cnt )
      all.PB( { it.FI, it.SE } );
    sort( ALLR( all ) );
    ll mx = 0, mn = 0;
    for( auto& e : all ) {
      if( e.SE < k ) k -= e.SE;
      else {
        if( e.FI%2 == 1 ) mn = mx = e.FI/2LL;
        else mn = e.FI/2LL-1, mx = e.FI/2LL;
        break;
      }
    }
    cout << "Case #" << tc << ": " << mx << " " << mn << "\n";
  }

  return 0;
}
