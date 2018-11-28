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


struct MaxFlow{
  struct edge{
    int to, cap, rev;
    edge(){}
    edge( int to , int cap , int rev ) : to(to) , cap(cap) , rev(rev) {}
  };
  vector<vector<edge> > G;
  vi level, iter;
  int n;
  void init( int arg_n ){
    n = arg_n;
    G = vector<vector<edge> >( n , vector<edge>(0) );
  }
  void add_edge( int from , int to , int cap ){
    G[from].pb( to , cap , SZ(G[to]) );
    G[to].pb( from , 0 , SZ(G[from])-1 );
  }
  void bfs( int s ){
    level = vi( n , -1 );
    queue<int> que;
    level[s] = 0;
    que.push( s );
    while( !que.empty() ){
      int v = que.front(); que.pop();
      YYS( e , G[v] ){
	if( e.cap > 0 && level[e.to] < 0 ){
	  level[e.to] = level[v] + 1;
	  que.push( e.to );
	}
      }
    }
  }
  int dfs( int v , int t , int f ){
    if( v == t ) return f;
    for( int &i = iter[v]; i < G[v].size(); i++ ){
      edge &e = G[v][i];
      if( e.cap > 0 && level[v] + 1 == level[e.to] ){
	int d = dfs( e.to , t , min( f , e.cap ) );
	if( d > 0 ){
	  e.cap -= d;
	  G[e.to][e.rev].cap += d;
	  return d;
	}
      }
    }
    return 0;
  }
  int max_flow( int s , int t ){
    int flow = 0;
    while( 1 ){
      bfs( s );
      if( level[t] < 0 ) return flow;
      iter = vi( n , 0 );
      int f;
      while( (f = dfs( s , t , INF )) > 0 ) flow += f;
    }
  }
};

typedef pair<pi,char> rr;

MaxFlow mf;

void solve( int tc ){
  int n = in();
  int m = in();
  mi a( n , vi(n,0) );
  mi b( n , vi(n,0) );
  vb ur( n , false );
  vb uc( n , false );
  vb us( 2*n , false );
  vb ut( 2*n , false );
  REP( i , m ){
    string s = stin();
    int r = in() - 1;
    int c = in() - 1;
    if( s[0] == 'o' ){
      a[r][c] = 1;
      b[r][c] = 1;
      ur[r] = true;
      uc[c] = true;
      us[r+c] = true;
      ut[r-c+n] = true;
    } else if( s[0] == '+' ){
      a[r][c] = 1;
      us[r+c] = true;
      ut[r-c+n] = true;
    } else if( s[0] == 'x' ){
      b[r][c] = 1;
      ur[r] = true;
      uc[c] = true;
    }
  }
  REP( i , n ){
    if( not ur[i] ){
      REP( j , n ){
        if( not uc[j] ){
          ur[i] = true;
          uc[j] = true;
          b[i][j] = 2;
          break;
        }
      }
    }
  }
  
  mf.init( 4 * n + 2 );
  REP( i , n ){
    REP( j , n ){
      int s = i + j;
      int t = i - j + n;
      if( ( not us[s] ) and ( not ut[t] ) ){
        mf.add_edge( s , ( 2 * n ) + t , 1 );
      }
    }
  }

  int so = 4 * n;
  int si = so + 1;
  REP( i , 2 * n ){
    mf.add_edge( so , i , 1 );
    mf.add_edge( 2 * n + i , si , 1 );
  }
  
  int re = mf.max_flow( so , si );
  
  REP( i , 2*n ){
    YYS( w , mf.G[i] ){
      if( w.cap == 0 and w.to != so ){
        int s = i;
        int t = w.to - 3 * n;
        
        int y = ( s + t ) / 2;
        int x = ( s - t ) / 2;

        a[y][x] = 2;
      }
    }
  }
  
  vector<rr> res;
  int ans = 0;
  REP( i , n ){
    REP( j , n ){
      if( a[i][j] != 0 ){
        ans++;
      }
      if( b[i][j] != 0 ){
        ans++;
      }
      if( ( a[i][j] == 2 and b[i][j] ) or ( a[i][j] and b[i][j] == 2 ) ){
        res.pb( pi( i , j ) , 'o' );
      } else if( a[i][j] == 2 ){
        res.pb( pi( i , j ) , '+' );
      } else if( b[i][j] == 2 ){
        res.pb( pi( i , j ) , 'x' );
      }
    }
  }

  printf( "Case #%d: %d %lld\n" , tc, ans, SZ(res) );
  YYS( w , res ){
    printf( "%c %d %d\n", w.se, w.fi.fi+1, w.fi.se+1 );
  }
}

int main(){

  int tc = in();
  FOR( i , 1 , tc+1 ){
    solve( i );
  }
  
  return 0;
}
