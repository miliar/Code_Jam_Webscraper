#include <bits/stdc++.h>
using namespace std;

int TC, N, M, orig[105][105], newg[105][105];
bool taken0_l[105], taken0_r[105], taken1_l[205], taken1_r[205];
vector<int> adj0[105], adj1[205];
int p[205];
bool vis[205];
string conv = ".x+o";

bool aug0(int x) {
	if (vis[x]) return 0;
	else vis[x] = 1;
	for (int i = 0; i < adj0[x].size(); i++) {
		if (p[adj0[x][i]] == -1 || aug0(p[adj0[x][i]])) {
			p[adj0[x][i]] = x;
			return 1;
		}
	}
	return 0;
}

bool aug1(int x) {
	if (vis[x]) return 0;
	else vis[x] = 1;
	for (int i = 0; i < adj1[x].size(); i++) {
		if (p[adj1[x][i]] == -1 || aug1(p[adj1[x][i]])) {
			p[adj1[x][i]] = x;
			return 1;
		}
	}
	return 0;
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		scanf("%d%d", &N, &M);
		memset(orig, 0, sizeof(orig));
		memset(newg, 0, sizeof(newg));
		memset(taken0_l, 0, sizeof(taken0_l));
		memset(taken1_l, 0, sizeof(taken1_l));
		memset(taken0_r, 0, sizeof(taken0_r));
		memset(taken1_r, 0, sizeof(taken1_r));
		for (int i = 0; i < M; i++) {
			int a, b;
			char c;
			scanf(" %c%d%d",&c, &a, &b);
			a--;
			b--;
			if (c == 'x' || c == 'o') {
				orig[a][b] |= 1;
				newg[a][b] |= 1;
				taken0_l[a] = 1;
				taken0_r[b] = 1;
			}
			if (c == '+' || c == 'o') {
				orig[a][b] |= 2;
				newg[a][b] |= 2;
				taken1_l[a - b + N - 1] = 1;
				taken1_r[a + b] = 1;
			}
		}
		for (int i = 0; i < N; i++) adj0[i].clear();
		for (int i = 0; i < 2 * N; i++) adj1[i].clear();
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!taken0_l[i] && !taken0_r[j]) adj0[i].push_back(j);
				if (!taken1_l[i - j + N - 1] && !taken1_r[i + j]) adj1[i - j + N - 1].push_back(i + j);
			}
		}
		int ans = 0;
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (orig[i][j] == 1 || orig[i][j] == 2) ans++;
				if (orig[i][j] == 3) ans += 2;
			}
		}
		// match 0
		memset(p, -1, sizeof(p));
		for (int i = 0; i < N; i++) {
			memset(vis, 0, sizeof(vis));
			ans += aug0(i);
		}
		for (int i = 0; i < N; i++) {
			if (p[i] != -1) {
				newg[p[i]][i] |= 1;
			}
		}
		memset(p, -1, sizeof(p));
		for (int i = 0; i < 2 * N; i++) {
			memset(vis, 0, sizeof(vis));
			ans += aug1(i);
		}
		for (int i = 0; i < 2 * N; i++) {
			if (p[i] != -1) {
				int aminusb = p[i] - (N - 1);
				int aplusb = i;
				int a = (aminusb + aplusb) / 2;
				int b = aplusb - a;
				newg[a][b] |= 2;
			}
		}
		int otherans = 0;
		for (int i = 0; i < N; i++)  for (int j = 0; j < N; j++) if (orig[i][j] != newg[i][j]) otherans++;
		printf("Case #%d: %d %d\n", tc, ans, otherans);
		for (int i = 0; i < N; i++)  for (int j = 0; j < N; j++) if (orig[i][j] != newg[i][j]) printf("%c %d %d\n", conv[newg[i][j]], i+1, j+1);
	}
}
