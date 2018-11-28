#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T, n, m;
long long a[110][110], go[110], sp[110];
long double d[110][110];

int main()  {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	cin >> T;
	for (int C = 1; C <= T; C++) {
		cin >> n >> m;
		for (int i = 1; i <= n; i++) scanf("%lld%lld", &go[i], &sp[i]);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				scanf("%lld", &a[i][j]);
				if (a[i][j] == -1) a[i][j] = 1ll << 50;
			}
		for (int i = 1; i <= n; i++) a[i][i] = 0;
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				d[i][j] = 1e20;
				if (a[i][j] <= go[i])
					d[i][j] = (long double)a[i][j] * 1.0 / sp[i];
			}
		for (int k = 1; k <= n; k++)
			for (int i = 1; i <= n; i++)
				for (int j = 1; j <= n; j++)
					d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
		printf("Case #%d:", C);
		for (int i = 1; i <= m; i++) {
			int s, t;
			scanf("%d%d", &s, &t);
			printf(" %.10Lf", d[s][t]);
		}
		puts("");
	}
}