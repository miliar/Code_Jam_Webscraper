#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 1111;

int a[MaxN][MaxN]; //[2][MaxN]
              
int main (void)
{
  int test, tests;
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, m, p, b, trains = 0, res = 0;
    scanf ("%*d %*d %d", &m); 
    trains = 0;
    memset (a, 0, sizeof(a));
    for (i = 0; i < m; i++)
    {
      scanf (" %d %d", &p, &b);
      a[b][0]++;
      a[b][p]++;
    }
    trains = max (max (a[1][0], a[2][0]), a[1][1] + a[2][1]);
    res = 0;
    for (i = 1; i <= 1000; i++)
      if (a[1][i] + a[2][i] > trains)
        res += a[1][i] + a[2][i] - trains;
    printf ("Case #%d: %d %d\n", test + 1, trains, res);
  }
  return 0;
}
