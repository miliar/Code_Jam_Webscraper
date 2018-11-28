#include <cstdio>

int main(void) {
  int TT;
  scanf("%d", &TT);
  for (int T = 1; T <= TT; ++T) {
    double worst = 0;
    int D, K;
    scanf("%d %d", &D, &K);
    for (int i = 0; i < K; ++i) {
      int k, s;
      scanf("%d%d", &k, &s);
      double curr = (D - k) / (double)s;
      if (curr > worst) worst = curr;
    }
    printf("Case #%d: %.9lf\n", T, D / worst);
  }
  return 0;
}
