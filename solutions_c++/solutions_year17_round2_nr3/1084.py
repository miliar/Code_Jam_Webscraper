#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
typedef long long ll;
const int N = 105;

int n, q, st, ed;
int e[N], s[N];
int d[N][N];
ld f[N];

int main()
{
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas)
	{
		scanf("%d%d", &n, &q);
		for (int i = 1; i <= n; ++i)
			scanf("%d%d", &e[i], &s[i]);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				scanf("%d", &d[i][j]);
		scanf("%d%d", &st, &ed);
		printf("Case #%d: ", cas);
		for (int i = 2; i <= n; ++i) f[i] = 1e99L;
		f[1] = 0;
		for (int i = 1; i < n; ++i)
		{
			ll ride = e[i];
			for (int j = i + 1; j <= n; ++j)
			{
				ride -= d[j-1][j];
				if (ride < 0) break;
				f[j] = min(f[j], f[i] + ld(e[i] - ride) / s[i]);
			}
		}
		printf("%.9Lf\n", f[n]);
	}
	return 0;
}
