#include<stdio.h>
#include<vector>
#include<deque>
using namespace std;

int n, m;
bool rook[100][100] = { 0 };
bool rook_row[100] = { 0 }, rook_column[100] = { 0 };
bool bishop[100][100] = { 0 };
bool bishop_1[210] = { 0 }, bishop_2[210] = { 0 };
bool changed[100][100] = { 0 };

void rook_assignment(int row) {
	if (row == n + 1) return;
	if (rook_row[row]) rook_assignment(row + 1);
	for (int i = 0; i < n; i++) {
		if (!rook_column[i]) {
			rook_column[i] = true;
			rook[row][i] = true;
			changed[row][i] = true;
			rook_assignment(row + 1);
			return;
		}
	}
}

vector< pair<int, int> > edge[500];
vector< pair<int, int> > backedge[500];
int num[500] = { 0 };
bool check[500] = { 0 };
bool bfs() {
	deque<int> dq;
	dq.push_back(0);
	for (int i = 0; i < 4 * n; i++) num[i] = check[i] = 0;
	check[0] = true;
	while (!dq.empty()) {
		int now = dq.front();
		dq.pop_front();
		for (int i = 0; i < edge[now].size(); i++) {
			if (edge[now][i].second != 0 && !check[edge[now][i].first]) {
				num[edge[now][i].first] = num[now] + 1;
				check[edge[now][i].first] = true;
				dq.push_back(edge[now][i].first);
			}
		}
	}
	return check[4 * n - 1];
}
bool dfs(int idx) {
	if (idx == 4 * n - 1) return true;
	check[idx] = true;
	for (int i = 0; i < edge[idx].size(); i++) {
		if (edge[idx][i].second != 0 && !check[edge[idx][i].first] && num[idx] < num[edge[idx][i].first]) {
			if (dfs(edge[idx][i].first)) {
				edge[idx][i].second = 0;
				edge[backedge[idx][i].first][backedge[idx][i].second].second++;
				return true;
			}
		}
	}
	check[idx] = false;
	return false;
}

void bishop_assignment() {
	int i, j;
	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			if (bishop[i][j]) continue;
			backedge[i + j + 1].push_back(make_pair(i - j + 3 * n - 1, edge[i - j + 3 * n - 1].size()));
			backedge[i - j + 3 * n - 1].push_back(make_pair(i + j + 1, edge[i + j + 1].size()));
			edge[i + j + 1].push_back(make_pair(i - j + 3 * n - 1, 1));
			edge[i - j + 3 * n - 1].push_back(make_pair(i + j + 1, 0));
		}
	}
	for (i = 0; i < 2 * n - 1; i++) {
		if (!bishop_1[i]) {
			backedge[0].push_back(make_pair(i + 1, edge[i + 1].size()));
			backedge[i + 1].push_back(make_pair(0, edge[0].size()));
			edge[0].push_back(make_pair(i + 1, 1));
			edge[i + 1].push_back(make_pair(0, 0));
		}
		if (!bishop_2[i]) {
			backedge[i + 2 * n].push_back(make_pair(4 * n - 1, edge[4 * n - 1].size()));
			backedge[4 * n - 1].push_back(make_pair(i + 2 * n, edge[i + 2 * n].size()));
			edge[i + 2 * n].push_back(make_pair(4 * n - 1, 1));
			edge[4 * n - 1].push_back(make_pair(i + 2 * n, 0));
		}
	}

	while (bfs()) {
		for (i = 0; i < 4 * n; i++) check[i] = false;
		while (dfs(0)) {
			for (i = 0; i < 4 * n; i++) check[i] = false;
		}
	}

	for (i = 1; i < 2*n; i++) {
		for (j = 0; j < edge[i].size(); j++) {
			if (edge[i][j].first < 2 * n) continue;
			if (edge[i][j].second == 1) continue;
			int r = (i + edge[i][j].first - 3 * n) / 2, c = (i - edge[i][j].first + 3 * n - 2) / 2;
			if (!bishop[r][c]) {
				bishop[r][c] = true;
				changed[r][c] = true;
			}
		}
	}
}
int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	int t, test;
	vector< pair<int, pair<int, int> > > ans;
	scanf("%d", &test);
	for (t = 1; t <= test; t++) {
		int i, j;
		scanf("%d%d", &n, &m);
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				rook[i][j] = false;
				bishop[i][j] = false;
				changed[i][j] = false;
			}
			rook_column[i] = rook_row[i] = false;
		}
		for (i = 0; i < 2 * n + 1; i++)
			bishop_1[i] = bishop_2[i] = false;
		for (i = 0; i < m; i++) {
			char s[2] = { 0 };
			int a, b;
			scanf("%s %d %d", s, &a, &b);
			if (s[0] == '+') {
				bishop[a - 1][b - 1] = true;
				bishop_1[a + b - 2] = bishop_2[a - b + n - 1] = true;
			}
			else if (s[0] == 'x') {
				rook[a - 1][b - 1] = true;
				rook_row[a - 1] = rook_column[b - 1] = true;
			}
			else if (s[0] == 'o') {
				bishop[a - 1][b - 1] = true;
				bishop_1[a + b - 2] = bishop_2[a - b + n - 1] = true;
				rook[a - 1][b - 1] = true;
				rook_row[a - 1] = rook_column[b - 1] = true;
			}
		}
		rook_assignment(0);
		for (i = 0; i < 4*n; i++) {
			edge[i].clear();
			backedge[i].clear();
		}
		bishop_assignment();

		int point = 0;
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				if (bishop[i][j]) point++;
				if (rook[i][j]) point++;

				if (!changed[i][j]) continue;

				if (bishop[i][j] && rook[i][j])
					ans.push_back(make_pair(2, make_pair(i + 1, j + 1)));
				else if(bishop[i][j])
					ans.push_back(make_pair(1, make_pair(i + 1, j + 1)));
				else
					ans.push_back(make_pair(0, make_pair(i + 1, j + 1)));
			}
		}
		printf("Case #%d: %d %d\n", t, point, ans.size());
		for (i = 0; i < ans.size(); i++) {
			if (ans[i].first == 0) printf("x ");
			else if (ans[i].first == 1) printf("+ ");
			else printf("o ");
			printf("%d %d\n", ans[i].second.first, ans[i].second.second);
		}
		ans.clear();
	}
	return 0;
}