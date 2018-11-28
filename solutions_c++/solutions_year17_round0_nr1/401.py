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

char s[10010];
int k, n;

void solve() {
  scanf("%s%d", s, &k);
  n = strlen(s);
  int times = 0;
  for (int i = 0; i + k <= n; ++i) {
    if (s[i] == '-') {
      times++;
      for (int j = i; j < i + k; ++j)
        s[j] = s[j] == '+' ? '-' : '+';
    }
  }
  bool ans = true;
  for (int i = 0; i < n; ++i)
    if (s[i] == '-') {
      ans = false;
      break;
    }
  if (ans) printf("%d\n", times);
  else puts("IMPOSSIBLE");
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

