#include <cstdio>
#include <cstdlib>
#include <algorithm>

const int MAXN = 1007;

std::pair<int, int> a[MAXN];

int f[MAXN], g[MAXN][MAXN];
int p[MAXN];
int ans, tot;
int n, m, c;

void insert(int u, int v, int vis) {
	++p[u];
	for (int i = 1; i <= ans; ++i)
		if (g[i][v] != vis && f[i] < u) {
			g[i][v] = vis;
			++f[i];
			return ;
		}
	++ans;
	g[ans][v] = vis;
	f[ans] = 1;
}

int main() {
	int Cases;
	scanf("%d", &Cases);
	for (int Case = 1; Case <= Cases; ++Case) {
		scanf("%d%d%d", &n, &c, &m);
		for (int i = 1; i <= m; ++i)
			scanf("%d%d", &a[i].first, &a[i].second);
		std::sort(a + 1, a + m + 1);
		for (int i = 1; i <= n; ++i)
			p[i] = 0;
		for (int i = 1; i <= m; ++i)
			f[i] = 0;
		ans = tot = 0;
		for (int i = 1; i <= m; ++i)
			insert(a[i].first, a[i].second, Case);
		for (int i = 1; i <= n; ++i)
			tot += std::max(0, p[i] - ans);
		printf("Case #%d: %d %d\n", Case, ans, tot);
	}
	return 0;
}
