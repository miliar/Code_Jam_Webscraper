#include <bits/stdc++.h>
using namespace std;

int n, C, m, T, x, y, Ans, Ans2, lim;
int sum[2001], tot[2001];

bool check(int K)
{
	int res = 0;
	for (int i = 1; i <= C; ++ i)
	{
		res += K;
		if (sum[i] > res) return 0;
		res -= sum[i];
	}
	return 1;
}

int main()
{
	
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case)
	{
		printf("Case #%d: ", Case);
		scanf("%d%d%d", &C, &n, &m);
		for (int i = 1; i <= n; ++ i) tot[i] = 0;
		for (int i = 1; i <= C; ++ i) sum[i] = 0;
		for (int i = 1; i <= m; ++ i)
		{
			scanf("%d%d", &x, &y);
			++ sum[x]; ++ tot[y];
		}
		lim = 0;
		for (int i = 1; i <= n; ++ i) lim = max(lim, tot[i]);
		int l = lim; int r = m; Ans = m;
		while (l <= r)
		{
			int mid = (l + r) >> 1;
			if (check(mid))
			{
				r = mid - 1;
				if (mid < Ans) Ans = mid;
			} else l = mid + 1;
		}
		Ans2 = 0;
		for (int i = 1; i <= C; ++ i)
			if (sum[i] >= Ans) Ans2 += sum[i] - Ans;
		printf("%d %d\n", Ans, Ans2);
	}
	return 0;
}

