#include <bits/stdc++.h>
using namespace std;

int T, N, K;
double U, P[100];

int main() {
  freopen("C-small-1-attempt0.in", "r", stdin);
  freopen("C-small-1-attempt0.out", "w+", stdout);
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d%d", &N, &K);
    scanf("%lf", &U);
    for (int i = 0; i < N; i++) {
      scanf("%lf", &P[i]);
    }
    double lb = 0.0, ub = 1.0, m, f;
    while (ub-lb>1e-9) {
      m = (lb+ub) / 2;
      f = 0;
      for (int i = 0; i < N; i++) {
        f += max(m-P[i], 0.0);
      }
      if (f < U) {
        lb = m;
      } else {
        ub = m;
      }
    }
    f = 1;
    for (int i = 0; i < N; i++) {
      f *= max(P[i], m);
    }
    printf("Case #%d: %.9f\n", t, f);
  }
  return 0;
}

