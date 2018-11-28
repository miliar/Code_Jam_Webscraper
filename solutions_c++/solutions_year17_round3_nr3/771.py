#include <cassert>

#include <cmath>
#include <cstdio>
#include <vector>
#include <algorithm>

int main() {
  int T;
  scanf ("%d", &T);

  for (int t = 1; t <= T; t++)
  {
    int N, K;

    scanf ("%d %d", &N, &K);

    double U;

    scanf ("%lf", &U);

    std::vector<double> P (N);

    for (int i = 0; i < N; i++)
    {
      scanf ("%lf", &P[i]);
    }

    std::sort (P.begin (), P.end ());

    P.push_back (1.0);
    N++;
    K++;

    double ans = 1.0;

    for (int i = 1; i < N; i++)
    {
      double D = P[i] - P[i - 1];

      double A = std::min (D * i, U);

      if (A >= 0)
      {
        U -= A;

        A /= i;

        for (int j = 0; j < i; j++)
        {
          P[j] += A;
        }
      }
    }

    for (int i = 0; i < N; i++)
    {
      ans *= P[i];
    }

    printf ("Case #%d: %lf\n", t, ans);
  }

  return 0;
}
