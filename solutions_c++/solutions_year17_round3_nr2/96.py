#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
using namespace std;
#define pi acos(-1.0)
int t[1441];
int dp[730][730][2];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int T,k;
	int cas=0;
	scanf("%d",&T);
	while(T--)
	{
		int n,m;
		for(int i=0;i<=1440;i++)t[i]=3;
		scanf("%d%d",&n,&m);
		for(int i=1;i<=n;i++)
		{
			int a,b;
			scanf("%d%d",&a,&b);
			for(int j=a;j<b;j++)
			{
				if(t[j]&1)
				{
					t[j]^=1;
				}
			}
		}
		for(int i=1;i<=m;i++)
		{
			int a,b;
			scanf("%d%d",&a,&b);
			for(int j=a;j<b;j++)
			{
				if(t[j]&2)
				{
					t[j]^=2;
				}
			}
		}
		//memset(dp,-1,sizeof(dp));
		for(int i=0;i<=720;i++)
		for(int j=0;j<=720;j++)
		for(int l=0;l<2;l++)
		dp[i][j][l]=99999;
		dp[0][0][0]=0;
		for(int i=1;i<=1440;i++)
		{
			for(int j=0;j<i;j++)
			{
				if(j>720)continue;
				if(i-1-j>720)continue;
				if(t[i]&1)
				{
					dp[j+1][i-1-j][0]=min(dp[j+1][i-1-j][0],min(dp[j][i-1-j][0],dp[j][i-1-j][1]+1));
				}
				if(t[i]&2)
				{
					dp[j][i-j][1]=min(dp[j][i-j][1],min(dp[j][i-1-j][1],dp[j][i-1-j][0]+1));
				}
			}
		}
		long long ans1;
		if(dp[720][720][0]<=dp[720][720][1])ans1=dp[720][720][0];
		else ans1=dp[720][720][1]+1;
		
		for(int i=0;i<=720;i++)
		for(int j=0;j<=720;j++)
		for(int l=0;l<2;l++)
		dp[i][j][l]=99999;
		dp[0][0][1]=0;
		for(int i=1;i<=1440;i++)
		{
			for(int j=0;j<i;j++)
			{
				if(j>720)continue;
				if(i-1-j>720)continue;
				if(t[i]&1)
				{
					dp[j+1][i-1-j][0]=min(dp[j+1][i-1-j][0],min(dp[j][i-1-j][0],dp[j][i-1-j][1]+1));
				}
				if(t[i]&2)
				{
					dp[j][i-j][1]=min(dp[j][i-j][1],min(dp[j][i-1-j][1],dp[j][i-1-j][0]+1));
				}
			}
		}
		long long ans2;
		if(dp[720][720][0]>=dp[720][720][1])ans2=dp[720][720][1];
		else ans2=dp[720][720][0]+1;
		printf("Case #%d: %d\n",++cas,min(ans1,ans2));
	}
}