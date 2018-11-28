#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define pb push_back
#define sz(s) ((int) ((s).size()))

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#else
#define eprintf(...) ;
#endif

typedef long long ll;
typedef long double ld;

const int inf = (int) 1.01e9;
const ld eps = 1e-11;
const ld pi = acos(-1.0L);

mt19937 mrand(random_device{} ());
int rnd(int x) {
  return mrand() % x;
}

const int mod = (int) 1e9 + 7;

void add(int & x, int y) {
  if ((x += y) >= mod) {
    x -= mod;
  }
}

int sum(int x, int y) {
  add(x, y);
  return x;
}

int mult(int x, int y) {
  return (ll) x * y % mod;
}

int power(int x, ll p) {
  int res = 1;
  while (p) {
    if (p & 1) {
      res = mult(res, x);
    }
    x = mult(x, x);
    p >>= 1;
  }
  return res;
}

int inv(int x) {
  return power(x, mod - 2);
}

void precalc() {
}

const int maxn = 55;
int n, m;
char s[maxn][maxn];

int gox[4] = {1, 0, -1, 0};
int goy[4] = {0, 1, 0, -1};

bool read() {
  if (scanf("%d%d", &n, &m) < 2) {
    return false;
  }
  for (int i = 0; i < n; i++) {
    scanf("%s", s + i);
  }
  return true;
}

bool inside(int x, int y) {
  return 0 <= x && x < n && 0 <= y && y < m;
}

vector<int> goes[maxn][maxn][2];

int mirror(int dir, int i, int j) {
  if (s[i][j] == '.') {
    return dir;
  }
  if (s[i][j] == '/') {
    return dir ^ 3;
  }
  if (s[i][j] == '\\') {
    return dir ^ 1;
  }
  assert(0);
}

vector<vector<int> > g;
vector<vector<int> > rg;

vector<int> perm;
const int maxm = 1e6;
int used[maxm];
int cols[maxm];

void dfs(int v) {
  if (used[v]) {
    return;
  }
  used[v] = 1;
  for (auto to : g[v]) {
    dfs(to);
  }
  perm.pb(v);
}

int curc;

void dfs2(int v) {
  if (cols[v] >= 0) {
    return;
  }
  cols[v] = curc;
  for (auto to : rg[v]) {
    dfs2(to);
  }
}

void solve() {
  int cnt = 0;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      goes[i][j][0].clear();
      goes[i][j][1].clear();
    }
  }
  g.clear();
  vector<pair<int, int> > v;
  for (int i0 = 0; i0 < n; i0++) {
    for (int j0 = 0; j0 < m; j0++) {
      if (s[i0][j0] == '-' || s[i0][j0] == '|') {
        v.pb({i0, j0});
        g.pb(vector<int> ());
        g.pb(vector<int> ());
        for (int it = 0; it < 2; it++) {
          //eprintf("%d %d %d\n", i0, j0, it);
          bool fail = false;
          for (int it2 = 0; it2 < 2; it2++) {
            int x = i0, y = j0;
            int dir = it + 2 * it2;
            while (true) {
              x += gox[dir];
              y += goy[dir];
              //eprintf("x = %d, y = %d\n", x, y);
              if (s[x][y] == '#') {
                break;
              }
              if (!inside(x, y)) {
                break;
              }
              if (s[x][y] == '.') {
                goes[x][y][dir & 1].pb(cnt * 2 + it);
              }
              if (s[x][y] == '|' || s[x][y] == '-') {
                fail = true;
                break;
              }
              dir = mirror(dir, x, y);
            }
          }
          if (fail) {
            //eprintf("%d %d %d\n", i0, j0, it);
            g[cnt * 2 + it].pb(cnt * 2 + !it);
          }
        }
        cnt++;
      }
    }
  }
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
      if (s[i][j] == '.') {
        vector<int> v0 = goes[i][j][0];
        vector<int> v1 = goes[i][j][1];
        if (sz(v0) == 2) {
          v0.clear();
        }
        if (sz(v1) == 2) {
          v1.clear();
        }
        vector<int> v;
        for (auto i : v0) {
          v.pb(i);
        }
        for (auto i : v1) {
          v.pb(i);
        }
        if (sz(v) == 0) {
          printf("IMPOSSIBLE\n");
          return;
        } else if (sz(v) == 1) {
          g[v[0] ^ 1].pb(v[0]);
        } else {
          assert(sz(v) == 2);
          g[v[0] ^ 1].pb(v[1]);
          g[v[1] ^ 1].pb(v[0]);
        }
      }
    }
  }
  rg.clear();
  rg.resize(sz(g));
  for (int i = 0; i < sz(g); i++) {
    for (int j = 0; j < sz(g[i]); j++) {
      rg[g[i][j]].pb(i);
    }
  }
  memset(used, 0, sizeof(used));
  memset(cols, -1, sizeof(cols));
  perm.clear();
  for (int i = 0; i < cnt * 2; i++) {
    if (!used[i]) {
      dfs(i);
    }
  }
  reverse(perm.begin(), perm.end());
  curc = 0;
  for (auto i : perm) {
    dfs2(i);
    curc++;
  }
  for (int i = 0; i < cnt; i++) {
    if (cols[i * 2] == cols[i * 2 + 1]) {
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  vector<int> res(cnt);
  for (int i = 0; i < cnt; i++) {
    if (cols[i * 2] < cols[i * 2 + 1]) {
      res[i] = 1;
    } else {
      res[i] = 0;
    }
  }
  for (int i = 0; i < cnt; i++) {
    s[v[i].first][v[i].second] = res[i] ? '-' : '|';
  }
  printf("POSSIBLE\n");
  for (int i = 0; i < n; i++) {
    printf("%s\n", s[i]);
  }
}

int main() {
  precalc();
#ifdef DEBUG
  assert(freopen("text.in", "r", stdin));
  assert(freopen("text.out", "w", stdout));
#endif

  int t;
  scanf("%d", &t);
  t = 0;
  while (read()) {
    printf("Case #%d: ", ++t);
    solve();
#ifdef DEBUG
    eprintf("Time: %.3f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}

