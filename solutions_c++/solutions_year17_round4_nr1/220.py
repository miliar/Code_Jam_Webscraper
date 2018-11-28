#include <bits/stdc++.h>
using namespace std;

int T, n, K, x, Sum;
int sum[11], Ans;

bool check(int x)
{
	return ((Sum - x) % K) == 0;
}

void upd(int &a, int b)
{
	if (b > a) a = b;
}

namespace four
{
	int f[101][101][101];
	void work()
	{
		for (int i = 0; i <= sum[1]; ++ i)
			for (int j = 0; j <= sum[2]; ++ j)
				for (int k = 0; k <= sum[3]; ++ k) f[i][j][k] = -1;
		f[sum[1]][sum[2]][sum[3]] = 0;
		for (int i = sum[1]; i >= 0; -- i)
			for (int j = sum[2]; j >= 0; -- j)
				for (int k = sum[3]; k >= 0; -- k)
					if (f[i][j][k] != -1)
					{
						if (i)
						{
							upd(f[i - 1][j][k], check(i - 1 + j * 2 + k * 3) + f[i][j][k]);
						}
						if (j)
						{
							upd(f[i][j - 1][k], check(i + (j - 1) * 2 + k * 3) + f[i][j][k]);
						}
						if (k)
						{
							upd(f[i][j][k - 1], check(i + j * 2 + (k - 1) * 3) + f[i][j][k]);
						}
					}
	//	printf("%d\n", check(0));
		printf("%d\n", 1 + f[0][0][0] - check(0) + sum[0]);
	}
}

namespace three
{
	int f[101][101];
	void work()
	{
		for (int i = 0; i <= sum[1]; ++ i)
			for (int j = 0; j <= sum[2]; ++ j) f[i][j] = -1;
		f[sum[1]][sum[2]] = 0;
		for (int i = sum[1]; i >= 0; -- i)
			for (int j = sum[2]; j >= 0; -- j)
				if (f[i][j] != -1)
				{
					if (i)
					{
						upd(f[i - 1][j], f[i][j] + check(i - 1 + j * 2));
					}
					if (j)
					{
						upd(f[i][j - 1], check(i + (j - 1) * 2) + f[i][j]);
					}
				}
		printf("%d\n", 1 + f[0][0] - check(0) + sum[0]);
	}
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	
	scanf("%d", &T);
	for (int Case = 1; Case <= T; ++ Case)
	{
		printf("Case #%d: ", Case);
		scanf("%d%d", &n, &K); Sum = 0;
		for (int i = 0; i < K; ++ i) sum[i] = 0;
		for (int i = 1; i <= n; ++ i)
		{
			scanf("%d", &x); Sum = (Sum + x) % K;
			++ sum[x % K];
		}
		if (K == 2)
		{
			printf("%d\n", 1 + sum[0] + sum[1] / 2 - check(0));
		} else if (K == 3) three::work();
		else four::work();
	}
	return 0;
}

