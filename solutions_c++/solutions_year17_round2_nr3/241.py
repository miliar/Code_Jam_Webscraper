#include <cstring>
#include <cstdio>
#include <algorithm>

using namespace std;
typedef long long LL;

const int MAXN = 105;

LL d[MAXN][MAXN];
int n, q, e[MAXN], s[MAXN];
double f[MAXN][MAXN];

void up1(LL &x, LL y) {
	if (x == -1) x = y; else
		x = min(x, y);
}

void up2(double &x, double y) {
	if (x == -1) x = y; else
		x = min(x, y);
}

void solve(int tim) {
	printf("Case #%d: ", tim);
	scanf("%d%d", &n, &q);
	for (int i = 1; i <= n; i ++) scanf("%d%d", &e[i], &s[i]);
	for (int i = 1; i <= n; i ++)
		for (int j = 1; j <= n; j ++)
			scanf("%lld", &d[i][j]);
	for (int k = 1; k <= n; k ++) 
		for (int i = 1; i <= n; i ++)
			if (d[i][k] != -1)
			for (int j = 1; j <= n; j ++)
				if (d[k][j] != -1 && i != j) up1(d[i][j], d[i][k] + d[k][j]);
	for (int i = 1; i <= n; i ++)
		for (int j = 1; j <= n; j ++)
			if (d[i][j] != -1 && d[i][j] <= e[i]) f[i][j] = 1.0 * d[i][j] / s[i]; else f[i][j] = -1;
	for (int k = 1; k <= n; k ++)
		for (int i = 1; i <= n; i ++)
			if (f[i][k] != -1) 
			for (int j = 1; j <= n; j ++)
				if (f[k][j] != -1 && i != j) up2(f[i][j], f[i][k] + f[k][j]);
	for (int i = 1; i <= q; i ++) {
		int u, v;
		scanf("%d%d", &u, &v);
		printf("%.8lf ", f[u][v]);
	}
	printf("\n");
}

int main() {
	//freopen("data.in", "r", stdin), freopen("data.out", "w", stdout);
	
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i ++) solve(i);
}