#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define mp make_pair
#define sz(x) ((int) (x).size())
#define all(x) (x).begin(), (x).end()

#ifdef LOCAL
#define eprintf(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)
#else
#define eprintf(...)
#endif

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

const int maxn = 100;

char a[maxn][maxn], b[maxn][maxn];
vi g[2][2 * maxn], mt;
vector<char> used;

bool is_in(int x, int y, int n) {
  return x >= 0 && x < n && y >= 0 && y < n;
}

bool rc_check(int x, int y, int n) { // x
  bool res = 1;
  for (int j = 0; j < n; j++)
    if (j != y && (a[x][j] == 'x' || a[x][j] == 'o'))
      res = 0;
  for (int i = 0; i < n; i++)
    if (i != x && (a[i][y] == 'x' || a[i][y] == 'o'))
      res = 0;
  return res;
}

bool d_check(int x, int y, int n) { // +
  bool res = 1;
  for (int i = 0; i < n; i++) {
    int j = (x + y) - i;
    if (is_in(i, j, n) && (i != x || j != y) && (a[i][j] == '+' || a[i][j] == 'o'))
      res = 0;
  }
  for (int i = 0; i < n; i++) {
    int j = i - (x - y);
    if (is_in(i, j, n) && (i != x || j != y) && (a[i][j] == '+' || a[i][j] == 'o'))
      res = 0;
  }
  return res;
}

pii rc_xy (int x, int y, int n) {
  return mp(x, y);
}

pii d_xy(int d1, int d2, int n) {
  d2 -= (n - 1);
  return mp((d1 + d2) / 2, (d1 - d2) / 2);
}

bool kuhn(int v, int id) {
  if (used[v])
    return 0;
  used[v] = 1;
  for (int i = 0; i < sz(g[id][v]); i++) {
    int u = g[id][v][i];
    if (mt[u] == -1 || kuhn(mt[u], id)) {
      mt[u] = v;
      return 1;
    }
  }
  return 0;
}

int main() {
#ifdef LOCAL
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  int tt;
  cin >> tt;
  for (int qq = 1; qq <= tt; qq++) {
    printf("Case #%d: ", qq);
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        a[i][j] = '.';
    for (int i = 0; i < m; i++) {
      char c;
      int x, y;
      cin >> c >> x >> y;
      a[x - 1][y - 1] = c;
    }
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        b[i][j] = a[i][j];
    int k = 2 * n - 1;
    for (int i = 0; i < k; i++) {
      g[0][i].clear();
      g[1][i].clear();
    }
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++) {
        int r = i, c = j, d1 = i + j, d2 = i - j + n - 1;
        if ((a[i][j] == '.' || a[i][j] == '+') && rc_check(i, j, n))
          g[0][r].pb(c);
        if ((a[i][j] == '.' || a[i][j] == 'x') && d_check(i, j, n))
          g[1][d1].pb(d2);
      }
    mt.assign(k, -1);
    for (int i = 0; i < k; i++) {
      used.assign(k, 0);
      kuhn(i, 0);
    }
    for (int i = 0; i < k; i++)
      if (mt[i] != -1) {
        int c = i, r = mt[i];
        pii p = rc_xy(r, c, n);
        int x = p.first, y = p.second;
        if (a[x][y] == '+')
          b[x][y] = 'o';
        else
          b[x][y] = 'x';
      }
    mt.assign(k, -1);
    for (int i = 0; i < k; i++) {
      used.assign(k, 0);
      kuhn(i, 1);
    }
    for (int i = 0; i < k; i++)
      if (mt[i] != -1) {
        int d2 = i, d1 = mt[i];
        pii p = d_xy(d1, d2, n);
        int x = p.first, y = p.second;
        if (a[x][y] == 'x' || b[x][y] == 'x')
          b[x][y] = 'o';
        else
          b[x][y] = '+';
      }
    int val = 0, cnt = 0;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++) {
        if (b[i][j] == 'x' || b[i][j] == '+')
          val++;
        if (b[i][j] == 'o')
          val += 2;
        if (b[i][j] != a[i][j])
          cnt++;
      }
    cout << val << ' ' << cnt << endl;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        if (b[i][j] != a[i][j])
          cout << b[i][j] << ' ' << i + 1 << ' ' << j + 1 << endl;
  }
#ifdef LOCAL
  eprintf("Time %.2f\n", (double) clock() / CLOCKS_PER_SEC);
#endif
  return 0;
}