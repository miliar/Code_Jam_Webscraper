#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 111, MaxC = 0x3f3f3f3f;

int g[MaxN][MaxN];
double gt[MaxN][MaxN];

int d[MaxN], s[MaxN];
              
int main (void)
{
  int test, tests;
  scanf ("%d", &tests);
  for (test = 0; test < tests; test++)
  {
    int i, j, k, n, q;
    scanf ("%d %d", &n, &q);
    for (i = 0; i < n; i++)
      scanf ("%d %d", &d[i], &s[i]);
    for (i = 0; i < n; i++)
      for (j = 0; j < n; j++)
      {
        scanf ("%d", &g[i][j]);
        if (g[i][j] == -1)
           g[i][j] = MaxC;
      }
    for (k = 0; k < n; k++)
      for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
          if (g[i][j] > g[i][k] + g[k][j])
            g[i][j] = g[i][k] + g[k][j];
    for (i = 0; i < n; i++)
      for (j = 0; j < n; j++)
      {
        gt[i][j] = 1e30;
        if (g[i][j] <= d[i])
          gt[i][j] = g[i][j] * 1.0 / s[i];
      }
    for (k = 0; k < n; k++)
      for (i = 0; i < n; i++)
        for (j = 0; j < n; j++)
          if (gt[i][j] > gt[i][k] + gt[k][j])
            gt[i][j] = gt[i][k] + gt[k][j];
    int u, v;
    printf ("Case #%d:", test + 1);
    for (i = 0; i < q; i++)
    {
      scanf("%d %d", &u, &v);
      printf (" %lf", gt[u-1][v-1]);
    }
    printf ("\n");
  }
  return 0;
}
