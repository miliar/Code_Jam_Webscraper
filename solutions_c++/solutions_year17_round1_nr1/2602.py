#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long LL;
const int maxn = 1e5+5;

int n,m,sum[50][50];
char g[50][50];

int main()
{
	int T;
	freopen("A-large.in","r",stdin);
	freopen("Ajjy.txt","w",stdout);
	scanf("%d",&T);
	for(int kase = 1;kase <= T;kase++)
	{
		scanf("%d %d",&n,&m);
		int cnt = 0;
		memset(sum,0,sizeof(sum));
		for(int i = 1;i <= n;i++) 
		{
			scanf("%s",g[i]+1);
			for(int j = 1;j <= m;j++) 
			{
				if(g[i][j] == '?')
				{
					cnt++;
				}
			}
		}

		printf("Case #%d:\n",kase);
		if(cnt == 0) 
		{
			for(int i = 1;i <= n;i++) printf("%s\n",g[i]+1);
			continue;
		}

		for(int i = 1;i <= n;i++)
		{
			for(int j = 1;j <= m;j++)
			{
				if(g[i][j] == '?') continue;
				int nx = i-1;
				while(nx >= 1 && g[nx][j] == '?') g[nx][j] = g[i][j],nx--;
			}
		}

		for(int i = 1;i <= n;i++)
		{
			for(int j = 1;j <= m;j++)
			{
				if(g[i][j] == '?') continue;
				int nx = i+1;
				while(nx <= n && g[nx][j] == '?') g[nx][j] = g[i][j],nx++;
			}
		}

		for(int i = 1;i <= n;i++)
		{
			for(int j = 1;j <= m;j++)
			{
				if(g[i][j] == '?') continue;
				int ny = j-1;
				while(ny >= 1 && g[i][ny] == '?') g[i][ny] = g[i][j],ny--;
			}
		}

		for(int i = 1;i <= n;i++)
		{
			for(int j = 1;j <= m;j++)
			{
				if(g[i][j] == '?') continue;
				int ny = j+1;
				while(ny <= m && g[i][ny] == '?') g[i][ny] = g[i][j],ny++;
			}
		}

		for(int i = 1;i <= n;i++) printf("%s\n",g[i]+1);

	}
	return 0;
}