#include <bits/stdc++.h>
using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w+", stdout);
  int T, D, N;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%d%d", &D, &N);
    double m = 0;
    for (int i = 0, j, k; i < N; i++) {
      scanf("%d%d", &j, &k);
      m = max(m, 1.0*(D-j)/k);
    }
    printf("Case #%d: %f\n", t, D/m);
  }
  return 0;
}

