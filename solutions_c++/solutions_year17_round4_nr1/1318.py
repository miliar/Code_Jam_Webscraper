#include<cstdio>

int T, n, m, tot[5], a, ans;
int min(int a, int b){return (a < b)? a : b;}
int Calc()
{
	ans = tot[0];
	if (m == 2)
	{
		while (tot[1] > 0)
		{
			ans++;
			tot[1] -= 2;
		}
		return ans;
	}
	if (m == 3)
	{
		int temp = min(tot[1], tot[2]);
		ans += temp;
		tot[1] -= temp;
		tot[2] -= temp;
		ans += tot[1] / 3;
		if (tot[1] % 3) ans++;
		ans += tot[2] / 3;
		if (tot[2] % 3) ans++;
		return ans;
	}
	if (m == 4)
	{
		ans += tot[2] / 2;
		tot[2] %= 2;
		int temp = min(tot[1], tot[3]);
		ans += temp;
		tot[1] -= temp;
		tot[3] -= temp;
		if (tot[2])
		{
			if (tot[3] >= 2)
			{
				ans++;
				tot[2]--;
				tot[3] -= 2;
			}
			if (tot[1] >= 2)
			{
				ans++;
				tot[2]--;
				tot[1] -= 2;
			}
		}
		ans += tot[1] / 4;
		if (tot[1] % 4) ans++;
		ans += tot[3] / 4;
		if (tot[3] % 4) ans++;
		if (!(tot[1] % 4) && !(tot[3] % 4) && tot[2]) ans++;
		return ans;
	}
	return 0;
}

int main()
{
//	freopen("A.in", "r", stdin);
//	freopen("A.out", "w", stdout);
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		scanf("%d%d", &n, &m);
		for (int i = 0; i <= m; i++) tot[i] = 0;
		for (int i = 1; i <= n; i++)
		{
			scanf("%d", &a);
			tot[a % m]++;
		}
		printf("Case #%d: %d\n", I, Calc());
	}
	return 0;
}
