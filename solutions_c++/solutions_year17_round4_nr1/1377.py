#include <bits/stdc++.h>

using namespace std;

const int N = 110;

int n, p;
int g[N], cnt[10];

int main() {
  int t;
  scanf("%d", &t);
  for (int _ = 1; _ <= t; ++_) {
    scanf("%d%d", &n, &p);
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < n; ++i) {
      scanf("%d", g + i);
      cnt[g[i] % p]++;
    }
    int ans = 0;
    if (p == 2) {
      ans += (cnt[1] + 1) / 2;
      ans += cnt[0];
    } else if (p == 3) {
      ans += cnt[0];
      ans += min(cnt[1], cnt[2]);
      if (cnt[2] < cnt[1])
        ans += (cnt[1] - cnt[2] + 2) / 3;
      else
        ans += (cnt[2] - cnt[1] + 2) / 3;
    } else if (p == 4) {
      ans += cnt[0];
      int mx = 0;
      for (int x1 = 0; x1 <= cnt[1]; ++x1) {
        for (int x3 = 0; x1 + 2 * x3 <= cnt[1]; ++x3) {
          for (int x4 = 0; x4 + x3 <= cnt[2]; ++x4) {
            int x6 = 0;
            if (cnt[2] - x3 - x4 < 0) continue;
            int x2 = (cnt[2] - x3 - x4) / 2;
            if (cnt[1] - x1 - 2 * x3 - 2 * x6 < 0) continue;
            int x5 = (cnt[1] - x1 - 2 * x3 - 2 * x6) / 4;
            if (cnt[3] - x1 - 2 * x4 - 2 * x6 < 0) continue;
            int x7 = (cnt[3] - x1 - 2 * x4 - 2 * x6) / 4;
            int tmp = x1 + x2 + x3 + x4 + x5 + x6 + x7;
            if (cnt[1] > x1 + 2 * x3 + 4 * x5 + 2 * x6 ||
                cnt[2] > 2 * x2 + x3 + x4 ||
                cnt[3] > x1 + 2 * x4 + 2 * x6 + 4 * x7)
              tmp++;
            mx = max(tmp, mx);
          }
        }
      }
      ans += mx;
    }
    printf("Case #%d: %d\n", _, ans);
  }
  return 0;
}
