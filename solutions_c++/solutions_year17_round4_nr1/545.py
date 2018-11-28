#include <bits/stdc++.h>

using namespace std;

const int maxn = 102;

int f[4][maxn][maxn][maxn];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++)
	{
		printf("Case #%d: ", t);
		int n, p;
		cin >> n >> p;
		int cnt[4] = {0, 0, 0, 0};
		for (int i = 1; i <= n; ++i)
		{
			int x;
			cin >> x;
			++cnt[x % p];
		}
		int ans = 0;
		if (p == 2)
		{
			ans += (cnt[1] + 1) / 2;
		}
		else if (p == 3)
		{
			int tmp = min(cnt[1] , cnt[2]);
			ans += tmp + (cnt[1] - tmp) / 3 + (cnt[2] - tmp) / 3 +
				((cnt[1] - tmp) % 3 > 0 || (cnt[2] - tmp) % 3 > 0);
		}
		else if (p == 4)
		{
			for (int i = 0; i < p; ++i)
				for (int a1 = 0; a1 <= cnt[1]; a1++)
					for (int a2 = 0; a2 <= cnt[2]; a2++)
						for (int a3 = 0; a3 <= cnt[3]; a3++)
							f[i][a1][a2][a3] = 0;
			f[0][0][0][0] = 0;
			for (int a1 = 0; a1 <= cnt[1]; a1++)
				for (int a2 = 0; a2 <= cnt[2]; a2++)
					for (int a3 = 0; a3 <= cnt[3]; a3++)
						for (int i = 0; i < p; ++i)
						{
							f[(i + 1) % p][a1 + 1][a2][a3] =
								max(f[(i + 1) % p][a1 + 1][a2][a3],
									f[i][a1][a2][a3] + ((i) % p == 0));
							f[(i + 2) % p][a1][a2 + 1][a3] =
								max(f[(i + 2) % p][a1][a2 + 1][a3],
									f[i][a1][a2][a3] + ((i) % p == 0));
							f[(i + 3) % p][a1][a2][a3 + 1] =
								max(f[(i + 3) % p][a1][a2][a3 + 1],
									f[i][a1][a2][a3] + ((i) % p == 0));
						}
			for (int i = 0; i < p; ++i)
				ans = max(ans, f[i][cnt[1]][cnt[2]][cnt[3]]);
		}
		printf("%d\n", ans + cnt[0]);
	}
	return 0;
}
 
