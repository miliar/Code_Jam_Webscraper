#include <cstdio>
#include <algorithm>

double P[64];

int main(void) {
  int TT;
  scanf("%d", &TT);
  for (int T = 1; T <= TT; ++T) {
    int N, K;
    double U;
    scanf("%d%d", &N, &K);
    scanf("%lf", &U);
    for (int i = 0; i < N; ++i)
      scanf("%lf", P + i);
    std::sort(P, P + N);

    double best = 1;
    for (int i = 0; i < N; ++i)
      best *= P[i];
    for (int i = 0; i < N; ++i) {
      double left = U;
      for (int j = 0; j < i; ++j)
        left -= P[i] - P[j];
      if (left < 0) break;
      double val = std::min(1., P[i] + left / (i + 1));
      // printf("i=%d P[i]=%lf left=%lf val=%lf\n", i, P[i], left, val);
      double cur = 1;
      for (int j = 0; j < N; ++j)
        cur *= j <= i ? val : P[j];
      if (cur > best) best = cur;
    }
    printf("Case #%d: %.9lf\n", T, best);
  }
  return 0;
}
