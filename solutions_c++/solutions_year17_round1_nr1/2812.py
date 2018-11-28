#include <bits/stdc++.h>

using namespace std;

char mm[30][30];
bool vis[26];

bool judge(int lx, int rx, int uy, int dy)
{
	int cnt = 0;
	for(int i = lx; i <= rx; ++i)
	{
		for(int j = uy; j <= dy; ++j)
			if(mm[j][i] != '?') ++cnt;
	}
	return cnt == 1;
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int cn = 1; cn <= n; ++cn)
	{
		memset(vis, 0, sizeof(vis));
		int cy, cx;
		scanf("%d %d", &cy, &cx);
		for(int i = 0; i != cy; ++i)
			scanf("%s", mm[i]);
		for(int x = 0; x != cx; ++x)
		{
			for(int y = 0; y != cy; ++y)
			{
				if(mm[y][x] != '?' && !vis[mm[y][x] - 'A'])
				{
					vis[mm[y][x] - 'A'] = true;
					int maxrb = x, minlb = x, minub = y, maxbb = y;
					for(int rx = x; rx < cx; ++rx)
					{
						for(int lx = x; lx >= 0; --lx)
						{
							for(int uy = y; uy >= 0; --uy)
							{
								for(int dy = y; dy < cy; ++dy)
								{
									if(judge(lx, rx, uy, dy) && (1 + rx - lx) * (1 + dy - uy) > (1 + maxrb - minlb) * (1 + maxbb - minub))
									{
										maxrb = rx;
										minlb = lx;
										maxbb = dy;
										minub = uy;
									}
								}
							}
						}
					}
					for(int i = minub; i <= maxbb; ++i)
					{
						for(int j = minlb; j <= maxrb; ++j)
							mm[i][j] = mm[y][x];
					}
				}
			}
		}
		printf("Case #%d:\n", cn);
		for(int i = 0; i != cy; ++i)
			printf("%s\n", mm[i]);
	}
	return 0;
}
