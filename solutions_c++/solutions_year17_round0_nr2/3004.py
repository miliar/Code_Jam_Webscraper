#include <algorithm>
#include <stdio.h>
#include <vector>

int main() {
  int T;
  scanf ("%d", &T);

  for (int t = 1; t <= T; t++)
  {
    unsigned long long N;

    scanf ("%llu", &N);

    std::vector<unsigned long long> Q;
    unsigned long long D = N;

    while (D > 0)
    {
      Q.push_back (D % 10);

      D /= 10;
    }

    int rd = -1;

    int i = Q.size () - 1;

    while (i > 0)
    {
      int lowerdigit = (i - 1 <= rd ? 9 : Q[i - 1]);

      if (Q[i] > lowerdigit)
      {
        rd = std::max (rd, i - 1);

        Q[i]--;

        if (i + 1 < Q.size ())
        {
          i++;
        }
      }
      else
      {
        i--;
      }
    }

    D = 0;

    for (int i = Q.size () - 1; i >= 0; i--)
    {
      D *= 10;

      D += (i <= rd ? 9 : Q[i]);
    }

    printf ("Case #%d: %llu\n", t, D);
  }

  return 0;
}
