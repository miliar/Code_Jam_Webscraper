#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif

#include <bits/stdc++.h>

using namespace std;

typedef long double ld;

#ifdef DEBUG
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#else
#define eprintf(...) ;
#endif

#define sz(x) ((int) (x).size())
#define TASK "text"

const int inf = (int) 1.01e9;
const ld eps = 1e-9;
const ld pi = acos((ld) -1);

mt19937 mrand(random_device{} ()); 

int rnd(int x) {
  return mrand() % x;
}

void precalc() {
}

const int maxn = 205;
int n, m;
int del[2][2][maxn];
int a[2][maxn][maxn];
int a0[2][maxn][maxn];

int read() {
  if (scanf("%d%d", &n, &m) < 2) {
    return false;
  }
  for (int it = 0; it < 2; it++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        a[it][i][j] = false;
      }
    }
    for (int i = 0; i < 2 * n; i++) {
      del[it][0][i] = false;
      del[it][1][i] = false;
    }
  }
  for (int i = 0; i < m; i++) {
    char tmp[5];
    int r, c;
    scanf("%s%d%d", tmp, &r, &c);
    r--;
    c--;
    char ch = tmp[0];
    if (ch == 'x' || ch == 'o') {
      a[0][r][c] = true;
      del[0][0][r] = true;
      del[0][1][c] = true;
    }
    if (ch == '+' || ch == 'o') {
      a[1][r][c] = true;
      del[1][0][r + c] = true;
      del[1][1][r + n - 1 - c] = true;
    }
  }
  return true;
}

int p[maxn];
int g[maxn][maxn];
int vs;
int used[maxn];
int curu;

bool dfs(int v) {
  used[v] = curu;
  for (int u = 0; u < vs; u++) {
    if (g[v][u] && p[u] == -1) {
      p[u] = v;
      return true;
    }
  }
  for (int u = 0; u < vs; u++) {
    if (g[v][u] && used[p[u]] != curu && dfs(p[u])) {
      p[u] = v;
      return true;
    }
  }
  return false;
}

void solve() {
  for (int it = 0; it < 2; it++) {
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        a0[it][i][j] = a[it][i][j];
      }
    }
  }
  for (int it = 0; it < 2; it++) {
    vs = (!it ? n : 2 * n - 1);
    for (int i = 0; i < vs; i++) {
      for (int j = 0; j < vs; j++) {
        g[i][j] = false;
      }
    }
    if (!it) {
      for (int i = 0; i < vs; i++) {
        if (del[it][0][i]) {
          continue;
        }
        for (int j = 0; j < vs; j++) {
          if (del[it][1][j]) {
            continue;
          }
          g[i][j] = true;
        }
      }
    } else {
      for (int i = 0; i < vs; i++) {
        if (del[it][0][i]) {
          continue;
        }
        for (int j = 0; j < vs; j++) {
          if (del[it][1][j]) {
            continue;
          }
          int r = i + j - n + 1;
          if (r & 1) {
            continue;
          }
          r /= 2;
          int c = i - j + n - 1;
          if (c & 1) {
            continue;
          }
          c /= 2;
          if (0 <= r && r < n && 0 <= c && c < n) {
            g[i][j] = true;
          }
        }
      }
    }
    for (int i = 0; i < vs; i++) {
      p[i] = -1;
    }
    for (int i = 0; i < vs; i++) {
      if (!del[it][0][i]) {
        curu++;
        dfs(i);
      }
    }
    for (int i = 0; i < vs; i++) {
      if (p[i] == -1) {
        continue;
      }
      int r, c;
      if (!it) {
        r = p[i];
        c = i;
      } else {
        r = p[i] + i - n + 1;
        assert(!(r & 1));
        r /= 2;
        c = p[i] - i + n - 1;
        assert(!(c & 1));
        c /= 2;
      }
      assert(0 <= r && r < n && 0 <= c && c < n);
      a[it][r][c] = true;
    }
  }
  int res = 0;
  vector< pair<char, pair<int, int> > > ans;
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      int msk = 0;
      bool need = false;
      for (int it = 0; it < 2; it++) {
        res += a[it][i][j];
        if (a[it][i][j]) {
          msk |= (1 << it);
        }
        if (a[it][i][j] != a0[it][i][j]) {
          need = true;
        }
      }
      if (need) {
        ans.push_back(make_pair(" x+o"[msk], make_pair(i, j)));
      }
    }
  }
  printf("%d %d\n", res, sz(ans));
  for (int i = 0; i < sz(ans); i++) {
    printf("%c %d %d\n", ans[i].first, ans[i].second.first + 1, ans[i].second.second + 1);
  }
}

int main() {
  precalc();
#ifdef DEBUG
  assert(freopen(TASK ".in", "r", stdin));
  assert(freopen(TASK ".out", "w", stdout));
#endif
  int t;
  scanf("%d", &t);
  t = 0;
  while (read()) {
    t++;
    printf("Case #%d: ", t);
    solve();
#ifdef DEBUG
    eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  }
  return 0;
}
