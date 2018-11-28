#include <bits/stdc++.h>
using namespace std;

int T, R, C, vis[101][101];
char mp[101][101];

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case)
	{
		
		
		
		printf("Case #%d:\n", Case);
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; ++ i) scanf("%s", mp[i]);
		
		
		
		for (int i = 0; i < R; ++ i)
			for (int j = 0; j < C; ++ j)
				if (mp[i][j] != '?') vis[i][j] = 1;
				else vis[i][j] = 0;
		for (int i = 0; i < R; ++ i)
			for (int j = 0; j < C; ++ j)
				if (vis[i][j])
				{
					int yl, yr;
					for (yr = 1; j + yr < C; ++ yr) if (mp[i][j + yr] != '?') break;
					for (yl = 1; j - yl >= 0; ++ yl) if (mp[i][j - yl] != '?') break;
					for (int jj = j - yl + 1; jj < j + yr; ++ jj) mp[i][jj] = mp[i][j];
				}
		int t;
		for (t = 0; mp[t][0] == '?'; ++ t);
		for (int i = 0; i < t; ++ i)
			for (int j = 0; j < C; ++ j) mp[i][j] = mp[t][j];
		for (int i = t + 1; i < R; ++ i)
			if (mp[i][0] == '?')
				for (int j = 0; j < C; ++ j) mp[i][j] = mp[i - 1][j];
		for (int i = 0; i < R; ++ i) printf("%s\n", mp[i]);	
	}
}

