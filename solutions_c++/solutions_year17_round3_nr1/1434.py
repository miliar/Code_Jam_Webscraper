#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
const int maxn = 1e3+5;
const double pi = acos(-1.0);

double dp[maxn][maxn];

int n,k;

struct node
{
	int r,h;
}a[maxn];

int cmp(node n1,node n2)
{
	return n1.r > n2.r;
}

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Abig.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int kase = 1;kase <= T;kase++)
	{
		scanf("%d %d",&n,&k);
		memset(dp,0,sizeof(dp));
		for(int i = 1;i <= n;i++) scanf("%d %d",&a[i].r,&a[i].h);

		printf("Case #%d: ",kase);

		sort(a+1,a+n+1,cmp);

		double last = 0.0;
		for(int i = 1;i <= n;i++)
		{
			for(int j = 1;j <= min(i,k);j++)
			{
				
				double tmp;
			//	printf("i = %d tmp = %f\n",i,tmp);

				if(j == 1)
				{
					tmp = 2 * pi * a[i].r * a[i].h + pi * a[i].r * a[i].r;
				}
				else
				{
					tmp = 2 * pi * a[i].r * a[i].h;
				}

				dp[i][j] = max(dp[i][j],dp[i-1][j-1] + tmp);
				dp[i][j] = max(dp[i][j],dp[i-1][j]);
			}
		}

		/*for(int i = 1;i <= n;i++)
		{
			for(int j = 1;j <= k;j++)
			{
				printf("dp[%d][%d] = %f\n",i,j,dp[i][j]);
			}
		}*/

		printf("%.9f\n",dp[n][k]);


	}
	return 0;
}