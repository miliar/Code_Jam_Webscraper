#include <iostream>
#include <stdio.h>
#include <fstream>
#include <string.h>

#include <string>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <set>
#include <deque>
#include <utility>
#include <sstream>
#include <queue>
#include <stack>
#include <bitset>

#include <math.h>
#include <algorithm>
#include <limits.h>
#include <iomanip>

#include <cstdio>
#include <cmath>
#include <climits>
#include <cassert>

#include <complex>

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

const int MAXN = int( 2e3 );
const int MOD  = int( 360 );
const int oo   = INT_MAX;

int n, c, m;
int cnt[ MAXN ][ MAXN ], sum[ MAXN ], x[ MAXN ], y[ MAXN ];

void init( ) {
  memset( cnt, 0, sizeof( cnt ) );
  memset( sum, 0, sizeof( sum ) );
  memset( x, 0, sizeof( x ) );
  memset( y, 0, sizeof( y ) );
}

void solve( int tc ) {
  init( );
  cin >> n >> c >> m;
  for( int i = 0; i < m; i++ ) {
    int p, b; cin >> p >> b; p--; b--;
    cnt[ b ][ p ]++;
    sum[ b ]++;
  } 
  int ans_a = 0, ans_b = 0;
  for( int i = 0; i < c; i++ ) {
    x[ i ] += cnt[ i ][ 0 ];
    y[ 0 ] += cnt[ i ][ 0 ]; 
    ans_a = max( ans_a, sum[ i ] );
    cnt[ i ][ 0 ] = 0;
  }
  ans_a = max( ans_a, y[ 0 ] );
  for( int i = 1; i < n; i++ ) {
    for( int j = 0; j < c; j++ ) {
      if( cnt[ j ][ i ] == 0 ) continue;
      int mn = min( min( cnt[ j ][ i ], ans_a-x[ j ] ), ans_a-y[ i ] );
      cnt[ j ][ i ] -= mn;
      x[ j ] += mn;
      y[ i ] += mn; 
    }
  }
  for( int i = 0; i < n; i++ ) {
    for( int j = 0; j < c; j++ ) {
      if( cnt[ j ][ i ] == 0 ) continue;
      ans_b += cnt[ j ][ i ];
    }
  } 
  cout << "Case #" << tc << ": " << ans_a << " " << ans_b << "\n";
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

  for( int tc = 1; tc <= n_test; tc++ )
    solve( tc );

  return 0;
}