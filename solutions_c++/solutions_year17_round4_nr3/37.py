#include <cstdio>
#include <vector>

using namespace std;

int p[5555], q[5555];
char a[64][64];
vector<int> g[11111], h[11111];
int v[11111], c[11111], s[11111], sn;

inline int hor(int i, int j) {
	return i * 51 + j;
}

inline int ver(int i, int j) {
	return i * 51 + j + 2777;
}

inline int pos(int x) {
	return x << 1;
}

inline int neg(int x) {
	return x << 1 | 1;
}

inline void then(int i, int j) {
	g[i].push_back(j);
	h[j].push_back(i);
}

int f(int x) {
	return x == p[x] ? x : p[x] = f(p[x]);
}

inline void com(int i, int j) {
	i = f(i);
	j = f(j);
	p[i] = j;
	q[j] += q[i];
}

void dfs1(int x) {
	if (v[x]) return;
	v[x] = 1;
	for (auto t : g[x]) dfs1(t);
	s[sn++] = x;
}

void dfs2(int x, int y) {
	if (!v[x]) return;
	v[x] = 0;
	c[x] = y;
	for (auto t : h[x]) dfs2(t, y);
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, Tn;
	scanf("%d", &Tn);
	for (T = 1; T <= Tn; T++) {
		int i, j, n, m;
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++) scanf("%s", a[i]);
		for (i = 0; i < 5555; i++) {
			p[i] = i;
			q[i] = 0;
		}
		for (i = 0; i < n; i++) for (j = 0; j < m; j++) {
			if (a[i][j] == '/') {
				com(hor(i, j), ver(i, j));
				com(hor(i + 1, j), ver(i, j + 1));
			}
			if (a[i][j] == '\\') {
				com(hor(i, j), ver(i, j + 1));
				com(hor(i + 1, j), ver(i, j));
			}
			if (a[i][j] == '-' || a[i][j] == '|') {
				com(hor(i, j), hor(i + 1, j));
				com(ver(i, j), ver(i, j + 1));
				q[f(hor(i, j))]++;
				q[f(ver(i, j))]++;
			}
			if (a[i][j] == '.') {
				com(hor(i, j), hor(i + 1, j));
				com(ver(i, j), ver(i, j + 1));
			}
		}
		for (i = 0; i < 11111; i++) {
			g[i].clear();
			h[i].clear();
		}
		for (i = 0; i < 5555; i++) if (q[i] != 1) then(pos(i), neg(i));
		for (i = 0; i < n; i++) for (j = 0; j < m; j++) {
			if (a[i][j] == '-' || a[i][j] == '|') {
				then(pos(f(hor(i, j))), neg(f(ver(i, j))));
				then(neg(f(hor(i, j))), pos(f(ver(i, j))));
				then(pos(f(ver(i, j))), neg(f(hor(i, j))));
				then(neg(f(ver(i, j))), pos(f(hor(i, j))));
			}
			if (a[i][j] == '.') {
				then(neg(f(hor(i, j))), pos(f(ver(i, j))));
				then(neg(f(ver(i, j))), pos(f(hor(i, j))));
			}
		}
		sn = 0;
		for (i = 0; i < 11111; i++) dfs1(i);
		while (sn--) dfs2(s[sn], sn);
		for (i = 0; i < 5555; i++) if (c[pos(i)] == c[neg(i)]) break;
		if (i < 5555) {
			printf("Case #%d: IMPOSSIBLE\n", T);
			continue;
		}
		printf("Case #%d: POSSIBLE\n", T);
		for (i = 0; i < n; i++) {
			for (j = 0; j < m; j++) if (a[i][j] == '-' || a[i][j] == '|') a[i][j] = c[pos(f(hor(i, j)))] < c[neg(f(hor(i, j)))] ? '|' : '-';
			puts(a[i]);
		}
	}
	return 0;
}