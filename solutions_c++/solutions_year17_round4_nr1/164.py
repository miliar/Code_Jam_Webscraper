#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<string>
#include<set>
#include<sstream>
using namespace std;
typedef long long lld;
#define mp make_pair
#define X first
#define Y second
#define pb push_back
#define mp make_pair
#define eps 1e-8
#define pi acos(-1.0)
int dp[110][110][110][4];
int s[110];
int dfs(int x,int y,int z,int k)
{
	if(dp[x][y][z][k] != -1)
		return dp[x][y][z][k];
	if(x+y+z == 0)
	{
		dp[x][y][z][k]=0;
		return 0;
	}
	dp[x][y][z][k]=0;
	if(k == 0)
	{
		if(x != 0)
			dp[x][y][z][k]=max(dp[x][y][z][k],dfs(x-1,y,z,(k+4-1)%4)+1);
		if(y != 0)
			dp[x][y][z][k]=max(dp[x][y][z][k],dfs(x,y-1,z,(k+4-2)%4)+1);
		if(z != 0)
			dp[x][y][z][k]=max(dp[x][y][z][k],dfs(x,y,z-1,(k+4-3)%4)+1);
	}
	else
	{
		if(x != 0)
			dp[x][y][z][k]=max(dp[x][y][z][k],dfs(x-1,y,z,(k+4-1)%4));
		if(y != 0)
			dp[x][y][z][k]=max(dp[x][y][z][k],dfs(x,y-1,z,(k+4-2)%4));
		if(z != 0)
			dp[x][y][z][k]=max(dp[x][y][z][k],dfs(x,y,z-1,(k+4-3)%4));
	}
	return dp[x][y][z][k];
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	memset(dp,-1,sizeof(dp));
	for(int cc=1;cc<=cas;cc++)
	{
		printf("Case #%d: ",cc);
		int n,p;
		scanf("%d %d",&n,&p);
		memset(s,0,sizeof(s));
		for(int i=0;i<n;i++)
		{
			int t;
			scanf("%d",&t);
			s[t%p]++;
		}
		if(p == 2)
		{
			int ans=s[0]+(s[1]+1)/2;
			printf("%d\n",ans);
		}
		if(p == 3)
		{
			int add=min(s[1],s[2]);
			int ans=s[0]+add;
			s[1]-=add;
			s[2]-=add;
			ans+=(s[1]+2)/3;
			ans+=(s[2]+2)/3;
			printf("%d\n",ans);
		}
		if(p == 4)
		{
			int ans=s[0]+dfs(s[1],s[2],s[3],0);
			printf("%d\n",ans);
		}
	}
	return 0;
}
/*
3
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1

 */
