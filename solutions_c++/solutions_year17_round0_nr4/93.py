//a34021501 {{{
#include<bits/stdc++.h>
#include<unistd.h>
using namespace std;
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

#ifdef HAO123
#define FILEIO(name)
#else
#define FILEIO(name) \
  freopen(name".in", "r", stdin); \
  freopen(name".out", "w", stdout);
#endif

#ifdef HAO123
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
// Let's Fight! !111111111!

typedef pair<int, int> pii;

const int MAXN = 405;

int N, M;
bool xu[MAXN], yu[MAXN], xpyu[MAXN], _xmyu[MAXN*2];
bool hasp[MAXN][MAXN], hasx[MAXN][MAXN], hasnew[MAXN][MAXN];
bool *xmyu;

struct Dinic{
  static const int MXN = 10000;
  struct Edge{ int v,f,re; };
  int n,s,t,level[MXN];
  vector<Edge> E[MXN];
  void init(int _n, int _s, int _t){
    n = _n; s = _s; t = _t;
    for (int i=0; i<n; i++) E[i].clear();
  }
  void add_edge(int u, int v, int f){
    E[u].PB({v,f,SZ(E[v])});
    E[v].PB({u,0,SZ(E[u])-1});
  }
  bool BFS(){
    for (int i=0; i<n; i++) level[i] = -1;
    queue<int> que;
    que.push(s);
    level[s] = 0;
    while (!que.empty()){
      int u = que.front(); que.pop();
      for (auto it : E[u]){
        if (it.f > 0 && level[it.v] == -1){
          level[it.v] = level[u]+1;
          que.push(it.v);
        }
      }
    }
    return level[t] != -1;
  }
  int DFS(int u, int nf){
    if (u == t) return nf;
    int res = 0;
    for (auto &it : E[u]){
      if (it.f > 0 && level[it.v] == level[u]+1){
        int tf = DFS(it.v, min(nf,it.f));
        res += tf; nf -= tf; it.f -= tf;
        E[it.v][it.re].f += tf;
        if (nf == 0) return res;
      }
    }
    if (!res) level[u] = -1;
    return res;
  }
  int flow(int res=0){
    while ( BFS() )
      res += DFS(s,2147483647);
    return res;
  }
}flow;

int calc()
{
  int ret = 0;

  int V = 2*N+2;
  int S = V-2, T = V-1;
  flow.init(V, S, T);

  for(int x=0; x<N; x++)
    flow.add_edge(S, x, 1);
  for(int y=0; y<N; y++)
    flow.add_edge(N+y, T, 1);

  for(int x=0; x<N; x++)
  {
    if(xu[x]) continue;
    for(int y=0; y<N; y++)
    {
      if(yu[y]) continue;
      flow.add_edge(x, N+y, 1);
    }
  }

  ret += flow.flow();

  for(int i=0; i<N; i++)
  {
    for(auto e: flow.E[i])
    {
      int v = e.v;
      if(N <= v and v < 2*N and e.f == 0)
        hasx[i][v-N] = hasnew[i][v-N] = true;
    }
  }

  V = 4*N;
  S = V-2, T = V-1;
  flow.init(V, S, T);

  for(int i=0; i<2*N-1; i++)
    flow.add_edge(S, i, 1);
  for(int i=0; i<2*N-1; i++)
    flow.add_edge((2*N-1)+i, T, 1);

  for(int x=0; x<N; x++)
  {
    for(int y=0; y<N; y++)
    {
      int a = x+y, b = x-y;
      if(xpyu[a] or xmyu[b]) continue;
      flow.add_edge(a, (2*N-1)+(N-1)+b, 1);
    }
  }

  ret += flow.flow();

  for(int i=0; i<2*N-1; i++)
  {
    for(auto e: flow.E[i])
    {
      int v = e.v;
      if(2*N-1 <= v and v < 4*N-2 and e.f == 0)
      {
        int a = i, b = v - (2*N-1) - (N-1);
        assert(abs(a-b)%2 == 0);
        int x = (a+b)/2, y = (a-b)/2;
        hasp[x][y] = hasnew[x][y] = true;
      }
    }
  }

  return ret;
}

int main() {
  IOS;
  xmyu = _xmyu + MAXN;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    for(int i=0; i<MAXN; i++)
    {
      xu[i] = yu[i] = xpyu[i] = _xmyu[i] = _xmyu[MAXN+i] = false;
      for(int j=0; j<MAXN; j++)
        hasp[i][j] = hasx[i][j] = hasnew[i][j] = false;
    }

    cin>>N>>M;
    int ans = 0;
    for(int i=0; i<M; i++)
    {
      string s;
      int x, y;
      cin>>s>>x>>y;
      x--;
      y--;
      char c = s[0];

      if(c == 'x' or c == 'o')
      {
        ans++;
        xu[x] = yu[y] = true;
        hasx[x][y] = true;
      }
      if(c == '+' or c == 'o')
      {
        ans++;
        xpyu[x+y] = xmyu[x-y] = true;
        hasp[x][y] = true;
      }
    }
    ans += calc();

    vector<pii> vnew;
    for(int i=0; i<N; i++)
      for(int j=0; j<N; j++)
        if(hasnew[i][j])
          vnew.PB({i, j});

    int s = SZ(vnew);

    cout<<"Case #"<<t<<": "<<ans<<" "<<s<<endl;
    for(auto p: vnew)
    {
      int x = p.F, y = p.S;
      if(hasp[x][y] and hasx[x][y]) cout<<"o";
      else if(hasp[x][y]) cout<<"+";
      else cout<<"x";
      cout<<" "<<x+1<<" "<<y+1<<endl;
    }
  }

  return 0;
}

