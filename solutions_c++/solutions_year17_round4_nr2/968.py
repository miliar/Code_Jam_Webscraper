#include <bits/stdc++.h>

#define forn(i, n) for (int i = 0; i < int(n); i++)
#define nfor(i, n) for (int i = int(n) - 1; i >= 0; i--)
#define fore(i, l, r) for (int i = int(l); i < int(r); i++)
#define correct(x, y, n, m) (0 <= (x) && (x) < (n) && 0 <= (y) && (y) < (m))
#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define pb(a) push_back(a)
#define mp(x, y) make_pair((x), (y))
#define x first
#define y second

using namespace std;

typedef long long li;
typedef long double ld;
typedef pair<int, int> pti;

template<typename X> inline X abs(const X& a) { return a < 0? -a: a; }
template<typename X> inline X sqr(const X& a) { return a * a; }

template<typename A, typename B> inline ostream& operator<< (ostream& out, const pair<A, B>& p) { return out << "(" << p.x << ", " << p.y << ")"; }
template<typename T> inline ostream& operator<< (ostream& out, const vector<T>& a) { out << "["; forn(i, sz(a)) { if (i) out << ','; out << ' ' << a[i]; } return out << " ]"; }
template<typename T> inline ostream& operator<< (ostream& out, const set<T>& a) { return out << vector<T>(all(a)); }
template<typename X, typename Y> inline ostream& operator<< (ostream& out, const map<X, Y>& a) { return out << vector<pair<X, Y>>(all(a)); }
template<typename T> inline ostream& operator<< (ostream& out, const pair<T*, int>& a) { return out << vector<T>(a.x, a.x + a.y); }

inline ld gett() { return ld(clock()) / CLOCKS_PER_SEC; }

const int INF = int(1e9);
const li INF64 = li(1e18);
const ld EPS = 1e-9, PI = 3.1415926535897932384626433832795;

#ifdef SU1
//#define GEN
#ifndef GEN
#define LOG
#endif
#endif

const int N = 1010;

int n, c, m;
vector<int> pos[N];

bool read() {
  if (!(cin >> n >> c >> m)) return false;
  forn(i, c) pos[i].clear();
  forn(i, m) {
    int x, y;
    assert(scanf("%d%d", &x, &y) == 2);
    x--, y--;
    pos[y].pb(x);
  }
  return true;
}

int u, used[N][N];
set<int> z[N];

vector<bool> us;
int p[N], pa[N];
vector<pti> g[N];

bool kuhn(int v) {
  if (us[v]) return false;
  us[v] = true;

  for (auto e : g[v]) {
    auto to = e.x;
    if (p[to] == -1 || kuhn(p[to])) {
      p[to] = v;
      pa[to] = e.y;
      return true;
    }
  }
  return false;
}

int process(int cnt, int cust) {
  auto& pos = ::pos[cust];

  forn(i, sz(pos)) {
    g[i].clear();
    forn(j, cnt)
      if (used[j][pos[i]] != u)
        g[i].pb(mp(j, pos[i]));
  }

  memset(p, -1, sizeof(p));
  vector<int> pos2;
  forn(i, sz(pos)) {
    us.assign(cnt, false);
    if (!kuhn(i)) pos2.pb(pos[i]);
  }
  forn(j, cnt)
    if (p[j] != -1) {
      used[j][pa[j]] = u;
      assert(z[j].erase(pa[j]));
    }

#ifdef LOG
  //clog << "pos2: " << pos2 << endl;
#endif
  forn(i, sz(pos2)) {
    g[i].clear();
    forn(j, cnt) {
      if (p[j] != -1) continue;
      auto it = z[j].lower_bound(pos2[i]);
      if (it != z[j].end()) assert(*it != pos2[i]);
      if (it == z[j].begin()) continue;
      auto np = *--it;
      g[i].pb(mp(j, np));
    }
  }

  memset(p, -1, sizeof(p));
  int ans = 0;
  forn(i, sz(pos2)) {
    us.assign(cnt, false);
    if (!kuhn(i)) return -1;
    ans++;
  }
  forn(j, cnt)
    if (p[j] != -1) {
      used[j][pa[j]] = u;
      assert(z[j].erase(pa[j]));
    }
  return ans;
}

int check(int cnt) {
  u++;
  forn(i, cnt) {
    z[i].clear();
    forn(j, n) z[i].insert(j);
  }

  int ans = 0;
  forn(i, c) {
    int cur = process(cnt, i);
    if (cur == -1) return -1;
    ans += cur;
  }
  return ans;
}

void solve(int test) {
  printf("Case #%d: ", test + 1);

  //clog << check(1) << endl;
  //exit(0);

  int lf = 1, rg = m;
  while (lf != rg) {
    int md = (lf + rg) >> 1;
    int val = check(md);
    if (val == -1) lf = md + 1;
    else rg = md;
#ifdef LOG
    //clog << endl;
#endif
  }

  int res = check(lf);
  assert(res != -1);
  cout << lf << " " << res << endl;
}

int main() {
#ifdef SU1
  assert(freopen("input.txt", "rt", stdin));
  assert(freopen("output.txt", "wt", stdout));
#endif

  cout << setprecision(10) << fixed;
  cerr << setprecision(5) << fixed;

  int tc;
  cin >> tc;
  forn(tt, tc) {
    assert(read());
    ld stime = gett();
    solve(tt);
#ifdef SU1
    cerr << "Time: " << gett() - stime << endl;
#endif
    //break;
  }

  return 0;
}

