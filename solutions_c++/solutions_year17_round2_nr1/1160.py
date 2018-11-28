#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
const ld eps = 1e-11L;
const int N = 1005;

int m, n;
int k[N], s[N];

int main()
{
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas)
	{
		scanf("%d%d", &m, &n);
		ld  t = 0.0;
		for (int i = 1; i <= n; ++i)
		{
			scanf("%d%d", &k[i], &s[i]);
			t = max(t, (ld)(m - k[i]) / s[i]);
		}
		printf("Case #%d: %.9Lf\n", cas, m / t);
	}
	return 0;
}
