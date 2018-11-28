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

const int MAXN = int( 1000 );
const int MOD  = int( 360 );
const int oo   = INT_MAX;

int n, p;
int g[ MAXN ];
int cnt[ MAXN ];

void init( ) {
  memset( cnt, 0, sizeof( cnt ) );
}

void solve( int tc ) {
  init( );
  cin >> n >> p;
  for( int i = 0; i < n; i++ ) {
    int g; cin >> g;
    cnt[ g%p ]++;
  }
  int mn;
  int ans = cnt[ 0 ];
  if( p == 2 ) {
    ans += ( cnt[ 1 ]/2 ) + ( cnt[ 1 ]%2 );
  }
  else if( p == 3 ) {
    mn = min( cnt[ 1 ], cnt[ 2 ] );
    ans += mn;
    cnt[ 1 ] -= mn; cnt[ 2 ] -= mn;
    ans += ( cnt[ 1 ]/3 ) + ( cnt[ 1 ]%3 > 0 );
    ans += ( cnt[ 2 ]/3 ) + ( cnt[ 2 ]%3 > 0 );
  }
  else {
    ans += cnt[ 2 ]/2; cnt[ 2 ] %= 2;
    mn = min( cnt[ 1 ], cnt[ 3 ] );
    ans += mn;
    cnt[ 1 ] -= mn; cnt[ 3 ] -= mn;
    if( cnt[ 2 ] && cnt[ 1 ] > 1 ) {
      ans++;
      cnt[ 2 ]--;
      cnt[ 1 ] -= 2;
    }
    if( cnt[ 2 ] && cnt[ 3 ] > 1 ) {
      ans++;
      cnt[ 2 ]--;
      cnt[ 3 ] -= 2;
    }
    ans += ( cnt[ 1 ]/4 ) + ( cnt[ 1 ]%4 > 0 );
    ans += ( cnt[ 3 ]/4 ) + ( cnt[ 3 ]%4 > 0 );
  }
  cout << "Case #" << tc << ": " << ans << "\n";
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

  for( int tc = 1; tc <= n_test; tc++ ) {
    cerr << "Case #" << tc << "\n";
    solve( tc );
  }

  return 0;
}