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
lld g[110][110];
lld limit[110];
double speed[110];
bool vis[110];
double dp[110];
int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int cas;
	scanf("%d",&cas);
	for(int cc=1;cc<=cas;cc++)
	{
		int n,Q;
		scanf("%d %d",&n,&Q);
		for(int i=0;i<n;i++)
			scanf("%I64d %lf",&limit[i],&speed[i]);
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
				scanf("%I64d",&g[i][j]);
		for(int k=0;k<n;k++)
			for(int i=0;i<n;i++)
				for(int j=0;j<n;j++)
				{
					if(g[i][k] != -1 && g[k][j] != -1)
					{
						if(g[i][j] == -1)
							g[i][j]=g[i][k]+g[k][j];
						else
							g[i][j]=min(g[i][j],g[i][k]+g[k][j]);
					}
				}
		printf("Case #%d:",cc);
		while(Q--)
		{
			int src,tc;
			scanf("%d %d",&src,&tc);
			src--;
			tc--;
			for(int i=0;i<n;i++)
				dp[i]=-1,vis[i]=false;
			dp[src]=0;
			vis[src]=true;
			for(int i=0;i<n;i++)
				if(!vis[i] && g[src][i] != -1 && limit[src] >= g[src][i])
				{
					if(dp[i] == -1)
						dp[i]=1.0*g[src][i]/speed[src];
					else
						dp[i]=min(dp[i],1.0*g[src][i]/speed[src]);
				}
			for(int l=1;l<n;l++)
			{
				int at=-1;
				for(int i=0;i<n;i++)
					if(!vis[i] && dp[i] != -1)
					{
						if(at == -1)
							at=i;
						else if(dp[i] < dp[at])
							at=i;
					}
				if(at == -1)
					break;
				vis[at]=true;
				for(int i=0;i<n;i++)
					if(!vis[i] && g[at][i] != -1 && limit[at] >= g[at][i])
					{
						if(dp[i] == -1)
							dp[i]=dp[at]+1.0*g[at][i]/speed[at];
						else
							dp[i]=min(dp[i],dp[at]+1.0*g[at][i]/speed[at]);
					}
			}
			printf(" %.8f",dp[tc]);
		}
		printf("\n");
	}
	return 0;
}
/*
3
3 1
2 3
2 4
4 4
-1 1 -1
-1 -1 1
-1 -1 -1
1 3
4 1
13 10
1 1000
10 8
5 5
-1 1 -1 -1
-1 -1 1 -1
-1 -1 -1 10
-1 -1 -1 -1
1 4
4 3
30 60
10 1000
12 5
20 1
-1 10 -1 31
10 -1 10 -1
-1 -1 -1 10
15 6 -1 -1
2 4
3 1
3 2

 */
