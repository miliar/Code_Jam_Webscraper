#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
double dp[1080];
int horse[1080];
ll pre[1080];
ll D[1080];
int L[1080][1080],S[1080];
int main()
{	
	int n,t,temp,i,j,q,st,end;
	scanf("%d",&t);
	temp=t;
	while(t--)
	{
		scanf("%d%d",&n,&q);
		pre[0]=0;
		pre[1]=0;
		for(i=0;i<=n;i++)
		{
			horse[i]=1;
			dp[i]=1e18;
		}
		for(i=1;i<=n;i++)
			scanf("%lld%d",&D[i],&S[i]);
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
				scanf("%d",&L[i][j]);
		for(i=1;i<n;i++)
		{
			pre[i+1]=(long long )L[i][i+1]+pre[i];
		}
		for(i=0;i<q;i++)
			scanf("%d%d",&st,&end);
		horse[1]=1;
		dp[1]=0;
		for(i=2;i<=n;i++)
		{
			for(j=1;j<i;j++)
			{	int k=j;
				ll dis=pre[i]-pre[k];
				if (D[k] >= dis)
				{
				double lol = dp[j]+(double)dis/(double)S[j];
				if (lol< dp[i]){
				horse[i]=j;
				dp[i]=lol;
				}
				}
			}
		}
		printf("Case #%d: %f\n",temp-t,dp[n]);
		}
	return 0;
}
		
				
				
