

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

int n , k;
set<pii> p , x;
typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
  for (int j = 0; j < w[i].size(); j++) {
    if (w[i][j] && !seen[j]) {
      seen[j] = true;
      if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
        mr[i] = j;
        mc[j] = i;
        return true;
      }
    }
  }
  return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
  mr = VI(w.size(), -1);
  mc = VI(w[0].size(), -1);
  
  int ct = 0;
  for (int i = 0; i < w.size(); i++) {
    VI seen(w[0].size());
    if (FindMatch(i, w, mr, mc, seen)) ct++;
  }
  return ct;
}

void main2( int _cs ) {
  printf( "Case #%d: " , _cs );
  p.clear();
  x.clear();
  R( n , k );
  int ans = 0;
  FOR( i , k ) {
    char s[ 2 ];
    int r , c;
    R( s , r , c );
    if ( *s == '+' || *s == 'o' ) p.insert( { r , c } ) , ans++;
    if ( *s == 'x' || *s == 'o' ) x.insert( { r , c } ) , ans++;
  }
  set<pii> ap , ax;
  {
    VVI w( 2*n-1 , VI( 2*n-1 , 0 ) );
    VI mr , mc;
    static bool vis[ 111 ][ 111 ];
    set<int> shitx , shity;
    REP( i , 1 , n ) REP( j , 1 , n ) vis[ i ][ j ] = 0;
    for( auto tp : p ) {
      int px, py;tie( px , py ) = tp;
      vis[ px ][ py ] = 1;
      shitx.insert( { px-1+py-1 } );
      shity.insert( { px-1-py+1+n-1 } );
    }
    REP( i , 1 , n ) REP( j , 1 , n ) if ( !vis[ i ][ j ] ) {
      int xx = ( i-1 ) + ( j-1 );
      int yy = ( i-1 ) - ( j-1 ) + ( n-1 );
      if ( !shitx.count( xx ) and !shity.count( yy ) )
        w[ xx ][ yy ] = 1;
    }
    ans += BipartiteMatching( w , mr , mc );
    FOR( xx , 2*n-1 ) {
      int yy = mr[ xx ];
      if ( yy == -1 ) continue;
      yy -= n-1;
      int i = ( xx+yy ) / 2 + 1;
      int j = xx - ( i-1 ) + 1;
      ap.insert( { i , j } );
    }
  }
  {
    vector<int> rs( n+1 , 1 ) , cs( n+1 , 1 );
    for( auto tp : x ) rs[ tp.first ] = 0;
    for( auto tp : x ) cs[ tp.second ] = 0;
    REP( i , 1 , n ) if ( rs[ i ] ) {
      REP( j , 1 , n ) if ( cs[ j ] ) {
        rs[ i ] = cs[ j ] = 0;
        ax.insert( { i , j } );
        ans++;
        break;
      }
    }
  }
  set<pii> ao;
  int cnt = 0;
  for( pii tp : ap ) {
    cnt++;
    if ( ax.count( tp ) ) {
      cnt--;
      ax.erase( tp );
      ao.insert( tp );
    }
    else if ( x.count( tp ) ) {
      cnt--;
      x.erase( tp );
      ao.insert( tp );
    }
  }
  for( pii tp : ax ) {
    cnt++;
    if ( p.count( tp ) ) {
      cnt--;
      p.erase( tp );
      ao.insert( tp );
    }
  }
  printf( "%d %d\n" , ans , cnt + SZ( ao ) );
  for( auto tp : ap ) if( !ao.count( tp ) ) printf( "+ %d %d\n" , tp.first , tp.second );
  for( auto tp : ax ) if( !ao.count( tp ) ) printf( "x %d %d\n" , tp.first , tp.second );
  for( auto tp : ao ) printf( "o %d %d\n" , tp.first , tp.second );
}

int main() {
  int tc;R(tc);
  REP( _ , 1 , tc ) main2( _ );
}
