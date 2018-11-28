#include <cstdio>
#include <cstring>
const char ch[6] = {'R', 'G', 'Y', 'V', 'B', 'O'};
int n, a[6];
int ans[6005];
void work()
{
	for (int i = 0; i < 6; i += 2)
	{
		if (a[i] < a[i + 1])
		{
			printf("IMPOSSIBLE\n");
			return;
		}
		if (a[i] == a[i + 1] && a[i] != 0)
		{
			//printf("%d %d\n", a[i], a[i + 1]);
			if (a[i] + a[i + 1] != n)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
			else
			{
				for (int j = 0; j < n; j += 2)
					printf("%c%c", ch[i], ch[i + 1]);
				return;
			}
		}
	}
	a[0] -= a[1];
	a[2] -= a[3];
	a[4] -= a[5];
	if (a[0] > a[2] + a[4] || a[2] > a[0] + a[4] || a[4] > a[0] + a[2])
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	memset(ans, 0, sizeof(ans));
	int end = 0;
	int rank1 = 0, rank2 = 2, rank3 = 4;
	if (a[rank1] < a[rank2])
	{
		rank1 ^= rank2;
		rank2 ^= rank1;
		rank1 ^= rank2;
	}
	if (a[rank1] < a[rank3])
	{
		rank1 ^= rank3;
		rank3 ^= rank1;
		rank1 ^= rank3;
	}
	if (a[rank2] < a[rank3])
	{
		rank2 ^= rank3;
		rank3 ^= rank2;
		rank2 ^= rank3;
	}
	for (int i = 0; i < a[rank1] - a[rank2]; i++)
	{
		ans[end++] = rank1;
		ans[end++] = rank2;
		ans[end++] = rank1;
		ans[end++] = rank3;
	}
	for (int i = 0; i < a[rank2] - a[rank3]; i++)
	{
		ans[end++] = rank1;
		ans[end++] = rank2;
	}
	for (int i = 0; i < a[rank3] - (a[rank1] - a[rank2]); i++)
	{
		ans[end++] = rank1;
		ans[end++] = rank2;
		ans[end++] = rank3;
	}
	for (int i = 0; i < end; i++)
	{
		if (a[ans[i] + 1])
		{
			for (int j = 0; j < a[ans[i + 1]]; j++)
				printf("%c%c", ch[ans[i]], ch[ans[i] + 1]);
			printf("%c", ch[ans[i]]);
			a[ans[i] + 1] = 0;
		}
		else
			printf("%c", ch[ans[i]]);
	}
	printf("\n");
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int tt = 1; tt <= test; tt++)
	{
		scanf("%d%d%d%d%d%d%d", &n, &a[0], &a[5], &a[2], &a[1], &a[4], &a[3]);
		printf("Case #%d: ", tt);
		work();
	}
	return 0;
}
