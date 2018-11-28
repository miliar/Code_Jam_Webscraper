#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<queue>
using namespace std;
const int N = 2050;
const int X = 720;
const int XX = 1440;
const int inf = ~0U>>2;
int n,m,p[N],dp[N][N][3];
int l,r;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-l.out","w",stdout);
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		memset(dp,0x3f,sizeof(dp));
		memset(p,0,sizeof(p));
		printf("Case #%d: ",tt);
		cin>>n>>m;
		for(int i=1;i<=n;i++)
		{
			scanf("%d %d",&l,&r);
			for(int j=l;j<r;j++) p[j]=1;
		}
		for(int i=1;i<=m;i++)
		{
			scanf("%d %d",&l,&r);
			for(int j=l;j<r;j++) p[j]=2;
		}
		if(p[0]) dp[0][0][p[0]]=0,dp[0][0][3-p[0]]=inf;
		else dp[0][0][1]=dp[0][0][2]=0;
		
		for(int i=1;i<=XX;i++)
		for(int j=max(0,i-X);j<=min(i,X);j++)
		for(int k=1;k<=2;k++)
		{
			if(p[i]&&p[i]!=k) dp[i][j][k]=inf;
			else if(j) 
			{
				if(k==1)
				dp[i][j][1]=min(dp[i-1][j][2]+1,dp[i-1][j-1][1]);
				else 
				dp[i][j][2]=min(dp[i-1][j-1][1]+1,dp[i-1][j][2]);
			}
			else
			{
				if(k==1)
				dp[i][j][1]=dp[i-1][j][2]+1;
				else 
				dp[i][j][2]=dp[i-1][j][2];
			}
		}
		
		if (min(dp[XX][X][1],dp[XX][X][2])&1) 
			cout<<min(dp[XX][X][1],dp[XX][X][2])+1<<endl;
		else 
			cout<<min(dp[XX][X][1],dp[XX][X][2])<<endl; 
	}
	return 0;
}
