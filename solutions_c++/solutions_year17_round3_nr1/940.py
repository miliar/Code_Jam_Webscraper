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

    std::vector< std::pair <long long, long long> > RH (N);
    std::vector< std::pair <long long, int> > RHR (N);

    for (int i = 0; i < N; i++)
    {
      scanf ("%lld %lld", &RH[i].first, &RH[i].second);

      RHR[i].first = RH[i].first * RH[i].second;
      RHR[i].second = i;
    }

    std::sort (RHR.rbegin (), RHR.rend ());

    long long m = 0;
    
    for (int i = 0; i < N; i++)
    {
      long long l = RH[i].first * RH[i].first + 2 * RH[i].first * RH[i].second;

      int amount = 1;

      for (int j = 0; j < N; j++)
      {
        if (RHR[j].second == i)
          continue;

        if (amount == K)
          break;

        if (RH[RHR[j].second].first <= RH[i].first)
        {
          l += 2 * RHR[j].first;

          amount++;
        }
      }      

      if (amount == K)
      {
        m = std::max (m, l);
      }
    }

    printf ("Case #%d: %0.9lf\n", t, m * M_PI);
  }

  return 0;
}
