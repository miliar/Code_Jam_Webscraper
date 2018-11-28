#include <stdio.h>
#include <algorithm>

int main() {
  freopen("A.in", "r", stdin);
  freopen("A.out", "w", stdout);
  int T;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    int d, n;
    scanf("%d%d", &d, &n);
    double time = 0;
    for(int i = 0; i < n; i++) {
      int k, s;
      scanf("%d%d", &k, &s);
      time = std::max(time, (double)(d - k) / s);
    }
    double speed = d / time;

    printf("Case #%d: %lf\n", t, speed);
  }
  return 0;
}
