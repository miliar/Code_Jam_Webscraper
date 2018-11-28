#include <cstdio>
#include <algorithm>
using namespace std;
int main() {
  int t;
  scanf("%d", &t);
  for (int ti = 0; ti < t; ++ti) {
    int n, p;
    scanf("%d%d", &n, &p);
    int g[4] = {};
    for (int i = 0; i < n; ++i) {
      int x;
      scanf("%d", &x);
      ++g[x % p];
    }
    int ans = g[0];
    if (p == 2) {
      ans += (g[1] + 1) / 2;
    } else if (p == 3) {
      int x = min(g[1], g[2]), y = max(g[1], g[2]);
      ans += x;
      ans += ((y - x) + 2) / 3;
    } else {
      ans += g[2] / 2;
      if (g[2] % 2) {
        int x = min(g[1], g[3]), y = max(g[1], g[3]);
        ans += x;
        ans += (y - x + 5) / 4;
      } else {
        int x = min(g[1], g[3]), y = max(g[1], g[3]);
        ans += x;
        ans += (y - x + 3) / 4;
      }
    }
    printf("Case #%d: %d\n", ti + 1, ans);
  }
  return 0;
}
