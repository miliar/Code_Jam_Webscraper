#include <cstdio>
#include <cstring>
#include <algorithm>

const int N = 1000 + 10;

int n, c, m;

int x[N], y[N], sum[N];

int main() {
  int tcase;
  scanf("%d", &tcase);
  for (int tid = 1; tid <= tcase; ++tid) {
    scanf("%d%d%d", &n, &c, &m);
    memset(x, 0, sizeof x);
    memset(y, 0, sizeof y);
    while (m--) {
      int p, b;
      scanf("%d%d", &p, &b);
      ++x[b], ++y[p];
    }
    int ans = *std::max_element(x + 1, x + c + 1);
    for (int i = 1, sum = 0; i <= n; ++i) ans = std::max(ans, ((sum += y[i]) + i - 1) / i);
    int val = 0;
    for (int i = 1, sum = 0; i <= n; ++i) {
      if (y[i] > ans) {
        int t = y[i] - ans;
        sum -= t;
        val += t;
      } else {
        sum += ans - y[i];
      }
    }
    printf("Case #%d: %d %d\n", tid, ans, val);
  }
  return 0;
}
