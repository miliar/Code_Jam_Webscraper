#include <bits/stdc++.h>
using namespace std;

const int maxN = 105;

typedef pair<int, int> pii;
typedef pair<double, int> pdi;
#define fi first
#define se second

long long n, q;
int E[maxN], S[maxN];
int a[maxN][maxN];
long long G[maxN][maxN];

void calc_G() {
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			if (a[i][j] == -1) G[i][j] = (long long)(1e15);
			else G[i][j] = a[i][j];
		}
	// floyd on a
	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++) {
				G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
			}
	//
	// for (int i = 1; i <= n; i++) for (int j = 1; j <= n; j++) printf("%lld\n", G[i][j]);
}

double query(int s, int t) {
	double d[maxN];
	bool visited[maxN];
	for (int i = 1; i <= n; i++) {
		d[i] = (i == s) ? 0.0 : 1e15;
		visited[i] = false;
	}
	while (true) {
		int u = -1;
		double mind = 1e15;
		for (int i = 1; i <= n; i++) if (!visited[i] && d[i] < mind) {
			mind = d[i];
			u = i;
		}
		visited[u] = true;
		// printf("u = %d (%.2f)\n", u, d[u]);
		if (u == t) return d[u];
		for (int i = 1; i <= n; i++) if (G[u][i] <= E[u]) {
			// printf("to %d: %lld -> %.2f\n", i, G[u][i], 1.0*G[u][i]/S[u]);
			d[i] = min(d[i], d[u] + 1.0*G[u][i]/S[u]);
		}
	}
	return -1.0;
}

void solve() {
	// input
	scanf("%d%d", &n, &q);
	for (int i = 1; i <= n; i++) {
		scanf("%d%d", &E[i], &S[i]);
	}
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) scanf("%d", &a[i][j]);
	// process
	calc_G();
	// query
	for (int i = 0; i < q; i++) {
		int u, v; scanf("%d%d", &u, &v);
		printf(" %.9f", query(u, v));
	}
	printf("\n");
}

int main() {
	freopen("C.out", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d:", i);
		solve();
	}
}