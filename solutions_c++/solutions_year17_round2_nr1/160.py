#include <stdio.h>
#include <float.h>
#include <algorithm>

int main() {
  int T;

  scanf("%d", &T);

  for (int t = 1; t <= T; t++) {
    int d, n;
    scanf("%d%d", &d, &n);

    double time = 0;
    for (int i = 0; i < n; i++) {
      int k, s;
      scanf("%d%d", &k, &s);

      if (k > d) continue;

      double thistime = ((double)(d - k)) / (double)s;
      time = std::max(time, thistime);
    }

    printf("Case #%d: ", t);
    printf("%lf", ((double)d) / time);
    printf("\n");
  }

  return 0;
}
