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


const int maxn = 550;
char s[maxn][maxn];
int n, m;

int read() {
  if (scanf("%d%d", &n, &m) < 2) {
    return 0;
  }
  for (int i = 0; i < n; ++i) {
    scanf("%s", s[i]);
  }
  return 1;
}

const int gox[] = {1, 0, -1, 0};
const int goy[] = {0, 1, 0, -1};


pair<int, int> used[maxn][maxn][2];

bool inside(int x, int y) {
  return 0 <= x && x < n && 0 <= y && y < m;
}

vector<vector<int> > es, esrev;

const int maxcnt = 1100;
bool isok[maxcnt][2];


const int maxv = maxcnt * 2;
int was[maxv];

int ans[maxcnt];

int perm[maxv];

int pk;

void dfs(int v) {
  was[v] = 1;
  for (int u : es[v]) {
    if (was[u]) {
      continue;
    }
    dfs(u);
  }
  perm[pk++] = v;
}

int col[maxv];

void dfs2(int v, int maxc) {
  col[v] = maxc;
  was[v] = 1;
  for (int u : esrev[v]) {
    if (was[u]) {
      continue;
    }
    dfs2(u, maxc);
  }
}

bool getans() {
  int n = sz(es);
  esrev = vector<vector<int> >(n);

  vector<pair<int, int> > toadd;
  for (int i = 0; i < n; ++i) {
    for (int j : es[i]) {
      toadd.pb(mp(i, j));
    }
  }
  for (auto p : toadd) {
    es[p.second ^ 1].pb(p.first ^ 1);
  }

  for (int i = 0; i < n; ++i) {
    was[i] = 0;
    for (int j : es[i]) {
      esrev[j].pb(i);
    }
  }
  pk = 0;
  for (int i = 0; i < n; ++i) {
    if (was[i]) {
      continue;
    }
    dfs(i);
  }
  for (int i = 0; i < n; ++i) {
    was[i] = 0;
  }
  assert(pk == n);
  int maxc = 0;
  for (int i = n - 1; i >= 0; --i) {
    int v = perm[i];
    if (was[v]) {
      continue;
    }
    dfs2(v, maxc);
    ++maxc;
  }

  for (int i = 0; i < n / 2; ++i) {
    if (col[i * 2] == col[i * 2 + 1]) {
      return 0;
    }
    ans[i] = (col[i * 2 + 1] > col[i * 2]);
  }

  return 1;
}

void solve() {
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      for (int dir = 0; dir < 2; ++dir) {
        used[i][j][dir] = mp(-1, -1);
      }
    }
  }

  for (int i = 0; i < n; ++i) {
    eprintf("%s\n", s[i]);
  }

  vector<pair<int, int> > where;
  int cnt = 0;
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (s[i][j] == '-' || s[i][j] == '|') {
        where.pb(mp(i, j));
        for (int type = 0; type < 2; ++type) {
          bool &ok = isok[cnt][type];
          ok = 1;
          for (int dir0 = type; ok && dir0 < 4; dir0 += 2) {
            int x = i, y = j;
            int dir = dir0;
            while (1) {
              x += gox[dir], y += goy[dir];
              if (!inside(x, y) || s[x][y] == '#') {
                break;
              }
              if (s[x][y] == '-' || s[x][y] == '|') {
                ok = 0;
                break;
              }
              if (s[x][y] == '/') {
                dir ^= 3;
              } else {
                if (s[x][y] == '\\') {
                  dir ^= 1;
                } else {
                  assert(s[x][y] == '.');
                  used[x][y][dir & 1] = mp(cnt, type);
                }
              }
            }
          }
        }
        ++cnt;
      }
    }
  }
  assert(cnt < maxcnt);

  es = vector<vector<int> >(2 * cnt);
  for (int i = 0; i < cnt; ++i) {
    for (int j = 0; j < 2; ++j) {
      if (!isok[i][j]) {
        es[i * 2 + j].pb(i * 2 + !j);
      }
    }
  }
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      if (s[i][j] != '.') {
        continue;
      }
      auto &cur = used[i][j];
      if (cur[0].first == -1 && cur[1].first == -1) {
        printf("IMPOSSIBLE\n");
        return;
      }
      if (cur[0].first != -1 && cur[1].first != -1) {
        auto s = cur[0];
        auto t = cur[1];
        es[s.first * 2 + !s.second].pb(t.first * 2 + t.second);
        swap(s, t);
        es[s.first * 2 + !s.second].pb(t.first * 2 + t.second);
      } else {
        auto v = cur[0];
        if (cur[1].first != -1) {
          v = cur[1];
        }
        es[v.first * 2 + !v.second].pb(v.first * 2 + v.second);
      }
    }
  }

  if (!getans()) {
    printf("IMPOSSIBLE\n");
    return;
  }
  printf("POSSIBLE\n");
  for (int i = 0; i < cnt; ++i) {
    s[where[i].first][where[i].second] = "|-"[ans[i]];
  }

  for (int i = 0; i < n; ++i) {
    printf("%s\n", s[i]);
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
