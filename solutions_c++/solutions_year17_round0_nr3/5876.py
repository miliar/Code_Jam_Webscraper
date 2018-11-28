#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <map>

using namespace std;
const int MaxN = 1111;
int u[MaxN];
int main (void)
{
  int test, tests;
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    long long n, k;
    scanf ("%I64d %I64d", &n, &k);
    memset (u, 0, sizeof u);
    u[0] = u[n+1] = 1;

    long long mx, mn, mxl, cur;
    for (int i = 0; i < k; i++)
    {
      mxl = 0;
      cur = 0;
      for (int j = 1; j <= n; j++)
      {
        if (u[j] == 0)
          cur++;
        else
          cur = 0;
        if (mxl < cur)
          mxl = cur;
      }
      cur = 0;
      for (int j = 1; j <= n; j++)
      {
        if (u[j] == 0)
          cur++;
        else
          cur = 0;
        if (cur == mxl)
        {
          mx = mxl / 2;
          mn = (mxl - 1) / 2;
          u[j - mx] = 1;
          break;
        }  
      }

    }        
    printf ("Case #%d: %I64d %I64d\n", test + 1, mx, mn);

  }
  return 0;
}
