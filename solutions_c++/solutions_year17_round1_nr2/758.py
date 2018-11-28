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

const int N = 55;
const int maxn = 2E6 + 10;
typedef double DB;
const DB A = 1.1;
const DB B = 0.9;

int n,m,T,Q[N][N],U[N][N],D[N][N],R[N];
bool vis[N][N];

vector <int> v[maxn][N];

void Solve(int I)
{
	int Min = maxn,Max = 0;
	scanf("%d%d",&n,&m);
	for (int i = 1; i <= n; i++) scanf("%d",&R[i]);
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++) scanf("%d",&Q[i][j]);
		sort(Q[i] + 1,Q[i] + m + 1);
		for (int j = 1; j <= m; j++)
		{
			D[i][j] = ceil((DB)(Q[i][j]) / A / (DB)(R[i]));
			U[i][j] = floor((DB)(Q[i][j]) / B / (DB)(R[i]));
			Min = min(Min,D[i][j]); Max = max(Max,U[i][j]);
			for (int k = D[i][j]; k <= U[i][j]; k++) v[k][i].push_back(j);
		}
	}
	int Ans = 0;
	for (int i = max(1,Min); i <= Max; i++)
	{
		int mi = 1000000;
		for (int j = 1; j <= n; j++)
		{
			int now = 0;
			for (int k = 0; k < v[i][j].size(); k++)
			{
				int t = v[i][j][k];
				if (!vis[j][t]) ++now;
			}
			mi = min(now,mi);
		}
		if (!mi)
		{
			for (int j = 1; j <= n; j++) v[i][j].clear();
			continue;
		}
		Ans += mi;
		for (int j = 1; j <= n; j++)
		{
			int cnt = 0;
			for (int k = 0; k < v[i][j].size(); k++)
			{
				if (vis[j][v[i][j][k]]) continue;
				vis[j][v[i][j][k]] = 1; ++cnt;
				if (cnt == mi) break;
			}
			v[i][j].clear();
		}
	}
	memset(vis,0,sizeof(vis));
	printf("Case #%d: %d\n",I,Ans);
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
