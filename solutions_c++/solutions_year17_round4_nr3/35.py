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
#define dame { puts("IMPOSSIBLE"); return;}
#define show(x) cout<<#x<<" = "<<x<<endl;
#define PQ(T) priority_queue<T,vector<T>,greater<T> >
#define bn(x) ((1<<x)-1)
#define newline puts("")
#define v(T) vector<T>
#define vv(T) vector<vector<T>>
using namespace std;
typedef long long ll;
typedef unsigned uint;
typedef unsigned long long ull;
typedef pair<int,int> P;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<ll> vl;
typedef vector<P> vp;
typedef vector<vp> vvp;
inline int in() { int x; scanf("%d",&x); return x;}
inline void priv(vi a) { rep(i,sz(a)) printf("%d%c",a[i],i==sz(a)-1?'\n':' ');}
template<typename T>istream& operator>>(istream&i,vector<T>&v)
{rep(j,sz(v))i>>v[j];return i;}
template<typename T>string join(const vector<T>&v)
{stringstream s;rep(i,sz(v))s<<' '<<v[i];return s.str().substr(1);}
template<typename T>ostream& operator<<(ostream&o,const vector<T>&v)
{if(sz(v))o<<join(v);return o;}
template<typename T1,typename T2>istream& operator>>(istream&i,pair<T1,T2>&v)
{return i>>v.fi>>v.se;}
template<typename T1,typename T2>ostream& operator<<(ostream&o,const pair<T1,T2>&v)
{return o<<v.fi<<","<<v.se;}
const int MX = 100005, INF = 1001001001;
const ll LINF = 1e18;
const double eps = 1e-10;
typedef vector<string> vs;
const int di[] = {-1,0,1,0}, dj[] = {0,-1,0,1}; //^<v>
//const int di[] = {-1,0,1,-1,1,-1,0,1}, dj[] = {-1,-1,-1,0,0,1,1,1};

// 2-SAT
// SCC
struct scc {
  int n, k;
  vvi to, ot, d, gt; // to, rev_to, groups, group_to
  vi g, used, kv; // group, gomi, topo_ord
  scc(int n=0):n(n),to(n),ot(n){}
  int inc() { to.pb(vi()); ot.pb(vi()); return n++;}
  void add(int a, int b) { to[a].pb(b); ot[b].pb(a);}
  void dfs(int v) {
    if (used[v]) return;
    used[v] = 1;
    rep(i,sz(to[v])) dfs(to[v][i]);
    kv[--k] = v;
  }
  void rfs(int v) {
    if (g[v] != -1) return;
    g[v] = k; d[k].pb(v);
    rep(i,sz(ot[v])) rfs(ot[v][i]);
  }
  void init() {
    k = n;
    used = kv = vi(n);
    g = vi(n,-1);
    rep(i,n) dfs(i);
    rep(i,n) if (g[kv[i]] == -1)  {
      d.pb(vi());
      rfs(kv[i]);
      k++;
    }
    gt = vvi(k);
    rep(i,n)rep(j,sz(ot[i])) {
      int v = g[ot[i][j]], u = g[i];
      if (v != u) gt[v].pb(u);
    }
    rep(i,k) {
      sort(rng(gt[i]));
      gt[i].erase(unique(rng(gt[i])),gt[i].end());
    }
  }
};
//
struct sat {
  int n, n2;
  scc g;
  vi d;
  sat() {}
  sat(int n):n(n),n2(n*2),g(n2),d(n2,1) {}
  int inv(int a) { return n2-1-a;}
  void add(int a, int b) {
    // cerr<<a<<" "<<b<<endl;
    g.add(inv(a),b); g.add(inv(b),a);
  }
  bool solve() {
    g.init();
    rep(i,n) if (g.g[i] == g.g[inv(i)]) return false;
    // todo: verify
    drep(i,g.k) {
      int r = 1;
      rep(j,sz(g.gt[i])) {
        int u = g.gt[i][j];
        r &= d[g.d[u][0]];
      }
      rep(j,sz(g.d[i])) {
        int v = g.d[i][j];
        r &= d[v];
      }
      rep(j,sz(g.d[i])) {
        int v = g.d[i][j];
        d[v] = r; d[inv(v)] = !r;
      }
    }
    //
    // cerr<<d<<endl;
    return true;
  }
};
//

struct Solver {
  void solve() {
    int h,w;
    scanf("%d%d",&h,&w);
    vs s(h);
    rep(i,h) cin >> s[i];
    vvi si(h,vi(w,-1));
    vvi ti(h,vi(w,-1));
    int ss = 0, ts = 0;
    vp sp, tp;
    rep(i,h)rep(j,w) {
      if (s[i][j] == '|' || s[i][j] == '-') ti[i][j] = ts++, tp.pb(P(i,j));
      if (s[i][j] == '.') si[i][j] = ss++, sp.pb(P(i,j));
    }
    vvvi tx(ts,vvi(2));
    vvp sx(ss);
    vi ng(1,-1); vvi ngs(2,ng);
    rep(k,ts) {
      rep(v,4) {
        int i = tp[k].fi, j = tp[k].se;
        int u = v;
        while (1) {
          i += di[u]; j += dj[u];
          if (i<0||j<0||i>=h||j>=w) break;
          if (s[i][j] == '#') break;
          if (si[i][j] != -1) {
            tx[k][v&1].pb(si[i][j]);
          } else if (ti[i][j] != -1) {
            tx[k][v&1].pb(-1);
            break;
          } else if (s[i][j] == '/') {
            u ^= 3;
          } else if (s[i][j] == '\\') {
            u ^= 1;
          } else assert(false);
        }
      }
      rep(i,2) {
        sort(rng(tx[k][i]));
        if (sz(tx[k][i]) && tx[k][i][0] == -1) tx[k][i] = ng;
        else {
          for (int j : tx[k][i]) {
            sx[j].pb(P(k,i));
          }
        }
        // cerr<<tx[k][i]<<endl;
      }
      if (tx[k] == ngs) dame;
    }
    sat g(ts);
    auto ft = [&](P p) {
      if (p.se) return g.inv(p.fi);
      return p.fi;
    };
    rep(i,ss) {
      if (sz(sx[i]) == 0) dame;
      assert(sz(sx[i]) <= 2);
      if (sz(sx[i]) == 1) sx[i].pb(sx[i][0]);
      int a = ft(sx[i][0]);
      int b = ft(sx[i][1]);
      g.add(a,b);
    }
    // cerr<<ts<<endl;
    rep(i,ts) {
      if (tx[i][0] == ng) g.add(g.inv(i),g.inv(i));
      if (tx[i][1] == ng) g.add(i,i);
    }
    if (!g.solve()) dame;
    rep(k,ts) {
      int i = tp[k].fi, j = tp[k].se;
      if (g.d[k]) {
        s[i][j] = '|';
      } else {
        s[i][j] = '-';
      }
    }
    cout<<"POSSIBLE"<<endl;
    rep(i,h) cout<<s[i]<<endl;
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




















