#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < int(n); ++i)
#define REPE(i, a, b) for (int i = (a); i <= int(b); ++i)
#define SZ(x) ((int)(x).size())
#define ALL(x) x.begin(), x.end()
#define PB push_back
#define EB emplace_back
using LL = long long;
using PII = pair<int, int>;
#define F first
#define S second

int type[128] = {};
int a[110][110], b[110][110];
bool vis[110], d1[220], d2[220];
void solve() {
  memset(a, 0, sizeof a);
  memset(b, 0, sizeof b);
  memset(vis, 0, sizeof vis);
  memset(d1, 0, sizeof d1);
  memset(d2, 0, sizeof d2);
  int n, m;
  scanf("%d%d", &n, &m);
  REP(i, m) {
    static char s[4];
    static int x, y;
    scanf("%s%d%d", s, &x, &y);
    x--, y--;
    a[x][y] = b[x][y] = type[s[0]];
    if (a[x][y] & 2) vis[y] = true;
  }
  REP(i, n) a[0][i] |= 1;
  REPE(i, 1, n - 2) a[n - 1][i] |= 1;
  REP(i, n) {
    bool f = true;
    REP(j, n) if (a[i][j] & 2) {
      f = false;
      break;
    }
    if (!f) continue;
    int chz = 0;
    REP(j, n) if (!vis[j]) {
      chz = j;
    }
    vis[chz] = true;
    a[i][chz] |= 2;
  }
  vector<tuple<char, int, int>> ans;
  int sum = 0;
  REP(i, n) REP(j ,n) {
    char c = '.';
    if (a[i][j] == 1) c = '+';
    else if (a[i][j] == 2) c = 'x';
    else if (a[i][j] == 3) c = 'o';
    // printf("%c", c); if (j == n - 1) puts("");
    if (a[i][j] & 1) sum++;
    if (a[i][j] & 2) sum++;
    if (a[i][j] != b[i][j]) {
      ans.EB(c, i, j);
    }
  }
  printf("%d %d\n", sum, SZ(ans));
  for (const auto &it : ans) {
    char c; int x, y;
    tie(c, x, y) = it;
    printf("%c %d %d\n", c, x + 1, y + 1);
  }
}

int main() {
  type['+'] = 1;
  type['x'] = 2;
  type['o'] = 3;
  int T;
  scanf("%d", &T);
  for (int kase = 1; kase <= T; ++kase) {
    printf("Case #%d: ", kase);
    solve();
  }
  return 0;
}

