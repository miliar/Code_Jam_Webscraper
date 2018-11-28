#include <iostream>
#include <cstdio>

using namespace std;

const int inf = 0x3f3f3f3f;
const int maxn = 105;
int E[maxn], a[maxn][maxn];
double S[maxn], f[maxn][maxn];

int main() {
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; ++cas) {
		int n, q;
		scanf("%d%d", &n, &q);
		for (int i = 1; i <= n; ++i) {
			scanf("%d%lf", &E[i], &S[i]);
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				scanf("%d", &a[i][j]);
				if (a[i][j] == -1) a[i][j] = inf; 
			}
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) 
			if (i!=j) {
				for (int k = 1; k <= n; ++k) 
				if (i!=k && j!=k) {
					a[j][k] = min(a[j][i] + a[i][k], a[j][k]);
				}
			}
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) {
				if (a[i][j] <= E[i]) f[i][j] = a[i][j] / S[i];
				else f[i][j] = 1e16;
			}
		}
		for (int i = 1; i <= n; ++i) {
			for (int j = 1; j <= n; ++j) 
			if (i!=j) {
				for (int k = 1; k <= n; ++k) 
				if (i!=k && j!=k) {
					f[j][k] = min(f[j][i] + f[i][k], f[j][k]);
				}
			}
		}
		printf("Case #%d: ", cas);
		for (int i = 1; i <= q; ++i) {
			int x, y;
			scanf("%d%d", &x, &y);
			printf("%.10lf", f[x][y]);
			if (i == q) puts("");
			else printf(" ");
		}
	}
	return 0;
} 
