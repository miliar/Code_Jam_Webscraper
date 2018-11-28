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

ll hd, ad, hk, ak, b, d;

ll yu( ll x , ll y ){
  ll chd = hd;
  ll cad = ad;
  ll chk = hk;
  ll cak = ak;
  ll res = x + y;
  REP( i , x ){
    ll nak = cak - d;
    chmax( nak , 0LL );
    if( chd - nak <= 0 ){
      chd = hd - cak;
      res++;
      if( chd - nak <= 0 ){
        return INFLL;
      }
    }
    cak = nak;
    chd -= nak;
  }
  REP( i , y ){
    if( chd - cak <= 0 ){
      chd = hd - cak;
      res++;
      if( chd - cak <= 0 ){
        return INFLL;
      }
    }
    cad = cad + b;
    chd -= cak;
  }
  while( 1 ){
    res++;
    if( chk - cad <= 0 ){
      return res;
    }
    if( chd - cak <= 0 ){
      chd = hd - cak;
      res++;
      if( chd - cak <= 0 ){
        return INFLL;
      }
    }
    chk -= cad;
    chd -= cak;
  }
  return INFLL;
}

ll solve(){
  hd = in();
  ad = in();
  hk = in();
  ak = in();
  b = in();
  d = in();
  ll ans = INFLL;
  REP( i , 101 ){
    REP( j , 101 ){
      chmin( ans , yu(i,j) );
    }
  }
  return ans;
}

int main(){

  int tc = in();
  FOR( i , 1 , tc+1 ){
    ll res = solve();
    if( res == INFLL ){
      printf( "Case #%lld: IMPOSSIBLE\n", i );
    } else {
      printf( "Case #%lld: %lld\n", i , res );
    }
  }
  
  return 0;
}
