#include<vector>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

const int N = 105;

const int INF = 1000000005;

int n, q;

int e[N], s[N];

int g[N][N];

double f[N][N];

int main() {
	int T;
	scanf("%d", &T);
	while (T--) {
		scanf("%d%d", &n, &q);
		for (int i = 0; i < n; ++i) {
			scanf("%d%d", e + i, s + i);
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				scanf("%d", &g[i][j]);
				if (g[i][j] == -1) {
					g[i][j] = INF;
				}
			}
			g[i][i] = 0;
		}
		for (int k = 0; k < n; ++k) {
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					g[i][j] = min(g[i][j], g[i][k] + g[k][j]);
				}
			}
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (g[i][j] > e[i]) {
					f[i][j] = 1e20;
				} else {
					f[i][j] = (double)g[i][j] / s[i];
				}
			}
		}
		for (int k = 0; k < n; ++k) {
			for (int i = 0; i < n; ++i) {
				for (int j = 0; j < n; ++j) {
					f[i][j] = min(f[i][j], f[i][k] + f[k][j]);
				}
			}
		}
		static int id = 0;
		printf("Case #%d: ", ++id);
		for (int i = 0; i < q; ++i) {
			int u, v;
			scanf("%d%d", &u, &v);
			--u, --v;
			printf("%.6f%c", f[u][v], i == q - 1 ? '\n' : ' ');
		}
	}
	return 0;
}
