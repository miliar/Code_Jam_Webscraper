#include <bits/stdc++.h>

using namespace std;

const int MAXN = 1E2 + 10;

int n, m;
int s0[MAXN][MAXN], s[MAXN][MAXN];

int getId(char c){
	return c == '+' ? 1 : c == 'x' ? 2 : 3;
}

int getType(int x){
	return x == 1 ? '+' : x == 2 ? 'x' : 'o';
}

int row[MAXN], col[MAXN];

void checkStar(){
	fill_n(row + 1, n, 0);
	fill_n(col + 1, n, 0);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
			if (s0[i][j] & 2)
				++row[i], ++col[j];

	vector<int> a, b;
	for (int i = 1; i <= n; ++i){
		if (!row[i])
			a.push_back(i);
		if (!col[i])
			b.push_back(i);
	}

	for (int i = 0; i < a.size() && i < b.size(); ++i)
		s[a[i]][b[i]] |= 2;
}

int c[MAXN << 1], d[MAXN << 1];

vector<int> E[MAXN << 1];
int mat[MAXN << 1];
bool vis[MAXN << 1];

bool findPath(int u){
	for (auto &v: E[u])
		if (!vis[v] && (vis[v] = true, mat[v] < 0 || findPath(mat[v])))
			return mat[v] = u, true;
	return false;
}

void Hungary(int n, int m){
	fill_n(mat + 1, m, -1);
	for (int i = 1; i <= n; ++i){
		fill_n(vis + 1, m, false);
		findPath(i);
	}
}

void checkPlus(){
	int n0 = n << 1;
	fill_n(c, n0, 0);
	fill_n(d, n0, 0);
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
			if (s0[i][j] & 1)
				++c[i + j - 1], ++d[i - j + n];

	for (int i = 1; i <= n0; ++i)
		E[i].clear();
	for (int i = 1; i <= n; ++i)
		for (int j = 1; j <= n; ++j)
			if (!c[i + j - 1] && !d[i - j + n])
				E[i + j - 1].push_back(i - j + n);

	Hungary(n0, n0);
	for (int i = 1; i <= n0; ++i)
		if (mat[i] > 0){
			int x = i + mat[i] - n + 1 >> 1, y = x + n - i;
			s[x][y] |= 1;
		}
}

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		scanf("%d%d", &n, &m);
		for (int i = 1; i <= n; ++i){
			fill_n(s0[i] + 1, n, 0);
			fill_n(s[i] + 1, n, 0);
		}
		char type[5];
		for (int x, y, i = 0; i < m; ++i){
			scanf("%s%d%d", type, &x, &y);
			s0[x][y] = s[x][y] = getId(type[0]);
		}

		checkStar();
		checkPlus();

		int score = 0, cnt = 0;
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j){
				score += (s[i][j] & 1) + (s[i][j] >> 1 & 1);
				cnt += s[i][j] != s0[i][j];
			}
		printf("%d %d\n", score, cnt);
		for (int i = 1; i <= n; ++i)
			for (int j = 1; j <= n; ++j)
				if (s0[i][j] != s[i][j])
					printf("%c %d %d\n", getType(s[i][j]), i, j);
	}
	return 0;
}
