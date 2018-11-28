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

const int MAXN = 52;
const int MAXV = 500;
const int dx[4] = {-1, 0, 1, 0};
const int dy[4] = {0, -1, 0, 1};

int R, C, V;
string arr[MAXN];
vector<int> tags[MAXN][MAXN];
int var[MAXN][MAXN];
bool ok[MAXV];
vector<int> edge[MAXV], rdge[MAXV];
bool vis[MAXV];
vector<int> stk;
int snum[MAXV];

bool inrange(int i, int j)
{
  return i >= 0 and i < R and j >= 0 and j < C;
}

bool dfs(int i, int j, int dir, int tag=-1)
{
  if(!inrange(i, j)) return true;
  if(arr[i][j] == '+') return false;
  if(arr[i][j] == '#') return true;
  if(arr[i][j] == '.' and tag != -1)
    tags[i][j].PB(tag);
  
  int ndir = dir;
  if(arr[i][j] == '/')
    ndir = 3 - ndir;
  else if(arr[i][j] == '\\')
    ndir = ndir ^ 1;
  int ni = i + dx[ndir];
  int nj = j + dy[ndir];
  return dfs(ni, nj, ndir, tag);
}

bool dfsz(int i, int j, int dir, int tag=-1)
{
  int ni = i + dx[dir];
  int nj = j + dy[dir];
  return dfs(ni, nj, dir, tag);
}

void dfs2(int v)
{
  if(vis[v]) return;
  vis[v] = true;
  for(auto ch: edge[v])
    dfs2(ch);
  stk.PB(v);
}

void dfs3(int v, int t)
{
  if(vis[v]) return;
  vis[v] = true;
  snum[v] = t;
  for(auto ch: rdge[v])
    dfs3(ch, t);
}

void scc()
{
  for(int i=0; i<2*V; i++)
    for(auto c: edge[i])
      rdge[c].PB(i);

  for(int i=0; i<2*V; i++)
    vis[i] = false;

  stk.clear();
  for(int i=0; i<2*V; i++)
    if(!vis[i])
      dfs2(i);
  reverse(ALL(stk));

  for(int i=0; i<2*V; i++)
    vis[i] = false;
  for(int i=0; i<2*V; i++)
    if(!vis[stk[i]])
      dfs3(stk[i], i);

  //for(int i=0; i<2*V; i++) cout<<i<<" => "<<edge[i]<<endl;
  //cout<<stk<<endl;
  //for(int i=0; i<2*V; i++)
    //cout<<snum[i]<<" ";
  //cout<<endl;
}

bool calc()
{
  for(int i=0; i<R; i++)
  {
    for(int j=0; j<C; j++)
    {
      tags[i][j].clear();
      var[i][j] = -1;
    }
  }
  for(int i=0; i<MAXV; i++)
  {
    ok[i] = true;
    edge[i].clear();
    rdge[i].clear();
  }

  V = 0;
  for(int i=0; i<R; i++)
  {
    for(int j=0; j<C; j++)
    {
      if(arr[i][j] == '+')
      {
        var[i][j] = V;
        if(dfsz(i, j, 0) and dfsz(i, j, 2))
        {
          dfsz(i, j, 0, 2*V);
          dfsz(i, j, 2, 2*V);
        }
        else
          ok[2*V] = false;

        if(dfsz(i, j, 1) and dfsz(i, j, 3))
        {
          dfsz(i, j, 1, 2*V+1);
          dfsz(i, j, 3, 2*V+1);
        }
        else
          ok[2*V+1] = false;

        V++;
      }
    }
  }

  //for(int i=0; i<2*V; i++) cout<<ok[i]<<" ";
  //cout<<endl;

  for(int i=0; i<2*V; i++)
    if(!ok[i])
      edge[i].PB(i^1);

  for(int i=0; i<R; i++)
  {
    for(int j=0; j<C; j++)
    {
      if(arr[i][j] != '.') continue;
      int sz = SZ(tags[i][j]);
      //cout<<i<<" "<<j<<" TAG "<<tags[i][j]<<endl;
      assert(sz <= 2);
      if(sz == 0) return false;
      else if(sz == 1)
      {
        int a = tags[i][j][0];
        edge[a^1].PB(a);
      }
      else
      {
        int a = tags[i][j][0], b = tags[i][j][1];
        edge[a^1].PB(b);
        edge[b^1].PB(a);
      }
    }
  }

  scc();

  for(int i=0; i<2*V; i++)
    if(snum[i] == snum[i^1])
      return false;

  for(int i=0; i<R; i++)
  {
    for(int j=0; j<C; j++)
    {
      if(arr[i][j] != '+') continue;
      int v = var[i][j];
      if(snum[2*v] < snum[2*v+1])
        arr[i][j] = '-';
      else
        arr[i][j] = '|';
    }
  }

  return true;
}

int main() {
  IOS;

  int T;
  cin>>T;
  for(int t=1; t<=T; t++)
  {
    cin>>R>>C;
    for(int i=0; i<R; i++)
    {
      cin>>arr[i];
      for(int j=0; j<C; j++)
        if(arr[i][j] == '-' or arr[i][j] == '|')
          arr[i][j] = '+';
    }

    bool ans = calc();
    cout<<"Case #"<<t<<": ";
    if(ans)
    {
      cout<<"POSSIBLE"<<endl;
      for(int i=0; i<R; i++)
        cout<<arr[i]<<endl;
    }
    else
    {
      cout<<"IMPOSSIBLE"<<endl;
    }
  }

  return 0;
}

