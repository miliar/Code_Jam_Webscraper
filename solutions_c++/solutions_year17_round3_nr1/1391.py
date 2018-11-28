#include <stdio.h>
#include <math.h>
#include <algorithm>
const double PI = acos(-1);
const int N = 1005;

double dp[N][N];

struct PanCake
{
   int r, h;
} pc[N];

bool cmp(const PanCake &x, const PanCake &y) { return x.r < y.r; }

int main()
{
   int T, cas;
   int n, k;
   int i, j;

   scanf("%d", &T);
   for (cas = 1; cas <= T; cas++)
   {
      scanf("%d %d", &n, &k);
      for (i = 0; i < n; i++)
         scanf("%d %d", &pc[i].r, &pc[i].h);
      std::sort(pc, pc+n, cmp);
      
      for (j = 0; j < n; j++)
         dp[1][j] = 2 * PI * pc[j].r * pc[j].h;
      for (i = 2; i <= k; i++)
      {
         double mx = dp[i-1][i-2];
         for (j = i - 1; j < n; j++)
         {
            dp[i][j] = mx + 2 * PI * pc[j].r * pc[j].h;
            mx = std::max(mx, dp[i-1][j]);
         }
      }
      double ans = 0;
      for (j = k - 1; j < n; j++)
         ans = std::max(ans, dp[k][j] + PI * pc[j].r * pc[j].r);
      printf("Case #%d: %lf\n", cas, ans);
   }

   return 0;
}
