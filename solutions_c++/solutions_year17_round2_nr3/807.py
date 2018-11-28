# include <bits/stdc++.h>
using namespace std;

const int maxn = 120;

int T, cas = 0;
int e[maxn], s[maxn];
int d[maxn][maxn];
double f[maxn][maxn];
int main() {
	scanf("%d", &T);
	while(T--) {
		int n, q;
		scanf("%d%d", &n, &q);
		printf("Case #%d:", ++cas);
		for(int i = 1; i <= n; ++i) 
			scanf("%d%d", &e[i], &s[i]);
		for(int i = 1; i <= n; ++i) {
			for(int j = 1; j <= n; ++j) {
				scanf("%d", &d[i][j]);
			}
		}
		f[n][n] = 0;
		for(int i = n - 1; i > 0; --i) {
			int v = s[i];
			double dist = 0;
			for(int j = i + 1; j <= n; ++j) {
				dist += d[j-1][j];
				if(dist <= e[i]) {
					f[i][j] = dist / v;
				} else {
					f[i][j] = 1e30;
				}
			}
			for(int j = i + 1; j <= n; ++j) {
				for(int k = j + 1; k <= n; ++k) {
					f[i][k] = min(f[i][k], f[i][j] + f[j][k]);
				}
			}
		}
		while(q--) {
			int u, v; scanf("%d%d", &u, &v);
			printf(" %lf", f[u][v]);
		}
		puts("");
	}
	return 0;
}

