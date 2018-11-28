#include <bits/stdc++.h>
using namespace std;
const int N = 30;
const int dx[] = {0, 0, 1, -1};
const int dy[] = {1, -1, 0, 0};
typedef pair<int, int> ii;

int n, m;
char v[N][N];
char used[N][N];
ii l, r;
char current;

bool valid (const int &x, const int &y) {
	if (x < 0 or x >= n)
		return false;
	if (y < 0 or y >= m)
		return false;
	if (used[x][y])
		return false;
	ii a = l;
	a.first = min(a.first, x);
	a.second = min(a.second, y);
	ii b = r;
	b.first = max(b.first, x);
	b.second = max(b.second, y);
	for (int i = a.first; i <= b.first; ++i) {
		for (int j = a.second; j <= b.second; ++j) {
			if (v[i][j] != '?' and v[i][j] != current)
				return false;
		}
	}
	l = a;
	r = b;
	return true;
}

void dfs (const int &i, const int &j) {
	v[i][j] = current;
	used[i][j] = true;
	for (int k = 0; k < 4; ++k) {
		int x = i + dx[k];
		int y = j + dy[k];
		if (valid(x, y))
			dfs(x, y);
	}
}

int main () {
	int test; scanf("%d", &test);
	for (int t = 1; t <= test; ++t) {
		scanf("%d %d", &n, &m);
		for (int i = 0; i < n; ++i) {
			while (getchar() != '\n');
			for (int j = 0; j < m; ++j) {
				scanf("%c", &v[i][j]);
			}
		}
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < m; ++j)
				used[i][j] = false;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (!used[i][j] and v[i][j] != '?') {
					l = make_pair(i, j);
					r = make_pair(i, j);
					current = v[i][j];
					dfs(i, j);
				}
			}
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				printf("%c", v[i][j]);
			}
			puts("");
		}
	}
	return 0;
}