#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)

#define pb push_back
#define eb emplace_back

#define fi first
#define se second

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long double ld;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef set<pii> spi;
typedef pair<ld, ld> pld;
typedef vector<ld> vld;
typedef vector<pld> vpld;

const ld eps = 1e-9;
const ld pi = acosl(-1.0);

template<typename T> bool uin(T& a, T b) { if (b < a) { a = b; return true; } return false; }
template<typename T> bool uax(T& a, T b) { if (a < b) { a = b; return true; } return false; }

vector<vi> g, gt;
vb used;
vi order, comp;

void init(int n) {
  g.assign(n*2, vi());
  gt.assign(n*2, vi());
  used.assign(n*2, false);
  order.clear();
  comp.assign(n*2, -1);
}

void add_edge(int x, int y) {
  // cerr << "ae " << x << ' ' << y << '\n';
  g[x].pb(y);
  gt[y].pb(x);
}

void dfs1 (int v) {
  used[v] = true;
  for (size_t i=0; i<g[v].size(); ++i) {
    int to = g[v][i];
    if (!used[to])
      dfs1 (to);
  }
  order.push_back (v);
}

void dfs2 (int v, int cl) {
  comp[v] = cl;
  for (size_t i=0; i<gt[v].size(); ++i) {
    int to = gt[v][i];
    if (comp[to] == -1)
      dfs2 (to, cl);
  }
}

vb sat2() {
  int n = used.size() / 2;
  forn(i, n*2) if (!used[i]) dfs1(i);
  int c = 0;
  ford(i, order.size()) {
    int v = order[i];
    if (comp[v] == -1)
      dfs2(v, c++);
  }
  forn(i, n*2) if (comp[i] == comp[i^1]) return {};
  vb r(n);
  forn(i, n) if (comp[i*2+1] > comp[i*2]) r[i] = 1;
  return r;
}

int di[4] = {-1, 0, 1, 0};
int dj[4] = {0, -1, 0, 1};

bool go(const vs& a, spi& s, int i, int j, int t) {
  while (true) {
    i += di[t]; j += dj[t];
    if (i < 0 || i >= (int)a.size()) break;
    if (j < 0 || j >= (int)a[0].size()) break;
    if (a[i][j] == '#') break;
    if (a[i][j] == '|' || a[i][j] == '-') return false;
    s.emplace(i, j);
    if (a[i][j] == '/') {
      t = 3 - t;
    } else if (a[i][j] == '\\') {
      t ^= 1;
    }
  }
  return true;
}

spi go(const vs& a, int i, int j) {
  spi x;
  x.emplace(i, j);
  if (a[i][j] == '-') {
    if (!go(a, x, i, j, 1)) return {};
    if (!go(a, x, i, j, 3)) return {};
  } else {
    if (!go(a, x, i, j, 0)) return {};
    if (!go(a, x, i, j, 2)) return {};
  }
  return x;
}

bool solve() {
  int R, C;
  cin >> R >> C;
  vs a(R);
  forn(i, R) cin >> a[i];
  vpi pos;
  map<pii, vi> rpos;
  vi consts;
  forn(i, R) forn(j, C) if (a[i][j] == '|' || a[i][j] == '-') {
    a[i][j] = '-';
    auto s0 = go(a, i, j);
    a[i][j] = '|';
    auto s1 = go(a, i, j);

    if (0) {
    cerr << '\n';
    cerr << "s0 " << i << ' ' << j << '\n';
    for(auto& e: s0) cerr << e.fi << ' ' << e.se << '\n';
    cerr << '\n';
    
    cerr << "s1 " << i << ' ' << j << '\n';
    for(auto& e: s1) cerr << e.fi << ' ' << e.se << '\n';
    cerr << '\n';
    }

    if (s0.empty() && s1.empty()) return false;
    if (s0.empty()) consts.eb(pos.size()*2+1);
    if (s1.empty()) consts.eb(pos.size()*2);
    for(auto& e: s0) rpos[e].pb(pos.size()*2);
    for(auto& e: s1) rpos[e].pb(pos.size()*2+1);
    pos.eb(i, j);
  }
  init(pos.size());
  for(auto& e: consts) {
    add_edge(e^1, e);
  }
  // cerr << "init " << pos.size() << '\n';
  forn(i, R) forn(j, C) if (a[i][j] == '.') {
    auto& r = rpos[pii(i, j)];
    if (r.empty()) return false;
    if (r.size() == 1) {
      int idx = r[0];
      add_edge(idx^1, idx);
    } else {
      assert(r.size() == 2);
      int idx = r[0], idy = r[1];
      add_edge(idx^1, idy);
      add_edge(idy^1, idx);
    }
  }
  auto ans = sat2();
  if (ans.empty()) return false;
  // forn(i, ans.size()) cerr << ans[i] << " \n"[i + 1 == ans.size()];
  forn(i, pos.size()) {
    if (ans[i]) 
      a[pos[i].fi][pos[i].se] = '|';
    else
      a[pos[i].fi][pos[i].se] = '-';
  }
  cout << "POSSIBLE\n";
  forn(i, R) cout << a[i] << '\n';
  return true;
}

int main() {
#ifdef HOME
  // freopen("input.txt", "r", stdin);
#endif
  cout << fixed;
  cout.precision(15);
  int T;
  // cerr << can({2, 0}, 1, T) << ' ' << T << '\n'; return 0;
  cin >> T;
  forn(t, T) {
    cout << "Case #" << t + 1 << ": ";
    if (!solve()) cout << "IMPOSSIBLE\n";
  }
  return 0;
}
