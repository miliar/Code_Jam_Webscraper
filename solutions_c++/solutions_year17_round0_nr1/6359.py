#include <bits/stdc++.h>

#define FOR(i, a, b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

#define x first
#define y second

using namespace std;

typedef long long ll;

const int MAXN = 1100;

void solve() {
  static char s[MAXN];
  int n, k;
  scanf("%s %d", s, &k);
  n = strlen(s);
  int ans = 0;
  REP(i, n-k+1) {
    if (s[i] == '+') continue;
    ++ans;
    FOR(j, i, i+k) {
      if (s[j] == '+') s[j] = '-';
      else s[j] = '+';
    }
  }
  REP(i, n) {
    if (s[i] == '+') continue;
    printf("IMPOSSIBLE\n");
    return;
  }
  printf("%d\n", ans);
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

