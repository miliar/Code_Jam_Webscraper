#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#define N 1444
using namespace std;
int n,m,a,b,p[N],dp[N][N][3],test;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("22.out","w",stdout);
	cin>>test;
	for (int kk=1;kk<=test;kk++)
	{
		memset(dp,0x3f,sizeof(dp));
		memset(p,0,sizeof(p));
		printf("Case #%d: ",kk);
		cin>>n>>m;
		for (int i=1;i<=n;i++)
		{
			scanf("%d%d",&a,&b);
			for (int j=a;j<b;j++) p[j]=1;
		}
		for (int i=1;i<=m;i++)
		{
			scanf("%d%d",&a,&b);
			for (int j=a;j<b;j++) p[j]=2;
		}
		if (p[0]) dp[0][0][p[0]]=0,dp[0][0][3-p[0]]=0x3f3f3f3f;
		else dp[0][0][1]=dp[0][0][2]=0;
		for (int i=1;i<=1440;i++)
		for (int j=max(0,i-720);j<=min(i,720);j++)
		for (int k=1;k<=2;k++)
		{
			if (p[i]&&p[i]!=k) dp[i][j][k]=0x3f3f3f3f;
			else if (j) 
			{
				if (k==1)
				dp[i][j][1]=min(dp[i-1][j][2]+1,dp[i-1][j-1][1]);
				else 
				dp[i][j][2]=min(dp[i-1][j-1][1]+1,dp[i-1][j][2]);
			}
			else
			{
				if (k==1)
				dp[i][j][1]=dp[i-1][j][2]+1;
				else 
				dp[i][j][2]=dp[i-1][j][2];
			}
		}
	//	cout<<p[540]<<endl;
	//	cout<<dp[539][359][1]<<' '<<dp[540][360][2]<<endl;
		if (min(dp[1440][720][1],dp[1440][720][2])&1) cout<<min(dp[1440][720][1],dp[1440][720][2])+1<<endl;
		else cout<<min(dp[1440][720][1],dp[1440][720][2])<<endl; 
	}
	return 0;
}
