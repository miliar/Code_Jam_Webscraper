#include<cstdio>
#include<algorithm>
using namespace std;
struct horse
{
	double d,v;
}h[105];
double e[105];
double dp[105];
int main()
{
	int T,d1,d2,q,n;
	double c;
	scanf("%d",&T);
	for(int I=1,d1=0,d2=0;I<=T;I++)
	{
		scanf("%d%d",&n,&q);
		for(int i=1;i<=n;i++)
		{
			scanf("%lf%lf",&h[i].d,&h[i].v);
			dp[i]=1e20;
			e[i]=0.0;
		}

		dp[1]=0.0;
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
			{
				scanf("%lf",&c);
				if(i+1==j)
				{
					e[j]=c;
					e[i+1]+=e[i];
					//printf("-= %lf =-\n",c);
				}
			}
		scanf("%d%d",&d1,&d2);
		
		
		for(int i=2;i<=n;i++)
			for(int j=1;j<i;j++)
				if(h[j].d>=e[i]-e[j])
					dp[i]=min(dp[i],(e[i]-e[j])/h[j].v+dp[j]);

		printf("Case #%d: %.9lf\n",I,dp[n]);
	}
}