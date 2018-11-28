#include<bits/stdc++.h>
using namespace std;
#define sd(x) scanf("%d",&x)
#define slld(x) scanf("%lld",&x)
#define ss(x) scanf("%s",x)
#define ll long long
#define mod 1000007
#define bitcount    __builtin_popcountll
#define pb push_back
#define fi first
#define se second
#define mp make_pair
#define pi pair<int,int>
int a[1500],dp[1445][1445][3][3];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,i,j,k,l,m,x;
    sd(t);
    for(x=1;x<=t;x++)
    {
    	sd(n);
    	sd(m);
    	for(i=0;i<=1440;i++)
    		a[i]=0;
    	//memset(dp,mod,sizeof dp);
    	for(i=0;i<=1440;i++)
    	{
    		for(j=0;j<=1440;j++)
    		{
    			dp[i][j][1][1]=mod;
    			dp[i][j][1][2]=mod;
    			dp[i][j][2][1]=mod;
    			dp[i][j][2][2]=mod;
    		}
    	}
    	for(i=0;i<n;i++)
    	{
    		sd(j);
    		sd(k);
    		for(l=j+1;l<=k;l++)
    			a[l]=1;
    	}
    	for(i=0;i<m;i++)
    	{
    		sd(j);
    		sd(k);
    		for(l=j+1;l<=k;l++)
    			a[l]=2;
    	}
    	if(a[1]==1)
    	{
    		dp[1][1][1][1]=0;
    	}
    	else if(a[1]==2)
    	{
    		dp[1][0][2][2]=0;
    	}
    	else
    	{
    		dp[1][1][1][1]=0;
    		dp[1][0][2][2]=0;
    	}
    	for(i=2;i<=1440;i++)
    	{
    		if(a[i]!=1)
    		{
    			dp[i][0][2][2]=dp[i-1][0][2][2];
    		}
    		for(j=1;j<=min(i,720);j++)
    		{
    			if(i-j>720)
    				continue;
    			if(a[i]==1)
    			{
    				dp[i][j][1][1]=min(dp[i-1][j-1][1][2]+1,dp[i-1][j-1][1][1]);
    				dp[i][j][2][1]=min(dp[i-1][j-1][2][2]+1,dp[i-1][j-1][2][1]);
    			}
    			else if(a[i]==2)
    			{
    				if(i==j)
    					continue;
    				dp[i][j][1][2]=min(dp[i-1][j][1][1]+1,dp[i-1][j][1][2]);
    				dp[i][j][2][2]=min(dp[i-1][j][2][1]+1,dp[i-1][j][2][2]);
    			}
    			else
    			{
    				dp[i][j][1][1]=min(dp[i-1][j-1][1][2]+1,dp[i-1][j-1][1][1]);
    				dp[i][j][2][1]=min(dp[i-1][j-1][2][2]+1,dp[i-1][j-1][2][1]);
    				if(i==j)
    					continue;
    				dp[i][j][1][2]=min(dp[i-1][j][1][1]+1,dp[i-1][j][1][2]);
    				dp[i][j][2][2]=min(dp[i-1][j][2][1]+1,dp[i-1][j][2][2]);
    			}
    		}
    	}
    	//printf("%d\n",dp[1439][719][1][2]);
    	k=mod;
    	for(i=1;i<=2;i++)
    	{
    		for(j=1;j<=2;j++)
    			k=min(k,dp[1440][720][i][j]+abs(i-j));
    	}
    	printf("Case #%d: %d\n",x,k);
    }
    return 0;
}