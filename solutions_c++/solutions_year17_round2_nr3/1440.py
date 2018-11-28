#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%lld",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define mod 1000000007
#define bitcount __builtin_popcountll
#define ll long long
#define pb push_back
#define pi pair<ll,ll>
#define pii pair<pi,ll>
#define mp make_pair
ll i,j,k,n,q,ener[105],speed[105],dist[105];
double dp[105];
int main()
{
	ll t;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	sd(t);
	for(ll x=1;x<=t;x++)
	{
		sd(n);
		sd(q);
		for(i=1;i<=n;i++)
		{
			sd(ener[i]);
			sd(speed[i]);
		}
		for(i=1;i<=n;i++)
		{
			for(j=1;j<=n;j++)
			{
				sd(k);
				if(j==i+1)
				{
					dist[j]=k;
					dist[j]+=dist[j-1];
				}
			}
		}
		while(q--)
		{
			sd(i);
			sd(j);
		}
		for(i=1;i<=n;i++)
			dp[i]=1e18;
		dp[1]=0;
		for(i=2;i<=n;i++)
		{
			for(j=i-1;j>=1;j--)
			{
				if(ener[j]>=dist[i]-dist[j])
				{
					// prllf("%d %d\n",dist[i],dist[j-1]);
					// prllf("%lf %lf\n",dp[i], dp[j]+((double)(dist[i]-dist[j-1]))/speed[j]);
					dp[i]=min(dp[i],dp[j]+((double)(dist[i]-dist[j]))/speed[j]);
				}
			}
			// prllf("%lf\n",dp[i] );
		}
		printf("Case #%lld: %0.10lf\n",x,dp[n] );
	}
	return 0;
}