#include <cstdio>
#include <map>
using namespace std;

#define iter(i, n) for (int i = 1; i <= n; ++i)

typedef tuple<int, int, int, int, int> Index;

map<Index, int> f;
int n, P;
int dfs(int i, int j, int k, int p, int s) {
	if (i == 0 && j == 0 && k == 0 && p == 0) return 0;
	Index t = Index(i, j, k, p, s);
	if (f.find(t) != f.end()) return f[t];
	int w = 0;
	if (i) w = max(w, dfs(i - 1, j, k, p, s));
	if (j) w = max(w, dfs(i, j - 1, k, p, (s + 1) % P));
	if (k) w = max(w, dfs(i, j, k - 1, p, (s + 2) % P));
	if (p) w = max(w, dfs(i, j, k, p - 1, (s + 3) % P));
	return f[t] = (w + (s == 0));
}

int main() {
	freopen("a.in", "r", stdin);
	int tt;
	scanf("%d", &tt);
	iter(id, tt) {
		scanf("%d%d", &n, &P);
		f.clear();
		int k;
		int c[4]; c[0] = c[1] = c[2] = c[3] = 0;
		iter(i, n) scanf("%d", &k), ++c[k % P];

		printf("Case #%d: %d\n", id, dfs(c[0], c[1], c[2], c[3], 0));
	}
	return 0;
}