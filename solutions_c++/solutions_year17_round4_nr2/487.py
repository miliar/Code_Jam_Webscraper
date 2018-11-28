
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

int N , M , C;

pii tic[ MAXN ];
unordered_set<int> cus[ MAXN ];
unordered_set<int> seat[ MAXN ];
int mn[ MAXN ];

inline bool nopro( pii t , int j ) {
  if ( cus[ j ].count( t.second ) ) return 0;
  if ( seat[ j ].count( t.first ) ) return 0;
  return 1;
}

inline bool ins( pii t , int j , int& cnt ) {
  if ( cus[ j ].count( t.second ) ) return 0;
  int sn = t.first;
  if ( seat[ j ].count( sn ) ) {
    while ( seat[ j ].count( mn[ j ] ) ) {
      mn[ j ]++;
    }
    if ( mn[ j ] >= sn ) return 0;
    cnt++;
    sn = mn[ j ];
  }
  seat[ j ].insert( sn );
  cus[ j ].insert( t.second );
  return 1;
}

int chk( int y ) {
  REP( i , 1 , y ) {
    cus[ i ].clear();
    seat[ i ].clear();
    mn[ i ] = 1;
  }
  int cnt = 0;
  REP( i , 1 , M ) {
    bool ok = 0;
    REP( j , 1 , y ) if ( nopro( tic[ i ] , j ) ) {
      ok = 1;
      seat[ j ].insert( tic[ i ].first );
      cus[ j ].insert( tic[ i ].second );
      break;
    }
    if ( ok ) continue;
    REP( j , 1 , y ) {
      bool flag = ins( tic[ i ] , j , cnt );
      if ( flag ) {
        ok = 1;
        break;
      }
    }
    if ( !ok ) return -1;
  }
  return cnt;
}

vector<int> tt[ MAXN ];
int need[ MAXN ];

void main2(int cs) {
  printf("Case #%d: ", cs);
  R( N , C , M );
  REP( i , 1 , M ) R( tic[ i ].first , tic[ i ].second );
  sort( tic+1 , tic+1+M );
  REP( i , 1 , C ) tt[ i ].clear();
  REP( i , 1 , M ) tt[ tic[ i ].second ].push_back( tic[ i ].first );
  int ans = 0;
  REP( i , 1 , C ) ans = max( ans , SZ( tt[ i ] ) );
  fill( need , need+N+1 , 0 );
  REP( i , 1 , M ) need[ tic[ i ].first ]++;
  int sum = 0;
  REP( i , 1 , N ) {
    sum += need[ i ];
    int cur = ( sum + i-1 ) / i;
    ans = max( ans , cur );
  }
  int pro = 0;
  REP( i , 1 , N ) if ( need[ i ] > ans ) pro += need[ i ]-ans;
  printf( "%d %d\n" , ans , pro );
}

int main() {
  int tc;R(tc);REP(_,1,tc) {
    main2(_);
  }
}
