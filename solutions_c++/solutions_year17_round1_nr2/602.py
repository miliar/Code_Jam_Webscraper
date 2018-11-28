#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;

const LL MOD = 1000000007LL;

int R[55];
int Q[55][55];
int ind[55];

int main()
{
	int T, N, P, ans;

	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d", &N, &P);
		for (int i = 0; i < N; i++)
			scanf("%d", R + i);
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < P; j++)
				scanf("%d", &Q[i][j]);
			sort(Q[i], Q[i] + P);
		}
		ans = 0;
		memset(ind, 0, sizeof(ind));
		for (LL s = 1; s <= 1000 * 1000; s++)
		{
			bool done = false;
			bool nxt = false;
			while (true)
			{
				for (int i = 0; i < N; i++)
				{
					while (ind[i] < P && Q[i][ind[i]] * 10 < R[i] * 9 * s)
						ind[i]++;

					if (ind[i] >= P)
					{
						done = true;
						break;
					}

					if (Q[i][ind[i]] * 10 > R[i] * 11 * s)
					{
						nxt = true;
						break;
					}
				}
				if (done || nxt)
					break;
				ans++;
				for (int i = 0; i < N; i++)
					ind[i]++;
			}
			if (done)
				break;
		}
		printf("Case #%d: %d\n", t, ans);
	}

	return 0;
}