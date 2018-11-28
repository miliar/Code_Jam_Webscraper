#include <bits/stdc++.h>
      
#define FOR(i,a,b) for( ll i = (a); i < (ll)(b); i++ )
#define REP(i,n) FOR(i,0,n)
#define YYS(x,arr) for(auto& x:arr)
#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort( (x).begin(),(x).end() )
#define REVERSE(x) reverse( (x).begin(),(x).end() )
#define UNIQUE(x) (x).erase( unique( ALL( (x) ) ) , (x).end() )
#define PW(x) (1LL<<(x))
#define SZ(x) ((ll)(x).size())
#define SHOW(x) cout << #x << " = " << x << endl
#define SHOWA(x,n) for( int yui = 0; yui < n; yui++ ){ cout << x[yui] << " "; } cout << endl

#define pb emplace_back
#define fi first
#define se second

using namespace std;

typedef long double ld;
typedef long long int ll;
typedef pair<int,int> pi;
typedef pair<ll,ll> pl;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<ld> vd;
typedef vector<pi> vpi;
typedef vector<pl> vpl;
typedef vector<vpl> gr;
typedef vector<vl> ml;
typedef vector<vd> md;
typedef vector<vi> mi;
     
const ll INF = (ll)1e9 + 10;
const ll INFLL = (ll)1e18 + 10;
const ld EPS = 1e-12;
const ll MOD = 1e9+7;
     
template<class T> T &chmin( T &a , const T &b ){ return a = min(a,b); }
template<class T> T &chmax( T &a , const T &b ){ return a = max(a,b); }
template<class T> inline T sq( T a ){ return a * a; }

ll in(){ long long int x; scanf( "%lld" , &x ); return x; }
char yuyushiki[1000010]; string stin(){ scanf( "%s" , yuyushiki ); return yuyushiki; }

// head


int n, p;
int r[72], a[72], b[72];
int q[72][72];

int solve(){
  n = in();
  p = in();
  REP( i , n ){
    r[i] = in();
    a[i] = r[i] * 9;
    b[i] = r[i] * 11;
  }
  REP( i , n ){
    REP( j , p ){
      q[i][j] = in() * 10;
    }
    sort( q[i], q[i] + p );
  }
  vi s( n , 0 );
  vi t( n , 0 );
  int ans = 0;
  FOR( kos , 1 , 1000010 ){
    bool ok = true;
    REP( i , n ){
      while( t[i] < p and b[i] * kos >= q[i][ t[i] ] ){
        t[i]++;
      }
      while( s[i] < p and a[i] * kos > q[i][ s[i] ] ){
        s[i]++;
      }
      assert( s[i] <= t[i] );
      if( s[i] == t[i] ){
        ok = false;
      }
    }
    while( ok ){
      REP( i , n ){
        s[i]++;
        if( s[i] == t[i] ){
          ok = false;
        }
      }
      ans++;
    }
  }
  return ans;
}

int main(){

  int tc = in();
  FOR( i , 1 , tc+1 ){
    int res = solve();
    printf( "Case #%lld: %d\n" , i , res );
  }
  
  return 0;
}
