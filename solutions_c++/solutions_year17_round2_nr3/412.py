
// default code for competitive programming
// ver 3.1415 {{{

// Includes
#include <bits/stdc++.h>

// Defines
#define NAME(x) #x
#define SZ(c) (int)(c).size()
#define ALL(c) (c).begin(), (c).end()
#define FOR(i, e) for( int i = 0 ; i < (e) ; i++ )
#define ITER(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); it++)
#define REP(i, s, e) for(int i = (s); i <= (e); i++)
#define REPD(i, s, e) for(int i = (s); i >= (e); i--)
#define IOS ios_base::sync_with_stdio( 0 )
#define DEBUG 1
#define fst first
#define snd second
#define PB push_back
#ifdef ONLINE_JUDGE
#define FILE( fn ) \
    freopen(fn".in","r",stdin); \
freopen(fn".out","w",stdout);
#else
#define FILE( fn )
#endif

#ifdef AKAI
#define debug( ... ) fprintf( stderr , __VA_ARGS__ )
#else
#define debug( ... )
#endif

using namespace std;

// Typedefs
typedef double real;
typedef long long ll;
typedef pair<ll, int> pli;
typedef tuple<ll, int> tli;
typedef pair<int, int> pii;
typedef tuple<int, int> tii;
typedef unsigned long long ull;

// Some common const.
const double EPS = 1e-8;
const double Pi = acos(-1);

// Equal for double
bool inline equ(double a, double b)
{return fabs(a - b) < EPS;}

int _R( int& x ) { return scanf( "%d" , &x ); }
int _R( ll& x ) { return scanf( "%" PRId64 , &x ); }
int _R( double& x ) { return scanf( "%lf" , &x ); }
int _R( char* s ) { return scanf( "%s" , s ); }

int R() { return 0; }

  template< typename T1 , typename... T2 >
int R( T1& x , T2&... tail )
{
  int tmp = _R( x );
  return tmp + R( tail... );
}

  template< typename Iter , typename F >
inline void out( Iter s , Iter e , F of )
{
  bool flag = 0;
  for( Iter it = s ; it != e ; it++ )
  {
    if( flag ) printf( " " );
    else flag = 1;
    of( *it );
  }
  puts( "" );
}

// }}}
// start ~~QAQ~~

typedef double type;

const int MAXN = 110;
const type INF = 1e15;

int n , Q;
type E[ MAXN ] , S[ MAXN ];
type D[ MAXN ][ MAXN ];
type D2[ MAXN ][ MAXN ];

void main2( int cs ) {
  printf( "Case #%d: " , cs );
  R( n , Q );
  REP( i , 1 , n ) R( E[ i ] , S[ i ] );
  REP( i , 1 , n ) REP( j , 1 , n ) R( D[ i ][ j ] );
  REP( i , 1 , n ) REP( j , 1 , n ) if ( D[ i ][ j ] < 0 )
    D[ i ][ j ] = INF;
  REP( i , 1 , n ) D[ i ][ i ] = 0;
  REP( k , 1 , n ) REP( i , 1 , n ) REP( j , 1 , n ) {
    D[ i ][ j ] = min( D[ i ][ j ] , D[ i ][ k ] + D[ k ][ j ] );
  }
  REP( i , 1 , n ) REP( j , 1 , n ) {
    if ( D[ i ][ j ] > E[ i ]+EPS ) D2[ i ][ j ] = INF;
    else D2[ i ][ j ] = D[ i ][ j ] / S[ i ];
  }
  REP( k , 1 , n ) REP( i , 1 , n ) REP( j , 1 , n ) {
    D2[ i ][ j ] = min( D2[ i ][ j ] , D2[ i ][ k ] + D2[ k ][ j ] );
  }
  FOR( i , Q ) {
    int u , v;
    R( u , v );
    printf( "%.9f%c" , D2[ u ][ v ] , " \n"[ i == Q-1 ] );
  }
}

int main() {
  int tc;R( tc );
  REP( _ , 1 , tc ) main2( _ );
}
