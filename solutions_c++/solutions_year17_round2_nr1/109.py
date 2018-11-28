#include <stdio.h>
#include <algorithm>

int main () {
  int T, D, N;
  double k, s, time;
  scanf("%d", &T);
  for (int t = 1; t <= T; ++t) {
    scanf("%d%d", &D, &N);
    time = 0.0;
    for (int i = 0; i < N; ++i) {
      scanf("%lf%lf", &k, &s);
      time = std::max(time, (D - k) / s);
    }
    printf("Case #%d: %lf\n", t, D / time);
  }
  return 0;
}
