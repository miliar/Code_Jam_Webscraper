#include <bits/stdc++.h>
using namespace std;

struct re{
	int l, r;
}imf[201][201];

int T, n, P, Ans, ls[2000001], l_cnt;
int a[201], pak[201][201], t[201];

int main()
{
	
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case)
	{
		printf("Case #%d: ", Case); Ans = 0; l_cnt = 0;
		scanf("%d%d", &n, &P);
		for (int i = 1; i <= n; ++ i) scanf("%d", &a[i]);
		for (int i = 1; i <= n; ++ i)
			for (int j = 1; j <= P; ++ j) scanf("%d", &pak[i][j]);
		for (int j = 1; j <= n; ++ j) sort(pak[j] + 1, pak[j] + 1 + P);
		for (int i = 1; i <= P; ++ i)
		{
			for (int j = 1; j <= n; ++ j)
			{
				// 0.9 * a[j] * K <= pak[i][j]  Max K
				imf[j][i].r = pak[j][i] * 10 / (9 * a[j]);
				// 1.1 * a[j] * K >= pak[i][j]  Min K
				imf[j][i].l = (pak[j][i] * 10) / (11 * a[j]);
				if ((pak[j][i] * 10) % (11 * a[j])) ++ imf[j][i].l;
				ls[++ l_cnt] = imf[j][i].l;
				ls[++ l_cnt] = imf[j][i].r;
			}
		}
		sort(ls + 1, ls + 1 + l_cnt);
		for (int i = 1; i <= n; ++ i) t[i] = 1;
		
	/*	for (int i = 1; i <= n; ++ i)
		{
			for (int j = 1; j <= P; ++ j) printf("[ %d, %d] ", imf[i][j].l, imf[i][j].r);
			printf("\n");
		}*/
		
		for (int ii = 1; ii <= l_cnt; ++ ii)
		{
			int i = ls[ii];
			for (int j = 1; j <= n; ++ j)
			{
				while (t[j] <= P && imf[j][t[j]].r < i) ++ t[j];
			}
			while (1)
			{
				int flag = 1;
				for (int j = 1; j <= n; ++ j)
				{
					if (t[j] > P || imf[j][t[j]].l > i) flag = 0;
				}
				if (flag) 
				{
					++ Ans;
					for (int j = 1; j <= n; ++ j) ++ t[j];
				}
				else break;
			}
		}
		printf("%d\n", Ans);
	}
	return 0;
}

