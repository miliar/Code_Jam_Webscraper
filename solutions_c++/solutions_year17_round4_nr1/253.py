#include<cstdio>
int main()
{
	int i;
	int t, tc;
	scanf("%d", &tc);
	for (t = 1; t <= tc; t++)
	{
		int n, p;
		int cnt[5] = { 0, 0, 0, 0, 0 };
		scanf("%d%d", &n, &p);
		for (i = 1; i <= n; i++)
		{
			int x;
			scanf("%d", &x);
			cnt[x%p]++;
		}
		int ans = cnt[0];
		if (p == 2) ans += (cnt[1] + 1) / 2;
		else if (p == 3)
		{
			int k = cnt[1] < cnt[2] ? cnt[1] : cnt[2];
			ans += k;
			cnt[1] -= k; cnt[2] -= k;
			if (cnt[1]) ans += (cnt[1] + 2) / 3;
			if (cnt[2]) ans += (cnt[2] + 2) / 3;
		}
		else if (p == 4)
		{
			ans += (cnt[2] / 2);
			cnt[2] &= 1;
			int k = cnt[1] < cnt[3] ? cnt[1] : cnt[3];
			ans += k;
			cnt[1] -= k; cnt[3] -= k;
			if (cnt[2] == 1 && cnt[1] >= 2)
			{
				ans++; cnt[2] = 0; cnt[1] -= 2;
			}
			if (cnt[2] == 1 && cnt[3] >= 2)
			{
				ans++; cnt[2] = 0; cnt[3] -= 2;
			}
			if (cnt[1]) ans += (cnt[1] + 3) / 4;
			if (cnt[3]) ans += (cnt[3] + 3) / 4;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
