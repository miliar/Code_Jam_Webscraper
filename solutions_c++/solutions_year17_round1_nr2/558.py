#include <stdio.h>
#include <algorithm>
using namespace std;

int a[60];
int b[60][60];
int p[60];

int N, P;

pair<int, int> range(int val, int i)
{
	int L = (val * 10 - 1) / (a[i] * 11) + 1;
	int R = (val * 10) / (a[i] * 9);

	return make_pair(L, R);
}


pair<int, int> rg(int i)
{
	return range(b[i][p[i]], i);
}


int main()
{
	int T;
	scanf("%d", &T);
	for (int re = 1; re <= T; re++)
	{
		scanf("%d%d", &N, &P);
		//printf("%d %d\n", N, P);

		for (int i = 0; i < N; i++)
		{
			scanf("%d", a + i);
			//printf("%d ", a[i]);
		}

		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < P; j++)
			{
				scanf("%d", &b[i][j]);
				//printf("%d ", b[i][j]);
			}
			//puts("");
			sort(b[i], b[i] + P);
		}

		memset(p, 0, sizeof(p));

		int ans = 0;
		bool flag = false;

		while (!flag)
		{
			int L = -1;
			int R = 1000000000;
			pair<int, int> pi;

			for (int i = 0; i < N; i++)
			{
				pi = rg(i);
				if (L < pi.first)
				{
					L = pi.first;
				}
				if (R > pi.second)
				{
					R = pi.second;
				}
			}

			//printf("%d %d\n", L, R);

			if (L > R)
			{
				for (int i = 0; i < N; i++)
				{
					pi = rg(i);
					if (R == pi.second)
					{
						p[i]++;
						flag = (p[i] >= P);
					}
				}
			}
			else
			{
				ans++;
				for (int i = 0; i < N; i++)
				{
					p[i]++;
					flag = (p[i] >= P);
				}
			}

			for (int i = 0; i < N; i++)
			{
				//printf("p[i]=%d\n", p[i]);
				if (p[i] >= P) break;
			}
		}

		printf("Case #%d: %d\n", re, ans);

	}
}