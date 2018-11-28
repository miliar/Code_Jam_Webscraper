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

int tc;
ll n, k;

map<ll,ll> ma;

pl solve(){
  n = in();
  k = in();

  ma.clear();
  
  ma[n] = 1;

  while( 1 ){
    pl t = *(ma.rbegin());
    // cout << t.fi << " " << t.se << endl;
    ma.erase( ma.find( t.fi ) );

    ll a, b;
    if( t.fi % 2 == 0 ){
      a = t.fi / 2;
      b = t.fi / 2 - 1;
    } else {
      a = t.fi / 2;
      b = t.fi / 2;
    }

    if( k <= t.se ){
      return pl( a , b );
    }

    ma[a] += t.se;
    ma[b] += t.se;

    k -= t.se;
  }
}

int main(){

  tc = in();
  FOR( i , 1 , tc+1 ){
    pl ans = solve();
    printf( "Case #%lld: %lld %lld\n", i, ans.fi, ans.se );
  }
  
  return 0;
}
