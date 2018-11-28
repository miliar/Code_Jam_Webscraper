#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <cassert>

int main() {
  int T, N, P, ans;
  int a[4];
  int tmp;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d%d", &N, &P);
    a[0] = a[1] = a[2] = a[3] = 0;
    for (int i = 0; i < N; ++i) {
      scanf("%d", &tmp);
      a[tmp % P] += 1;
    }
    ans = a[0];
    if (P == 2) {
      ans += (a[1] + 1) / 2;
    } else if (P == 3) {
      ans += std::min(a[1], a[2]);
      ans += (std::abs(a[1] - a[2]) + 2) / 3;
    } else if (P == 4) {
      ans += std::min(a[1], a[3]);
      ans += a[2] / 2;
      int t1 = std::abs(a[1] - a[3]);
      int t2 = a[2] % 2;
      if (t2 == 1 && t1 >= 2) {
        t2 -= 1;
        t1 -= 2;
        ans += 1;
      }
      ans += t1 / 4;
      t1 %= 4;
      assert(t1 + t2 * 2 < 4);
      if (t1 + t2 > 0) ans += 1;
    } else {
      assert(0);
    }
    printf("Case #%d: %d\n", t, ans);
  }
}
