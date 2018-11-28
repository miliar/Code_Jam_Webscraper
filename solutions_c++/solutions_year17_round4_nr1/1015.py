#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <cassert>

using namespace std;

const int MaxN = 10;

int a[MaxN];
              
int main (void)
{
  int test, tests;
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, n, p, t, res = 0;
    scanf ("%d %d", &n, &p);
    memset (a, 0, sizeof a);
    for (i = 0; i < n; i++)
    {
      scanf ("%d", &t);
      a[t % p]++;
    }
    res = a[0];
    if (p == 2)
      res += (a[1] + 1) / 2;
    else if (p == 3)
    {
      int m = min(a[1], a[2]);
      res += m;
      a[1] -= m;
      a[2] -= m;
      res += a[1] / 3 + a[2] / 3;
      a[1] %= 3;
      a[2] %= 3;
      if (a[1] + a[2]  > 0)
        res++;
    }
    else if (p == 4)
    {
      res += a[2] / 2;
      a[2] %= 2;
      int m = min (a[1], a[3]);
      res += m;
      a[1] -= m;
      a[3] -= m;
      res += a[1] / 4 + a[3] / 4;
      a[1] %= 4;
      a[3] %= 4;
      if (a[1] + a[2] + a[3] > 0)
        res++;
    }
    else
      assert (false);
    printf ("Case #%d: %d\n", test + 1, res);
  }
  return 0;
}
