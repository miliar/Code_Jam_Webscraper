#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;

#define iter(i, n) for (int i = 1; i <= n; ++i)
#define forw(i, a, b) for (int i = a; i <= b; ++i)

#define NR 730
int bel[2 * NR];
int f[NR][NR][2][2], n, m;
const int inf = 1e9;
int dfs(int i, int j, bool d, bool s) {
	if (i > 720 || j > 720) return inf;
	if (i + j == 1440) {
		//printf("%d %d\n", i, j);
		return d != s;
	}
	int &w = f[i][j][d][s];
	if (w != -1) return w;

	w = inf;

	if (bel[i + j] != 0)
		w = min(w, dfs(i + 1, j, 0, s) + (d == 1));
	if (bel[i + j] != 1)
		w = min(w, dfs(i, j + 1, 1, s) + (d == 0));

	return w;
}

int main() {
	freopen("B.in", "r", stdin);
	int tt;
	scanf("%d", &tt);
	iter(id, tt) {
		scanf("%d%d", &n, &m);
		memset(bel, -1, sizeof(bel));
		memset(f, -1, sizeof(f));

		iter(i, n) {
			int l, r;
			scanf("%d%d", &l, &r);
			forw(k, l, r - 1) bel[k] = 0;
		}

		iter(i, m) {
			int l, r;
			scanf("%d%d", &l, &r);
			forw(k, l, r - 1) bel[k] = 1;
		}
		printf("Case #%d: %d\n", id, min(dfs(0, 0, 0, 0), dfs(0, 0, 1, 1)));
	}
	return 0;
}