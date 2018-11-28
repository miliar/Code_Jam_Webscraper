
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

const int MAXN = 1010;
typedef double type;
typedef pair<type,type> Pts;
#define X first
#define Y second

int D , n;
Pts p[ MAXN ];


void main2( int cs ) {
  printf( "Case #%d: " , cs );
  R( D , n );
  REP( i , 1 , n ) R( p[ i ].first , p[ i ].second );
  sort( p+1 , p+1+n );
  reverse( p+1 , p+1+n );
  vector<Pts> stk;
  REP( i , 1 , n ) {
    type my_t = ( D - p[ i ].X ) / p[ i ].Y;
    while( SZ( stk ) ) {
      Pts pt = stk.back();
      type p_t = ( D - pt.X ) / pt.Y;
      if ( my_t > p_t-EPS ) {
        stk.pop_back();
      } else {
        stk.pop_back();
        if ( SZ( stk ) ) {
          Pts pt2 = stk.back();
          type ins_p1 = ( p[ i ].Y*pt.X - p[ i ].X*pt.Y ) / ( p[ i ].Y - pt.Y );
          type ins_p2 = ( p[ i ].Y*pt2.X - p[ i ].X*pt2.Y ) / ( p[ i ].Y - pt2.Y );
          if ( ins_p1 < ins_p2 ) continue;
        } 
        stk.push_back( pt );
        break;
      }
    }
    stk.push_back( p[ i ] );
  }
  Pts slow = stk[ 0 ];
  type fin_t = ( D - slow.X ) / slow.Y;
  printf( "%.12f\n" , (1. * D) / fin_t );
}

int main() {
  int tc;R( tc );
  REP( _ , 1 , tc ) main2( _ );
}
