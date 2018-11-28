#include <bits/stdc++.h>

int main ()
{
  int t, i, d, n, j, k, s;
  scanf ("%d\n", &t);
  for (i = 1; i <= t; i++) {
    scanf ("%d%d", &d, &n);
    double worst = 0;
    for (j = 0; j < n; j++) {
      scanf ("%d%d", &k, &s);
      if ((d - k) / (double) s > worst) worst = (d - k) / (double) s;
    }
    printf ("Case #%d: %.9lf\n", i, d / worst);
  }
  return 0;
}
