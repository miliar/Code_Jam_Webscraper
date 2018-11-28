#include <cstdio>
#include <cstring>
int n, p, sum[4];
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		int now;
		scanf("%d%d", &n, &p);
		memset(sum, 0, sizeof(sum));
		for (int i = 1; i <= n; i++)
		{
			int tmp;
			scanf("%d", &tmp);
			sum[tmp % p]++;
		}
		printf("Case #%d: ", tt);
		if (p == 2)
			printf("%d\n", sum[0] + (sum[1] + 1 >> 1));
		else if (p == 3)
		{
			if (sum[1] > sum[2])
			{
				sum[1] ^= sum[2];
				sum[2] ^= sum[1];
				sum[1] ^= sum[2];
			}
			printf("%d\n", sum[0] + sum[1] + (sum[2] - sum[1] + 2) / 3);
		}
		else
		{
			int ans = 0;
			ans = sum[0] + sum[2] / 2;
			sum[2] %= 2;
			if (sum[1] > sum[3])
			{
				sum[1] ^= sum[3];
				sum[3] ^= sum[1];
				sum[1] ^= sum[3];
			}
			ans += sum[1];
			sum[3] -= sum[1];
			sum[1] = 0;
			if (sum[2] == 1 && sum[3] == 0 && sum[1] == 0)
				ans++;
			if (sum[2] == 1 && sum[3] > 1)
			{
				ans++;
				sum[3] -= 2;
				sum[2] = 0;
			}
			ans += (sum[3] + 3) / 4;
			printf("%d\n", ans); 
		}
	}
	return 0;
}
