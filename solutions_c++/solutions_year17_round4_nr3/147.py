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

struct Scc{
  static const int MXN = 100005;
  int n, nScc, vst[MXN], bln[MXN];
  vector<int> E[MXN], rE[MXN], vec;
  void init(int _n){
    n = _n;
    for (int i=0; i<n; i++){
      E[i].clear();
      rE[i].clear();
    }
  }
  void add_edge(int u, int v){
    E[u].PB(v);
    rE[v].PB(u);
  }
  void DFS(int u){
    vst[u]=1;
    for (auto v : E[u])
      if (!vst[v]) DFS(v);
    vec.PB(u);
  }
  void rDFS(int u){
    vst[u] = 1;
    bln[u] = nScc;
    for (auto v : rE[u])
      if (!vst[v]) rDFS(v);
  }
  void solve(){
    nScc = 0;
    vec.clear();
    for (int i=0; i<n; i++) vst[i] = 0;
    for (int i=0; i<n; i++)
      if (!vst[i]) DFS(i);
    reverse(vec.begin(),vec.end());
    for (int i=0; i<n; i++) vst[i] = 0;
    for (auto v : vec){
      if (!vst[v]){
        rDFS(v);
        nScc++;
      }
    }
  }
} scc;

using A34 = array<int,3>;
const int dir[4][2] = {{-1,0},{0,1},{1,0},{0,-1}};
const int V = 1;
const int H = 2;
const int MAXN = 55*55;

int R,C;
int may[55][55],vst[55][55][4];
A34 arr[55][55][3];
int trans[2][4];
int gg[55][55][3];
vector<pii> vec[55][55][3];
string mp[55];
int fr,bk,que[MAXN*100];
int cov[55][55];

void input() {
  cin>>R>>C;
  REP(i,R) cin>>mp[i];
}

int getid(int i, int j) { return i * C + j; }
int isBeam(int i, int j) { return mp[i][j] == '|' or mp[i][j] == '-'; }
int isp(int i, int j) { return mp[i][j] == '.'; }

vector<pii> go(int stx, int sty, int d1, int d2, int stdir) {
  memset(vst,0,sizeof(vst));
  //vst[stx][sty][d1] = 1;
  //vst[stx][sty][d2] = 1;
  fr = bk = 0;
  que[bk++] = d1; que[bk++] = stx; que[bk++] = sty;
  que[bk++] = d2; que[bk++] = stx; que[bk++] = sty;
  while (fr < bk) {
    int d = que[fr++];
    int x = que[fr++];
    int y = que[fr++];
    int nx = x + dir[d][0];
    int ny = y + dir[d][1];
    if (nx < 0 or nx >= R or ny < 0 or ny >= C) continue;
    if (vst[nx][ny][d]) continue;
    if (mp[nx][ny] == '#') continue;

    if (mp[nx][ny] == '/') d = trans[0][d];
    if (mp[nx][ny] == '\\') d = trans[1][d];

    vst[nx][ny][d] = 1;
    que[bk++] = d; que[bk++] = nx; que[bk++] = ny;
  }

  vector<pii> res;
  REP(i,R) REP(j,C) {
    int ok = 0;
    REP(k,4) ok |= vst[i][j][k];
    if (ok) {
      res.PB({i,j});
      if (vst[i][j][0] or vst[i][j][2]) {
        arr[i][j][V] = A34{stx,sty,stdir};
      }
      if (vst[i][j][1] or vst[i][j][3]) {
        arr[i][j][H] = A34{stx,sty,stdir};
      }
    }
  }

  return res;
}
void gen(int stx, int sty) {
  vec[stx][sty][V] = go(stx, sty, 0, 2, V);
  vec[stx][sty][H] = go(stx, sty, 1, 3, H);
}
int N, NV;
int dif(int x) {
  if (x < N) return x + N;
  return x - N;
}
void solve(int cas) {
  N = R * C;
  NV = N * 2;
  scc.init(NV);

  REP(i,R) REP(j,C) {
    arr[i][j][V] = {-1,-1,-1};
    arr[i][j][H] = {-1,-1,-1};
  }

  memset(may,0,sizeof(may));
  REP(i,R) {
    REP(j,C) {
      vec[i][j][V].clear();
      vec[i][j][H].clear();
      gg[i][j][V] = gg[i][j][H] = 0;
      if (isBeam(i,j)) {
        gen(i,j);

        may[i][j] = V | H;

        int id = getid(i,j);
        for (auto it:vec[i][j][V]) {
          if (isBeam(it.F, it.S)) {
            scc.add_edge(id, id+N);
            may[i][j] &= H;
            break;
          }
        }

        for (auto it:vec[i][j][H]) {
          if (isBeam(it.F, it.S)) {
            scc.add_edge(id+N, id);
            may[i][j] &= V;
            break;
          }
        }
      }
    }
  }


  int fail = 0;
  REP(i,R) REP(j,C) {
    if (isp(i,j)) {
      if (arr[i][j][V][0] == -1 and arr[i][j][H][0] == -1) {
        fail = 1;
      } else if (arr[i][j][H][0] == -1) {
        int a = getid(arr[i][j][V][0], arr[i][j][V][1]);
        if (arr[i][j][V][2] == H) a += N;

        scc.add_edge(dif(a), a);
      } else if (arr[i][j][V][0] == -1) {
        int a = getid(arr[i][j][H][0], arr[i][j][H][1]);
        if (arr[i][j][H][2] == H) a += N;

        scc.add_edge(dif(a), a);
      } else {
        int a = getid(arr[i][j][V][0], arr[i][j][V][1]);
        int b = getid(arr[i][j][H][0], arr[i][j][H][1]);
        if (arr[i][j][V][2] == H) a += N;
        if (arr[i][j][H][2] == H) b += N;
        scc.add_edge(dif(b), a);
        scc.add_edge(dif(a), b);
      }
    }
  }
  scc.solve();
  REP(i,N) if (scc.bln[i] == scc.bln[i+N]) fail = 1;

  memset(cov,0,sizeof(cov));
  if (fail) {
    cout<<"Case #"<<cas<<": IMPOSSIBLE"<<endl;
  } else {
    cout<<"Case #"<<cas<<": POSSIBLE"<<endl;
    REP(i,R) {
      REP(j,C) {
        if (isBeam(i,j)) {
          int a = getid(i,j);
          int b = a + N;
          if (scc.bln[a] > scc.bln[b]) {
            cout<<"|";
            for (auto it:vec[i][j][V]) cov[it.F][it.S] = 1;
          } else {
            cout<<"-";
            for (auto it:vec[i][j][H]) cov[it.F][it.S] = 1;
          }
        } else {
          cout<<mp[i][j];
        }
      }
      cout<<endl;
    }
    REP(i,R) REP(j,C) {
      if (isBeam(i,j)) assert(!cov[i][j]);
      if (isp(i,j)) {
        assert(cov[i][j]);
      }
    }
  }
}
int main() {
  trans[0][0] = 1;
  trans[0][1] = 0;
  trans[0][2] = 3;
  trans[0][3] = 2;
  trans[1][0] = 3;
  trans[1][1] = 2;
  trans[1][2] = 1;
  trans[1][3] = 0;
  IOS;
  int nT;
  cin>>nT;
  REP1(cas,1,nT) {
    input();
    solve(cas);
  }

  return 0;
}

