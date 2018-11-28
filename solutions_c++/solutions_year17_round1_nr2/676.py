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

struct Event {
  ll f, t; int tp;
  bool operator < ( const Event& o ) const {
    if( f != o.f ) return f < o.f;
    return t < o.t;
  }
};

ll find_lowest( ll e, ll x ) {
  ll lo = 1, hi = ll( 1e10 );
  while( lo <= hi ) {
    ll mi = ( lo+hi )>>1;
    if( x*100LL <= 110LL*mi*e ) hi = mi-1;
    else lo = mi+1;
  }
  return lo;
}

ll find_highest( ll e, ll x ) {
  ll lo = 1, hi = ll( 1e10 );
  while( lo <= hi ) {
    ll mi = ( lo+hi )>>1;
    if( x*100LL >= 90LL*mi*e ) lo = mi+1;
    else hi = mi-1;
  }
  return hi;
}

void solve( ) {
  cout << fixed << setprecision( 2 );
  int n, p; cin >> n >> p;
  vi r( n );
  for( auto& e : r ) cin >> e;
  vector< vi > q( n, vi( p ) );
  vector< Event > events;
  for( int i = 0; i < n; i++ ) {
    for( int j = 0; j < p; j++ ) {
      cin >> q[ i ][ j ];
      int a = find_lowest( r[ i ], q[ i ][ j ] );
      int b = find_highest( r[ i ], q[ i ][ j ] );
      if( b < a ) continue;
      events.PB( { a, b, i } );
    }
  }
  sort( ALL( events ) );
  vi cnt( n );
  vector< priority_queue< int, vector< int >, greater< int > > > pq( n );
  int ans = 0;
  for( auto& e : events ) {
    for( auto& q : pq ) {
      while( !q.empty( ) && q.top( ) < e.f )
        q.pop( );
    }
    pq[ e.tp ].push( e.t );
    int mn = p;
    for( auto& q : pq )
      mn = min( mn, SIZE( q ) );
    ans += mn;
    for( auto& q : pq ) {
      for( int i = 0; i < mn; i++)
        q.pop( );
    }
  }
  cout << ans;
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

  int n_test; cin >> n_test;

  for( int tc = 1; n_test--; tc++ ) {
    cerr << "Solving test case #" << tc << "\n";
    cout << "Case #" << tc << ": ";
    solve( );
    cout << "\n";
  }

  return 0;
}
