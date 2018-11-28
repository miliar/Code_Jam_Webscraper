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
int n, k;
string s;
int a[1010];
int imo[1010];

int solve(){
  s = stin();
  k = in();
  n = SZ(s);

  REP( i , n ){
    if( s[i] == '+' ){
      a[i] = 0;
    } else {
      a[i] = 1;
    }
  }

  REP( i , n ){
    imo[i] = 0;
  }

  int cur = 0;
  int ans = 0;

  REP( i , n-k+1 ){
    cur += imo[i];
    if( ( cur + a[i] ) % 2 == 1 ){
      ans++;
      cur++;
      imo[i+k]--;
    }
  }
  FOR( i , n-k+1 , n ){
    cur += imo[i];
    if( ( cur + a[i] ) % 2 == 1 ){
      return -1;
    }
  }

  return ans;
}

int main(){

  tc = in();
  FOR( i , 1 , tc+1 ){
    int ans = solve();
    if( ans == -1 ){
      printf( "Case #%lld: IMPOSSIBLE\n" , i );
    } else {
      printf( "Case #%lld: %d\n" , i , ans );
    }
  }
  
  return 0;
}
