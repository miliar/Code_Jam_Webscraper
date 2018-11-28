#include <cstdio>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <string.h>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <map>
#include <set>
#include <iostream>
#include <sstream>
#include <numeric>
#include <cctype>
#include <bitset>
#include <cassert>
#include <random>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < (n); ++i)
#define rrep(i,n) for(int i = 1; i <= (n); ++i)
#define drep(i,n) for(int i = (n)-1; i >= 0; --i)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcount
#define uni(x) x.erase(unique(rng(x)),x.end())
#define snuke srand((unsigned)clock()+(unsigned)time(NULL));
#define df(x) int x = in()
#define dame { puts("-1"); return;}
#define show(x) cout<<#x<<" = "<<x<<endl;
#define PQ(T) priority_queue<T,vector<T>,greater<T> >
#define bn(x) ((1<<x)-1)
#define newline puts("")
using namespace std;
typedef long long int ll;
typedef pair<int,int> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<P> vp;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}
template<typename T>istream& operator>>(istream&i,vector<T>&v)
{rep(j,sz(v))i>>v[j];return i;}
template<typename T>string join(vector<T>&v)
{stringstream s;rep(i,sz(v))s<<' '<<v[i];return s.str().substr(1);}
template<typename T>ostream& operator<<(ostream&o,vector<T>&v)
{if(sz(v))o<<join(v);return o;}
template<typename T1,typename T2>istream& operator>>(istream&i,pair<T1,T2>&v)
{return i>>v.fi>>v.se;}
template<typename T1,typename T2>ostream& operator<<(ostream&o,pair<T1,T2>&v)
{return o<<v.fi<<","<<v.se;}
const int MX = 100005, INF = 1001001001;
const ll LINF = 1e18;
const double eps = 1e-10;

// Max flow
// !! Be care of double and INF !!
struct Maxflow {
  typedef int TT;
  int n;
  vi to, next, head, dist, it;
  vector<TT> lim;
  Maxflow(){}
  Maxflow(int n):n(n),head(n,-1),it(n){}
  void add(int a, int b, TT c=1) {
    next.pb(head[a]); head[a] = sz(to); to.pb(b); lim.pb(c);
    next.pb(head[b]); head[b] = sz(to); to.pb(a); lim.pb(0); 
  }
  // void add2(int a, int b, int c=1) {
  //   next.pb(head[a]); head[a] = sz(to); to.pb(b); lim.pb(c);
  //   next.pb(head[b]); head[b] = sz(to); to.pb(a); lim.pb(c); 
  // }
  void bfs(int sv) {
    dist = vi(n,INF); // INF !!
    queue<int> q;
    dist[sv] = 0; q.push(sv);
    while (!q.empty()){
      int v = q.front(); q.pop();
      for (int i = head[v]; i != -1; i = next[i]) {
        if (lim[i] && dist[to[i]] == INF) { // double INF !!
          dist[to[i]] = dist[v]+1; q.push(to[i]);
        }
      }
    }
  }
  TT dfs(int v, int tv, TT nf=INF) { // INF !!
    if (v == tv) return nf;
    for (; it[v] != -1; it[v] = next[it[v]]) {
      int u = to[it[v]]; TT f;
      if (!lim[it[v]] || dist[v] >= dist[u]) continue;
      if (f = dfs(u, tv, min(nf, lim[it[v]])), f) { // double !!
        lim[it[v]] -= f;
        lim[it[v]^1] += f;
        return f;
      }
    }
    return 0;
  }
  int solve(int sv, int tv) {
    TT flow = 0, f;
    while (1) {
      bfs(sv);
      if (dist[tv] == INF) return flow; // INF !!
      rep(i,n) it[i] = head[i];
      while (f = dfs(sv,tv), f) flow += f;
    }
  }
};
//


struct Solver {
  void solve() {
    int n,q;
    scanf("%d%d",&n,&q);
    int m = n*2;
    vi s(n), t(n);
    vi xs(m), xt(m);
    vvi d(n,vi(n,4));
    int ans = 0;
    rep(i,q) {
      char c;
      int x,y;
      scanf(" %c%d%d",&c,&x,&y);
      --x; --y;
      if (c != '+') {
        s[x] = 1;
        t[y] = 1;
        d[x][y] |= 1;
        ++ans;
      }
      if (c != 'x') {
        xs[x+y] = 1;
        xt[x-y+n] = 1;
        d[x][y] |= 2;
        ++ans;
      }
    }
    {
      int sv = n+n, tv = sv+1;
      Maxflow g(tv+1);
      rep(i,n)rep(j,n) {
        if (!s[i] && !t[j]) g.add(i,n+j);
      }
      rep(i,n) if (!s[i]) g.add(sv,i);
      rep(i,n) if (!t[i]) g.add(n+i,tv);
      ans += g.solve(sv,tv);
      int id = 0;
      rep(i,n)rep(j,n) {
        if (!s[i] && !t[j]) {
          if (!g.lim[id]) {
            d[i][j] &= 3;
            d[i][j] |= 1;
          }
          id += 2;
        }
      }
    }
    {
      int sv = m+m, tv = sv+1;
      Maxflow g(tv+1);
      rep(i,n)rep(j,n) {
        int a = i+j, b = i-j+n;
        if (!xs[a] && !xt[b]) g.add(a,m+b);
      }
      rep(i,m) if (!xs[i]) g.add(sv,i);
      rep(i,m) if (!xt[i]) g.add(m+i,tv);
      ans += g.solve(sv,tv);
      int id = 0;
      rep(i,n)rep(j,n) {
        int a = i+j, b = i-j+n;
        if (!xs[a] && !xt[b]) {
          if (!g.lim[id]) {
            d[i][j] &= 3;
            d[i][j] |= 2;
          }
          id += 2;
        }
      }
    }
    int cnt = 0;
    rep(i,n)rep(j,n) cnt += !(d[i][j]&4);
    cout<<ans<<" "<<cnt<<endl;
    rep(i,n)rep(j,n) {
      if (d[i][j]&4) continue;
      cout<<" x+o"[d[i][j]]<<" "<<i+1<<" "<<j+1<<endl;
    }
  }
};

int main() {
  int ts;
  scanf("%d",&ts);
  rrep(ti,ts) {
    Solver solver;
    printf("Case #%d: ",ti);
    solver.solve();
  }
  return 0;
}




















