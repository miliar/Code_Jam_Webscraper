
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

const int MAXN = 110;

int n , P;
int c[ 5 ];
int dp[ MAXN ][ MAXN ][ MAXN ][ MAXN ];

inline void chk(int &a , int b) {
  a = max( a , b );
}

void main2(int cs) {
  printf("Case #%d: ", cs);
  R( n , P );
  fill( c , c+4 , 0 );
  FOR( i , n ) {
    int x;R( x );
    c[ x%P ]++;
  }
  REP( i0 , 0 , c[ 0 ] ) REP( i1 , 0 , c[ 1 ] ) REP( i2 , 0 , c[ 2 ] ) REP( i3 , 0 , c[ 3 ] ) {
    dp[ i0 ][ i1 ][ i2 ][ i3 ] = 0;
  }
  REP( i0 , 0 , c[ 0 ] ) REP( i1 , 0 , c[ 1 ] ) REP( i2 , 0 , c[ 2 ] ) REP( i3 , 0 , c[ 3 ] ) {
    int s = i1 + i2*2 + i3*3;
    s %= P;
    int rst = (P-s)%P;
    int tmp = dp[ i0 ][ i1 ][ i2 ][ i3 ];
    if ( rst == 0 ) tmp++;
    chk( dp[ i0+1 ][ i1 ][ i2 ][ i3 ] , tmp );
    chk( dp[ i0 ][ i1+1 ][ i2 ][ i3 ] , tmp );
    chk( dp[ i0 ][ i1 ][ i2+1 ][ i3 ] , tmp );
    chk( dp[ i0 ][ i1 ][ i2 ][ i3+1 ] , tmp );
  }
  printf( "%d\n" , dp[ c[ 0 ] ][ c[ 1 ] ][ c[ 2 ] ][ c[ 3 ] ] );
}

int main() {
  int tc;R(tc);REP(_,1,tc) {
    main2(_);
  }
}
