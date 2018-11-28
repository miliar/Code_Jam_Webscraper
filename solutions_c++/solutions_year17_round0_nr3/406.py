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

LL f(LL a, LL x, LL b, LL y, LL k) {
  if (x + y >= k)
    return k <= y ? b : a;
  k -= x + y;
  map<LL, LL> m;
  a--;
  m[a / 2] += x;
  m[a - a / 2] += x;
  b--;
  m[b / 2] += y;
  m[b - b / 2] += y;

  assert(m.size() <= 2);
  vector<pair<LL, LL>> v(m.begin(), m.end());
  if (v.size() == 1)
    v.EB(v[0].F + 1, 0);
  return f(v[0].F, v[0].S, v[1].F, v[1].S, k);
}

void solve() {
  LL n, k;
  scanf("%lld%lld", &n, &k);
  LL t = f(n, 1, n + 1, 0, k);
  t--;
  LL a = t / 2, b = t - t / 2;
  printf("%lld %lld\n", max(a, b), min(a, b));
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

