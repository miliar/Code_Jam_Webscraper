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

int n, m;
string s[72];

void solve(){
  n = in();
  m = in();
  REP( i , n ){
    s[i] = stin();
  }
  int pr = 0;
  REP( i , n ){
    int pc = 0;
    REP( j , m ){
      if( s[i][j] != '?' ){
        FOR( k , pr , i+1 ){
          FOR( l , pc , j+1 ){
            s[k][l] = s[i][j];
          }
        }
        pc = j+1;
      }
    }
    if( pc != 0 ){
      FOR( k , pr , i+1 ){
        FOR( l , pc , m ){
          s[k][l] = s[i][pc-1];
        }
      }
      pr = i+1;
    }
  }
  FOR( i , pr , n ){
    REP( j , m ){
      s[i][j] = s[i-1][j];
    }
  }
  REP( i , n ){
    printf( "%s\n" , s[i].c_str() );
  }
}

int main(){

  int tc = in();
  FOR( i , 1 , tc+1 ){
    printf( "Case #%lld:\n" , i );
    solve();
  }

  return 0;
}
