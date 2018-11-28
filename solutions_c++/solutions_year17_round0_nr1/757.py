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

const int maxN = 1111;
int n, K;
char S[maxN];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  int tests;
  scanf("%d\n", &tests);
  for (int tt = 1; tt <= tests; ++tt) {
    scanf("%s %d", S+1, &K);
    n = strlen(S+1);
    int cnt = 0;
    for (int i = 1; i <= n-K+1; ++i) {
      if (S[i] == '-') {
        for (int j = i; j < i+K; ++j) {
          S[j] = (S[j] == '-' ? '+' : '-');
        }
        ++cnt;
      }
    }
    for (int i = 1; i <= n; ++i) {
      if (S[i] == '-') cnt = -1;
    }
    printf("Case #%d: ", tt);
    if (cnt != -1) {
      printf("%d\n", cnt);
    } else puts("IMPOSSIBLE");
  }
  return 0;
}
