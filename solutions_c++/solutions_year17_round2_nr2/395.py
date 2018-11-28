
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

char c[] = "ROYGBV";
int n , cnt[ 6 ];

void main2( int cs ) {
  printf( "Case #%d: " , cs );
  R( n );
  FOR( i , 6 ) R( cnt[ i ] );
  FOR( i , 3 ) {
    if ( cnt[ i ] + cnt[ i+3 ] == n ) {
      if ( cnt[ i ] != cnt[ i+3 ] ) {
        puts( "IMPOSSIBLE" );
        return;
      }
      FOR( j , n )
        if ( j&1 ) putchar( c[ i ] );
        else putchar( c[ i+3 ] );
      puts( "" );
      return;
    }
  }
  vector<string> strs[ 6 ];
  for ( int i = 0 ; i < 6 ; i += 2 ) {
    int sub = ( i+3 ) % 6;
    if ( cnt[ i ] == 0 ) continue;
    if ( cnt[ i ] <= cnt[ sub ] ) {
      puts( "IMPOSSIBLE" );
      return;
    }
    string s1( 1 , c[ i ] );
    for ( int j = 0 ; j < cnt[ sub ] ; j++ ) {
      s1 += c[ sub ];
      s1 += c[ i ];
    }
    strs[ i ].push_back( s1 );
    cnt[ i ] -= cnt[ sub ] + 1;
    for ( int j = 0 ; j < cnt[ i ] ; j++ )
      strs[ i ].push_back( string( 1 , c[ i ] ) );
  }
  vector<pii> vec;
  vector<int> ord{ 0 , 2 , 4 };
  sort( ALL( ord ) , [&]( int a , int b ) { return SZ( strs[ a ] ) > SZ( strs[ b ] ); } );
  FOR( i , SZ( strs[ ord[ 0 ] ] ) ) vec.emplace_back( ord[ 0 ] , i );
  FOR( i , SZ( strs[ ord[ 1 ] ] ) ) {
    pii p{ ord[ 1 ] , i };
    vec.insert( vec.begin()+2*i , p );
  }
  FOR( i , SZ( strs[ ord[ 2 ] ] ) ) {
    pii p{ ord[ 2 ] , i };
    vec.insert( vec.end()-2*i-1 , p );
  }
  FOR( i , SZ( vec ) ) {
    int nxt = ( i+1 ) % SZ( vec );
    if ( vec[ i ].first == vec[ nxt ].first ) {
      puts( "IMPOSSIBLE" );
      return;
    }
  }
  for ( auto p : vec ) cout << strs[ p.first ][ p.second ];
  cout << endl;
}

int main() {
  int tc;R( tc );
  REP( _ , 1 , tc ) main2( _ );
}
