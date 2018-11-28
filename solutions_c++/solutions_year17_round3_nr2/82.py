#include<cstdio>
#include<cstring>
#include<iostream>
using namespace std;
const int N = 1500;
int dp[N][N][2][2];
int u[N];
int mi(int x,int y)
{
	if(x==-1)return y;
	if(y==-1)return x;
	return min(x,y);
}
int main()
{
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",ca++);
		int m,n;
		scanf("%d%d",&m,&n);
		memset(u,-1,sizeof(u));
		for(int i=0;i<m;i++)
		{
			int st,ed;
			scanf("%d%d",&st,&ed);
			st++;ed++;
			for(int j=st;j<ed;j++)u[j]=1;
		}
		for(int i=0;i<n;i++)
		{
			int st,ed;
			scanf("%d%d",&st,&ed);
			st++;ed++;
			for(int j=st;j<ed;j++)u[j]=0;
		}
		memset(dp,-1,sizeof(dp));
		dp[0][0][0][0]=dp[0][0][0][1]=0;
		for(int i=1;i<=24*60;i++)
		{
			for(int j=0;j<=720;j++)
			{
				for(int h=0;h<2;h++)
				{
					for(int k=0;k<2;k++)if(dp[i-1][j][h][k]!=-1)
					{
						int tmp=dp[i-1][j][h][k];
						int k1,h1;
						if(u[i]!=1&&j<720)
						{
							k1=0;
							int v=tmp;
							if(k1!=k)v++;
							if(i==1)h1=k1;
							else h1=h;
							if(i==24*60&&k1!=h1)v++;
							if(dp[i][j+1][h1][k1]==-1||dp[i][j+1][h1][k1]>v)dp[i][j+1][h1][k1]=v;
						}
						if(u[i]!=0&&i-j<=720)
						{
							k1=1;
							int v=tmp;
							if(k1!=k)v++;
							if(i==1)h1=k1;
							else h1=h;
							if(i==24*60&&k1!=h1)v++;
							if(dp[i][j][h1][k1]==-1||dp[i][j][h1][k1]>v)dp[i][j][h1][k1]=v;
						}
					}
				}
			}
		}
		int ret=mi(mi(dp[24*60][720][0][0],dp[24*60][720][0][1]), mi(dp[24*60][720][1][0],dp[24*60][720][1][1]));
		printf("%d\n",ret);
	}
}
		//printf("r1:%d r2:%d r3:%d r4:%d \n",dp[24*60][720][0][0],dp[24*60][720][0][1],
		////dp[24*60][720][1][0],dp[24*60][720][1][1]);
		//int ret=mi(mi(dp[24*60][720][0][0],dp[24*60][720][0][1]),
		//mi(dp[24*60][720][1][0],dp[24*60][720][1][1]));
		//printf("%d\n",ret);
		//}
		//return 0;
