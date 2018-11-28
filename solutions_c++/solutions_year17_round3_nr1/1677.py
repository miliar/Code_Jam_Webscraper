#include <stdio.h>
#include <algorithm>
#include <string.h>
using namespace std;

int n, k, t;
double dp[1005][1005];
double pi = 3.14159265358979323846;

struct d{
	double r, h;
};
d dd[1005];

bool cmp(d a, d b)
{
	return a.r < b.r;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-out.txt", "w", stdout);
	while (~scanf("%d", &t))
	{
		int kase = 0;
		while (t--)
		{
			scanf("%d%d", &n, &k);
			for (int i = 0; i < n; i++)
			{
				scanf("%lf%lf", &dd[i].r, &dd[i].h);
			}
			sort(dd, dd + n, cmp);
			memset(dp, 0, sizeof(dp));
			//printf("%lf\n", dd[0].r);
			for (int i = 0; i < n; i++)
			{
				dp[0][i] = pi * dd[i].r * dd[i].r + 2 * pi * dd[i].r * dd[i].h;
			}
			for (int i = 1; i < k; i++)
			{
				for (int j = 0; j < n; j++)
				{
					dp[i][j] = dp[i - 1][j];
					for (int l = j + 1; l < n; l++)
					{
						dp[i][j] = max(dp[i][j], dp[i - 1][l] + 2 * pi * dd[j].r * dd[j].h);
					}
				}
			}
			double ans = 0;
			for (int i = 0; i < n; i++)
			{
				ans = max(ans, dp[k - 1][i]);
			}
			kase++;
			printf("Case #%d: %.9lf\n", kase, ans);
		}
	}
 } 
