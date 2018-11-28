#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <cstdlib>

using namespace std;

int cnt[4];

int main() {
  freopen("/Users/yogy/ClionProjects/untitled/A-small-attempt0.in", "r", stdin);
  freopen("/Users/yogy/ClionProjects/untitled/A-small.out", "w", stdout);
  int T, tc = 0;
  scanf("%d", &T);
  while (T--) {
    int ans = 0;
    int n, p, m, t;
    scanf("%d%d", &n, &p);
    memset(cnt, 0, sizeof(cnt));
    m = n;
    for (int i = 0; i < n; ++i) {
      int x;
      scanf("%d", &x);
      cnt[x % p]++;
    }
    ans += cnt[0];
    m -= cnt[0];

    if (p == 2) {
      t = cnt[1] / 2;
      ans += t;
      m -= t * 2;
    } else if (p == 3) {
      t = min(cnt[1], cnt[2]);
      ans += t;
      m -= t * 2;
      cnt[1] -= t;
      cnt[2] -= t;

      for (int i = 1; i <= 2; ++i) {
        if (cnt[i]) {
          t = cnt[i] / 3;
          ans += t;
          m -= t * 3;
        }
      }
    } else if (p == 4) {
      t = min(cnt[1], cnt[3]);
      ans += t;
      m -= t * 2;
      cnt[1] -= t;
      cnt[3] -= t;

      t = cnt[2] / 2;
      ans += t;
      m -= t * 2;
      cnt[2] -= t * 2;

      for (int i = 1; i <= 3; i += 2) {
        if (cnt[i]) {
          t = min(cnt[2], cnt[i] / 2);
          ans += t;
          cnt[i] -= t * 2;
          cnt[2] -= t;

          if (cnt[i]) {
            t = cnt[i] / 4;
            ans += t;
            m -= t * 4;
          }
        }
      }
    }
    if (m) ++ans;

    printf("Case #%d: %d\n", ++tc, ans);
  }
  return 0;
}