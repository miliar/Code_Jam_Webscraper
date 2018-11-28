#include <bits/stdc++.h>

using namespace std;

typedef long long LL;
const int maxint = 0x7f7f7f7f, mod = 1000000007;
const double eps = 1e-8, pi = acos(-1.0);
#define mset(a, v) memset(a, v, sizeof(a));
#define mset0(a) mset(a, 0);

void rd() { }
template<typename... T> void rd(int &h, T &... t) { scanf("%d", &h); rd(t...); }
template<typename... T> void rd(long long &h, T &... t) { scanf("%lld", &h); rd(t...); }
template<typename... T> void rd(double &h, T &... t) { scanf("%lf", &h); rd(t...); }

LL n;
int ds[111];

LL solve(LL n) {
  if (n == 0) return 0;
  int k = 0;
  LL m = n;
  while (n) {
    ds[++k] = n % 10;
    n /= 10;
  }
  n = m;
  LL nines = 0;
  for (int i = 1; i < k; ++i) {
    nines = nines * 10 + 9;
    n /= 10;
    if (ds[i] < ds[i+1]) {
      return solve(n-1) * (nines + 1) + nines;
    }
  }
  return m;
}

int main() {
  freopen("B-small-attempt0.out", "w", stdout);
  int tests;
  rd(tests);
  for (int tt = 1; tt <= tests; ++tt) {
    rd(n); 
    printf("Case #%d: %lld\n", tt, solve(n));
  }
  return 0;
}
