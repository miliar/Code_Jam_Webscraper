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

int n, m;
char g[33][33];

void solve() {
  scanf("%d%d", &n, &m);
  REP(i, n) scanf("%s", g[i]);
  REPE(i, 1, n - 1) REP(j, m)
    if (g[i][j] == '?') g[i][j] = g[i - 1][j];
  for (int i = n - 2; i >= 0; --i) REP(j, m)
    if (g[i][j] == '?') g[i][j] = g[i + 1][j];
  REP(i, n) REPE(j, 1, m - 1)
    if (g[i][j] == '?') g[i][j] = g[i][j - 1];
  REP(i, n) for (int j = m - 2; j >= 0; --j)
    if (g[i][j] == '?') g[i][j] = g[i][j + 1];
  puts("");
  REP(i, n) puts(g[i]);
}

int main() {
  int T;
  scanf("%d", &T);
  for (int kase = 1; kase <= T; ++kase) {
    printf("Case #%d: ", kase);
    solve();
  }
  return 0;
}

