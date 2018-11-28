#include <bits/stdc++.h>
using namespace std;

int TC, C, R, M, dp[1055][1055], dir[4][2] = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
vector< pair<int, int> > S, T;
char g[105][105];



vector< pair<int, int> > answer;
queue< pair< int, pair<int, int> > > Q;

int tans = -1;
vector< pair<int, int> > solution;

int f(int bms, int bmt) {
	char tmpg[35][35];
	bool vis[35][35];
	bool possible[15];
	vector<int> whacks[35][35];
	if (dp[bms][bmt] != -1) return dp[bms][bmt];
	int ans = __builtin_popcount(bms);
	if (ans > tans) {
		tans = ans;
		solution = answer;
	}
	//printf("trying!\n");
	//for (int i = 0; i < answer.size(); i++) printf("meow %d %d\n", answer[i].first, answer[i].second);
	for (int i = 0; i < R; i++) {
		for (int j = 0; j < C; j++) {
			tmpg[i][j] = g[i][j];
		}
	}
	for (int i = 0; i < S.size(); i++) if (bms & (1 << i)) tmpg[S[i].first][S[i].second] = '.';
	for (int i = 0; i < T.size(); i++) if (bmt & (1 << i)) tmpg[T[i].first][T[i].second] = '.';
	for (int i = 0; i < T.size(); i++) {
		if (!(bmt & (1 << i))) {
			for (int j = 0; j < 4; j++) {
				int x = T[i].first, y = T[i].second;
				while (1) {
					whacks[x][y].push_back(i);
					//if (bms == 0 && bmt == 0) printf("%d %d = %d\n", x, y, i);
					x += dir[j][0];
					y += dir[j][1];
					if (x < 0 || x >= R) break;
					if (y < 0 || y >= C) break;
					if (tmpg[x][y] == '#') break;
				}
			}
		}
	}
	for (int i = 0; i < S.size(); i++) {
		if (!(bms & (1 << i))) {
			memset(vis, 0, sizeof(vis));
			memset(possible, 0, sizeof(possible));
			while (!Q.empty()) Q.pop();
			Q.push(make_pair(0, make_pair(S[i].first, S[i].second)));
			vis[S[i].first][S[i].second] = 1;
			while (!Q.empty()) {
				int d = Q.front().first, x = Q.front().second.first, y = Q.front().second.second;
				Q.pop();
				
				if (whacks[x][y].size() > 0) {
					//if (bms == 0 && bmt == 0) printf(" r %d %d %d\n", i, x, y);
					for (int i = 0; i < whacks[x][y].size(); i++) possible[whacks[x][y][i]] = 1;
					continue;
				}
				for (int di = 0; di < 4; di++) {
					int newx = x + dir[di][0], newy = y + dir[di][1];
					if (newx < 0 || newx >= R) continue;
					if (newy < 0 || newy >= C) continue;
					if (tmpg[newx][newy] == 'T') continue;
					if (tmpg[newx][newy] == '#') continue;
					if (vis[newx][newy]) continue;
					if (d + 1 > M) continue;
					vis[newx][newy] = 1;
					Q.push(make_pair(d + 1, make_pair(newx, newy)));
				}
			}
			for (int j = 0; j < T.size(); j++) {
				if (possible[j] && !(bmt & (1 << j))) {
					//if (bms == 0 && bmt == 0) printf("%d->%d\n", i, j);
					answer.push_back(make_pair(i, j));
					ans = max(ans, f(bms ^ (1 << i), bmt^(1<<j)));
					answer.pop_back();
				}
			}
		}
	}
	return dp[bms][bmt] = ans;
}

int main() {
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		tans = -1;
		solution.clear();
		scanf("%d%d%d", &C, &R, &M);
		for (int i = 0; i < R; i++) scanf("%s", &g[i]);
		S.clear();
		T.clear();
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				if (g[i][j] == 'S') S.push_back(make_pair(i, j));
				if (g[i][j] == 'T') T.push_back(make_pair(i, j));
			}
		}
		memset(dp, -1, sizeof(dp));
		printf("Case #%d: %d\n", tc, f(0, 0));
		for (int i = 0; i < solution.size(); i++) printf("%d %d\n", solution[i].first + 1, solution[i].second + 1);
		fprintf(stderr, "%d\n", tc);
	}
}
