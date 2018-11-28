//bcw0x1bd2 {{{
#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;
#define FZ(x) memset((x),0,sizeof(x))
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define IOS ios_base::sync_with_stdio(0); cin.tie(0);
#define SZ(x) ((int)((x).size()))
#define ALL(x) begin(x),end(x)
#define REP(i,x) for (int i=0; i<(x); i++)
#define REP1(i,a,b) for (int i=(a); i<=(b); i++)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef long double ld;

#ifdef DARKHH
#define FILEIO(name)
#else
#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
#endif

#ifdef DARKHH
template<typename T>
void _dump( const char* s, T&& head ) { cerr<<s<<"="<<head<<endl; }

template<typename T, typename... Args>
void _dump( const char* s, T&& head, Args&&... tail ) {
  int c=0;
  while ( *s!=',' || c!=0 ) {
    if ( *s=='(' || *s=='[' || *s=='{' ) c++;
    if ( *s==')' || *s==']' || *s=='}' ) c--;
    cerr<<*s++;
  }
  cerr<<"="<<head<<", ";
  _dump(s+1,tail...);
}

#define dump(...) do { \
  fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); \
  _dump(#__VA_ARGS__, __VA_ARGS__); \
} while (0)

template<typename Iter>
ostream& _out( ostream &s, Iter b, Iter e ) {
  s<<"[";
  for ( auto it=b; it!=e; it++ ) s<<(it==b?"":" ")<<*it;
  s<<"]";
  return s;
}

template<typename A, typename B>
ostream& operator <<( ostream &s, const pair<A,B> &p ) { return s<<"("<<p.first<<","<<p.second<<")"; }
template<typename T>
ostream& operator <<( ostream &s, const vector<T> &c ) { return _out(s,ALL(c)); }
template<typename T, size_t N>
ostream& operator <<( ostream &s, const array<T,N> &c ) { return _out(s,ALL(c)); }
template<typename T>
ostream& operator <<( ostream &s, const set<T> &c ) { return _out(s,ALL(c)); }
template<typename A, typename B>
ostream& operator <<( ostream &s, const map<A,B> &c ) { return _out(s,ALL(c)); }
#else
#define dump(...)
#endif
// }}}
// Let's Fight! ~OAO~~

const int MAXN = 105;
const ld INF = 1e20;

int N,M,Q;
ll dis[MAXN][MAXN],E[MAXN],S[MAXN];
int inq[MAXN];
ld dp[MAXN];
pii qry[MAXN];
ld ans[MAXN];

void input() {
  cin>>N>>Q;
  REP(i,N) {
    cin>>E[i]>>S[i];
  }
  REP(i,N) REP(j,N) {
    cin>>dis[i][j];
  }
  REP(i,Q) {
    cin>>qry[i].F>>qry[i].S;
    qry[i].F--;
    qry[i].S--;
  }
}
ld calc(int st, int ed) {
  REP(i,N) {
    dp[i] = INF;
  }
  dp[st] = 0;
  queue<int> que;
  que.push(st);
  inq[st] = 1;
  while (!que.empty()) {
    int u = que.front();
    que.pop();
    REP(v,N) {
      if (dis[u][v] > E[u]) continue;
      if (dp[v] > dp[u] + 1. * dis[u][v] / S[u]) {
        dp[v] = dp[u] + 1. * dis[u][v] / S[u];
        if (!inq[v]) {
          que.push(v);
          inq[v] = 1;
        }
      }
    }
    inq[u] = 0;
  }

  return dp[ed];
}
void solve() {
  REP(i,N) {
    REP(j,N) 
      if (dis[i][j] == -1) dis[i][j] = 1LL<<50;
    dis[i][i] = 0;
  }
  REP(k,N) REP(i,N) REP(j,N)
    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);

  REP(qid,Q) {
    int st = qry[qid].F;
    int ed = qry[qid].S;
    ans[qid] = calc(st, ed);
  }
}
int main() {
  IOS;
  cout<<fixed<<setprecision(10);
  int nT;
  cin>>nT;
  REP1(cas,1,nT) {
    input();
    solve();
    cout<<"Case #"<<cas<<":";
    REP(i,Q) cout<<" "<<ans[i];
    cout<<endl;
  }

  return 0;
}

