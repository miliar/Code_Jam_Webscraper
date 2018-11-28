#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<vector>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<bitset>
#include<ext/pb_ds/priority_queue.hpp>
using namespace std;

const int N = 33;

int n,m,T;
char stk[N],p[N][N];

void Dfs(int r1,int c1,int r2,int c2)
{
	int tp = 0;
	for (int i = r1; i <= r2; i++)
		for (int j = c1; j <= c2; j++)
			if ('A' <= p[i][j] && p[i][j] <= 'Z')
				stk[++tp] = p[i][j];
	if (tp == 1)
	{
		for (int i = r1; i <= r2; i++)
			for (int j = c1; j <= c2; j++)
				p[i][j] = stk[1];
		return;
	}
	int sum = 0;
	for (int i = r1; i < r2; i++)
	{
		for (int j = c1; j <= c2; j++)
			if ('A' <= p[i][j] && p[i][j] <= 'Z') ++sum;
		if (sum && sum < tp)
		{
			Dfs(r1,c1,i,c2);
			Dfs(i + 1,c1,r2,c2);
			return;
		}
	}
	sum = 0;
	for (int j = c1; j < c2; j++)
	{
		for (int i = r1; i <= r2; i++)
			if ('A' <= p[i][j] && p[i][j] <= 'Z') ++sum;
		if (sum && sum < tp)
		{
			Dfs(r1,c1,r2,j);
			Dfs(r1,j + 1,r2,c2);
			return;
		}
	}
}

void Solve(int I)
{
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
		scanf("%s",p[i] + 1);
	Dfs(1,1,n,m);
	printf("Case #%d:\n",I);
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
			putchar(p[i][j]); puts("");
	}
}

int main()
{
	#ifdef DMC
		freopen("DMC.txt","r",stdin);
		freopen("test.txt","w",stdout);
	#endif
	
	cin >> T;
	for (int I = 1; I <= T; I++) Solve(I);
	return 0;
}
