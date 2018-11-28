#include <bits/stdc++.h>

#define FOR(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

#define x first
#define y second

using namespace std;

typedef long long ll;

const int MAXN = 1010;

int n, d;
int k[MAXN], s[MAXN];

void solve() {
  scanf("%d%d", &d, &n);
  REP(i, n) scanf("%d%d", &k[i], &s[i]);
  double tm = 0;
  REP(i, n) tm = max(tm, (double)(d - k[i]) / s[i]);
  printf("%.8lf\n", d / tm);
}

int main(void) {
  int tests;
  scanf("%d", &tests);
  for (int test = 1; test <= tests; ++test) {
    printf("Case #%d: ", test);
    solve();
  }
  return 0;
}

