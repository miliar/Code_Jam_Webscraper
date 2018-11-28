#include <cassert>

#include <stdio.h>

int main() {
  int T;
  scanf ("%d", &T);

  for (int t = 1; t <= T; t++)
  {
    int D, N;

    scanf ("%d %d", &D, &N);

    double speed = 1.e+30;

    for (int i = 0; i < N; i++)
    {
      int K, S;

      scanf ("%d %d", &K, &S);

      double s = D;
      s *= S;
      s /= D - K;

      if (s < speed)
      {
        speed = s;
      }
    }

    printf ("Case #%d: %lf\n", t, speed);
  }

  return 0;
}
