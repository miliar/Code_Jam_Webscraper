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

void doit( int& r, int& c, vector< string >& board ) {
  for( int i = 0; i < r; i++ ) {
    for( int j = 0; j < c; j++ ) {
      if( board[ i ][ j ] != '?' ) {
        for( int ni = i-1; ni >= 0 && board[ ni ][ j ] == '?'; ni-- )
          board[ ni ][ j ] = board[ i ][ j ];
        for( int ni = i+1; ni < r && board[ ni ][ j ] == '?'; ni++ )
          board[ ni ][ j ] = board[ i ][ j ];
      }
    }
  }
}

void rot90( int& r, int& c, vector< string >& board ) {
  vector< string > nboard( c );
  for( auto& e : nboard ) e = string( r, ' ' );
  for( int i = 0; i < r; i++ )
    for( int j = 0; j < c; j++ )
      nboard[ j ][ r-i-1 ] = board[ i ][ j ];
  board = nboard;
  swap( r, c );
}

void solve( ) {
  int r, c; cin >> r >> c;
  vector< string > board( r );
  for( auto& e : board ) cin >> e;
  for( int i = 0; i < 4; i++ ) {
    doit( r, c, board );
    rot90( r, c, board );
  }
  for( auto& e : board ) cout << e << "\n";
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
    cout << "Case #" << tc << ":\n";
    solve( );
  }

  return 0;
}
