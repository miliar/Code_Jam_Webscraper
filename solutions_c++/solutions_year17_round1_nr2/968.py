#include <stdio.h>
#include <string.h>
#include <math.h>
#include <queue>
#include <utility>
#include <map>
#include <set>

using namespace std;

const int maxn = 60;
const int maxp = 60;

vector<pair<int, int> >  a[maxn + 1];
int res, n, P;
int R[maxn + 1];
bool done[maxn + 1];
int dy[maxn + 1];

void gao(int x, int r, int &t1, int &t2) {
	t1 = x / (1.1 * r);
	if (x / (1.1 * r) - t1 > 1e-8) ++t1;
	t2 = x / (0.9 * r);
	if (t2 + 1 - x / (0.9 * r) < 1e-8) ++t2;
	if (t1 < 1) t1 = 1;
}

void init() {
	int i, j, x, t1, t2;
	scanf("%d%d", &n, &P);
	for (i = 1; i <= maxn; ++i) a[i].clear();
	for (i = 1; i <= n; ++i) scanf("%d", &R[i]);
	for (i = 1; i <= n; ++i) {
		for (j = 1; j <= P; ++j) {
			scanf("%d", &x);
			gao(x, R[i], t1, t2);
			if (t1 <= t2) {
				a[i].push_back(pair<int, int>(t1, t2));
			}
		}
		sort(a[i].begin(), a[i].end());
	}
}

int zd(int x, int y) {
	if (x > y) return x;
	else return y;
}

int zx(int x, int y) {
	if (x < y) return x;
	else return y;
}

void dfs(int l, int now) {
	int i;
	if (a[1].size() - l + now <= res) return;
	if (l >= a[1].size()) {
		if (now > res) res = now;
		return;
	}
	for (i = 0; i < a[2].size(); ++i) {
		if (!done[i] && zd(a[1][l].first, a[2][i].first) <= zx(a[1][l].second, a[2][i].second)) {
			done[i] = true;
			dy[l] = i;
			dfs(l + 1, now + 1);
			done[i] = false;
		}
	}
	dfs(l + 1, now);
}

void work() {
	int i;
	res = 0;
	if (n == 1) {
		res = a[1].size();
		return;
	}
	// n == 2
	for (i = 0; i < a[2].size(); ++i) done[i] = false;
	dfs(0, 0);
}

void output() {
	printf("%d\n", res);
}

int main() {
	int T, t;
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	scanf("%d", &T);
	for (t = 1; t <= T; ++t)
	{
		if (t == 44) {
			t = t;
		}
		printf("Case #%d: ", t);
		init();
		work();
		output();
	}
	return 0;
}