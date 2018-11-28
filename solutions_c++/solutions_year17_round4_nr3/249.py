#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
char board[100][100];
vector<pair<int, int>> laser;
int di[] = { 0, 1, 0, -1 };
int dj[] = { 1, 0, -1, 0 };

int rotateLaser(int dir, char mirror) {
	if (mirror == '/') {
		return 3 - dir;
	}
	else {
		return dir ^ 1;
	}
}

bool laserCheck(int i, int j, bool sw, vector<int>& elist) {
	int dd[2];
	if (sw == false) {
		dd[0] = 0;
		dd[1] = 2;
	}
	else {
		dd[0] = 1;
		dd[1] = 3;
	}
	elist.clear();

	for (int p = 0; p < 2; ++p) {
		int ci = i, cj = j;
		int cd = dd[p];
		ci += di[cd];
		cj += dj[cd];
		while (0 <= ci && ci < n && 0 <= cj && cj < m) {
			if (board[ci][cj] == '#') break;
			if (board[ci][cj] == '-' || board[ci][cj] == '|') {
				elist.clear();
				return false;
			}
			if (board[ci][cj] == '.') elist.push_back(ci * m + cj);

			if (board[ci][cj] == '/' || board[ci][cj] == '\\') {
				cd = rotateLaser(cd, board[ci][cj]);
			}
			ci += di[cd];
			cj += dj[cd];
		}
	}
	return true;
}

vector<vector<int>> targets[2];
vector<pair<int, int>> laserlist[100][100];
bool possible[1000][2];

const int MAXN = 30000;
int vn;
vector<int> graph[MAXN], grev[MAXN];
int visit[MAXN], vcnt;
int scc_idx[MAXN], scc_cnt;
int assignv[MAXN];
vector<int> emit;

void dfs(int nod, vector<int> graph[]) {
    visit[nod] = vcnt;
    for (int next : graph[nod]) {
        if (visit[next] == vcnt) continue;
        dfs(next, graph);
    }
    emit.push_back(nod);
}

// find SCCs in given graph
// O(V+E)
void get_scc() {
    scc_cnt = 0;
    vcnt = 1;
    emit.clear();
    memset(visit, 0, sizeof(visit));
	memset(assignv, -1, sizeof(assignv));

    for (int i = 0; i < vn; i++) {
        if (visit[i] == vcnt) continue;
        dfs(i, graph);
    }

    ++vcnt;
    for (auto st : vector<int>(emit.rbegin(), emit.rend())) {
        if (visit[st] == vcnt) continue;
        emit.clear();
        dfs(st, grev);
        ++scc_cnt;
        for (auto node : emit) {
            scc_idx[node] = scc_cnt;

			int isTrue = (node % 2);
			if (assignv[node / 2] != -1) continue;
			assignv[node / 2] = 1 - isTrue;
		}
    }
}

void proc(int caseidx) {
	scanf("%d %d", &n, &m);
	laser.clear();
	for (int i = 0; i < n; ++i) {
		scanf("%s", board[i]);
		for (int j = 0; j < m; ++j) {
			laserlist[i][j].clear();
			if (board[i][j] == '-' || board[i][j] == '|')
				laser.push_back({ i, j });
		}
	}
	targets[0].clear();
	targets[0].resize(laser.size());
	targets[1].clear();
	targets[1].resize(laser.size());

	bool fail = false;

	int idx = 0;
	for (const auto& ll : laser) {
		bool resa = true, resb = true;

		board[ll.first][ll.second] = '-';
		if (!laserCheck(ll.first, ll.second, false, targets[0][idx])) {
			resa = false;
		}
		board[ll.first][ll.second] = '|';
		if (!laserCheck(ll.first, ll.second, true, targets[1][idx])) {
			resb = false;
		}
		possible[idx][0] = possible[idx][1] = true;

		if (resa == false && resb == false) {
			fail = true;
			break;
		}
		if (resa == false) {
			possible[idx][0] = false;
		}
		if (resb == false) {
			possible[idx][1] = false;
		}

		++idx;
	}

	if (fail) {
		printf("Case #%d: ", caseidx);
		printf("IMPOSSIBLE\n");
		return;
	}

	for (int i = 0; i < laser.size(); ++i) {
		for (int v : targets[0][i]) {
			int ci = v / m, cj = v % m;
			laserlist[ci][cj].push_back({ i, 0 });
		}
		for (int v : targets[1][i]) {
			int ci = v / m, cj = v % m;
			laserlist[ci][cj].push_back({ i, 1 });
		}
	}

	vn = laser.size() * 2;
	for (int i = 0; i < vn; ++i) graph[i].clear();
	for (int i = 0; i < vn; ++i) grev[i].clear();

	for (int i = 0; i < laser.size(); ++i) {
		if (possible[i][0] == false) {
			graph[i * 2].push_back(i * 2 + 1);
			grev[i * 2 + 1].push_back(i * 2);
		}
		if (possible[i][1] == false) {
			graph[i * 2 + 1].push_back(i * 2);
			grev[i * 2].push_back(i * 2 + 1);
		}
	}

	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (board[i][j] != '.') continue;

			if (laserlist[i][j].size() == 0) fail = true;
			else if (laserlist[i][j].size() == 1) {
				int v0 = (laserlist[i][j][0].second == 0) ? laserlist[i][j][0].first * 2 : laserlist[i][j][0].first * 2 + 1;
				graph[v0 ^ 1].push_back(v0);
				grev[v0].push_back(v0 ^ 1);
			}
			else {
				int v0 = (laserlist[i][j][0].second == 0) ? laserlist[i][j][0].first * 2 : laserlist[i][j][0].first * 2 + 1;
				int v1 = (laserlist[i][j][1].second == 0) ? laserlist[i][j][1].first * 2 : laserlist[i][j][1].first * 2 + 1;

				graph[v0 ^ 1].push_back(v1);
				grev[v1].push_back(v0 ^ 1);
				graph[v1 ^ 1].push_back(v0);
				grev[v0].push_back(v1 ^ 1);
			}
		}
	}

	get_scc();
	for (int i = 0; i < vn / 2; ++i) {
		if (scc_idx[i] == scc_idx[i + 1]) {
			fail = true;
			break;
		}
	}

	for (int i = 0; i < laser.size(); ++i) {
		if (assignv[i]) {
			board[laser[i].first][laser[i].second] = '|';
		}
		else {
			board[laser[i].first][laser[i].second] = '-';
		}
	}

	if (fail) {
		printf("Case #%d: ", caseidx);
		printf("IMPOSSIBLE\n");
		return;
	}

	printf("Case #%d: ", caseidx);
	printf("POSSIBLE\n");
	for (int i = 0; i < n; ++i) {
		printf("%s\n", board[i]);
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		proc(i);
	}
	return 0;
}