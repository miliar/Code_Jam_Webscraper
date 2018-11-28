#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <bits/stdc++.h>

using namespace std;

mt19937 mrand(random_device{} ()); 

int rnd(int x) {
  return mrand() % x;
}

typedef long double ld;
typedef long long ll;

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#else
#define eprintf(...) ;
#endif

#define pb push_back
#define mp make_pair
#define sz(x) ((int) (x).size())
#define TASK "text"

const int inf = (int) 1.01e9;
const ld eps = 1e-9;
const ld pi = acos((ld) -1.0);

const int mod = (int) 1e9 + 7;

void add(int &x, int y) {
  if ((x += y) >= mod) {
    x -= mod;
  }
}

int mult(int x, int y) {
  return (long long) x * y % mod;
}

int power(int x, int pw) {
  int res = 1;
  for (; pw; pw >>= 1) {
    if (pw & 1) {
      res = mult(res, x);
    }
    x = mult(x, x);
  }
  return res;
}

void precalc() {
}

const int maxn = 210;
int ans0[maxn][maxn];
int ans[maxn][maxn];

int n, m;

int read() {
  if (scanf("%d%d", &n, &m) < 2) {
    return 0;
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      ans[i][j] = 0;
    }
  }
  for (int i = 0; i < m; ++i) {
    char ch;
    int x, y;
    scanf(" %c%d%d", &ch, &x, &y);
    --x, --y;
    if (ch != '+') {
      ans[x][y] |= 1;
    }
    if (ch != 'x') {
      ans[x][y] |= 2;
    }
  }
  return 1;
}

int cool[2][2 * maxn];
int pr[2 * maxn];
vector<vector<int> > es;

int used[2 * maxn];
int maxu = 0;

int dfs(int v) {
  used[v] = maxu;
  for (int u : es[v]) {
    if (cool[1][u]) {
      continue;
    }
    if (pr[u] == -1 || (used[pr[u]] < maxu && dfs(pr[u]))) {
      pr[u] = v;
      return 1;
    }
  }
  return 0;
}

int findBrides(int n, vector<pair<int, int> > edges, vector<pair<int, int> > &q) {
  for (int i = 0; i < n; ++i) {
    cool[0][i] = cool[1][i] = 0;
    pr[i] = -1;
  }
  for (auto p : q) {
    pr[p.second] = p.first;
  }
  es = vector<vector<int> >(n);
  for (auto p : edges) {
    es[p.first].pb(p.second);
  }
  for (int i = 0; i < sz(q); ++i) {
    cool[0][q[i].first] = 1;
    cool[1][q[i].second] = 1;
  }

  for (int i = 0; i < n; ++i) {
    if (cool[0][i]) {
      continue;
    }
    ++maxu;
    dfs(i);
  }
  for (int i = 0; i < n; ++i) {
    if (cool[1][i]) {
      continue;
    }
    int j = pr[i];
    if (j == -1) {
      continue;
    }
    q.pb(mp(j, i));
  }
  return sz(q);
}


void solve() {
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      ans0[i][j] = ans[i][j];
    }
  }

  int res = 0;
  {
    vector<pair<int, int> > edges;
    vector<pair<int, int> > q;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        auto cur = mp(i, j);
        edges.pb(cur);
        if (ans0[i][j] & 1) {
          q.pb(cur);
        }
      }
    }
    res += findBrides(n, edges, q);
    for (auto cur : q) {
      ans[cur.first][cur.second] |= 1;
    }
  }
  {
    vector<pair<int, int> > edges;
    vector<pair<int, int> > q;
    for (int i = 0; i < n; ++i) {
      for (int j = 0; j < n; ++j) {
        auto cur = mp(i - j + (n - 1), i + j);
        edges.pb(cur);
        if (ans0[i][j] & 2) {
          q.pb(cur);
        }
      }
    }
    res += findBrides(n * 2 - 1, edges, q);
    for (auto cur : q) {
      int x = (cur.first + cur.second - (n - 1)) / 2;
      int y = (cur.second - cur.first + (n - 1)) / 2;
      ans[x][y] |= 2;
    }
  }

  vector<pair<int, int> > top;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      if (ans[i][j] != ans0[i][j]) {
        top.pb(mp(i, j));
      }
    }
  }

  char chs[] = ".x+o";

  printf("%d %d\n", res, sz(top));
  for (int i = 0; i < sz(top); ++i) {
    printf("%c %d %d\n", chs[ans[top[i].first][top[i].second]], top[i].first + 1, top[i].second + 1);
  }
}

int main() {
  precalc();
#ifdef LOCAL
  freopen(TASK ".out", "w", stdout);
  assert(freopen(TASK ".in", "r", stdin));
#endif

  int t;
  scanf("%d", &t);
  t = 0;
  while (1) {
    if (!read()) {
      break;
    }
    printf("Case #%d: ", ++t);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}
