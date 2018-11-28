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
int dp[110][110][110];
int a[110];
int r[4];

int solve(){
  n = in();
  p = in();
  REP( i , n ){
    a[i] = in();
  }
  REP( i , 110 ){
    REP( j , 110 ){
      REP( k , 110 ){
        dp[i][j][k] = 0;
      }
    }
  }
  REP( i , 4 ){
    r[i] = 0;
  }
  REP( i , n ){
    r[ a[i] % p ]++;
  }
  REP( i , 110 ){
    REP( j , 110 ){
      REP( k , 110 ){
        int cr = ( i + j * 2 + k * 3 ) % p;
        int add = ( cr == 0 ? 1 : 0 );
        int nex = dp[i][j][k] + add;

        if( i < r[1] ){
          chmax( dp[i+1][j][k], nex );
        }

        if( j < r[2] ){
          chmax( dp[i][j+1][k], nex );
        }

        if( k < r[3] ){
          chmax( dp[i][j][k+1], nex );
        }
      }
    }
  }
  return dp[ r[1] ][ r[2] ][ r[3] ] + r[0];
}

int main(){

  int t = in();
  FOR( tc , 1 , t+1 ){
    int res = solve();
    printf( "Case #%lld: %d\n", tc, res );
  }
  
  return 0;
}
