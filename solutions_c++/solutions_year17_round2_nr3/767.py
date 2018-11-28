#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <vector>

typedef long long LL;

const int MAXN = 107;
const long long INF = 1e14;

int s[MAXN], e[MAXN];
long long f[MAXN][MAXN];
std::vector<int> d[MAXN];

double dist[MAXN];
std::priority_queue<std::pair<double, int> > heap;

int sgn(double u, double eps = 1e-8) {
	return u < -eps? -1: u > eps;
}

void work(int st, int n) {
	for (int i = 1; i <= n; ++i)
		dist[i] = 1e14;
	dist[st] = 0.0;
	while (!heap.empty()) heap.pop();
	heap.push(std::make_pair(0, st));
	while (!heap.empty()) {
		int u = heap.top().second;
		double dst = -heap.top().first;
		heap.pop();
		if (dst - dist[u] > 0) continue;
		for (int i = 0; i < (int)d[u].size(); ++i) {
			int v = d[u][i];
			if (sgn(dist[v] - dst - 1.0 * f[u][v] / s[u]) > 0) {
				dist[v] = dst + 1.0 * f[u][v] / s[u];
				heap.push(std::make_pair(-dist[v], v));
			}
		}
	}
}

int main() {
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		int n, Q;
		scanf("%d%d", &n, &Q);
		for (int i = 1; i <= n; ++i)
			scanf("%d%d", &e[i], &s[i]);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j) {
				int k;
				scanf("%d", &k);
				if (k == -1) f[i][j] = INF;
				else f[i][j] = k;
				if (i == j) f[i][j] = 0;
			}
		for (int k = 1; k <= n; ++k)
			for (int i = 1; i <= n; ++i)
				for (int j = 1; j <= n; ++j)
					f[i][j] = std::min(f[i][j], f[i][k] + f[k][j]);
		for (int i = 1; i <= n; ++i) {
			d[i].clear();
			for (int j = 1; j <= n; ++j)
				if (f[i][j] <= e[i] && i != j) d[i].push_back(j);
		}
		printf("Case #%d:", Case);
		for (int i = 1; i <= Q; ++i) {
			int u, v;
			scanf("%d%d", &u, &v);
			work(u, n);
			printf(" %.9f", dist[v]);
		}
		printf("\n");
	}
	return 0;
}
