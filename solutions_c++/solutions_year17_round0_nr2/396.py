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

char s[110], t[110];
LL inc(char *s) {
  int l = strlen(s);
  for (int i = 1; i < l; ++i)
    if (s[i] < s[i - 1])
      return 0;
  return stoll(s);
}
void solve() {
  scanf("%s", s);
  int l = strlen(s);
  if (l <= 1) {
    puts(s);
    return;
  }
  LL ans = 1;
  ans = max(ans, inc(s));
  REP(i, l - 1) t[i] = '9';
  t[l - 1] = 0;
  ans = max(ans, inc(t));
  REP(i, l) {
    if (s[i] > '1') {
      REP(j, l) t[j] = j <= i ? s[j] : '9';
      t[i]--;
      t[l] = 0;
      ans = max(ans, inc(t));
    }
  }
  printf("%lld\n", ans);
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

