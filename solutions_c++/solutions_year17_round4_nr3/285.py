#include <bits/stdc++.h>
using namespace std;
using namespace chrono;

const int dx[] = {0, -1, 0, 1};
const int dy[] = {1, 0, -1, 0};

vector<pair<int, int> > ch[2600][2];
char buf[52][52];
int id[52][52];
int ans[2600];
int r, c, __;

pair<int, int> sim(int x, int y, int d)
{
	if (x < 0 || x >= r || y < 0 || y >= c || buf[x][y] == '#') return make_pair(-1, -1);
	if (buf[x][y] == '-' || buf[x][y] == '|') return make_pair(id[x][y], d&1);
	if (buf[x][y] == '/') d ^= 1;
	if (buf[x][y] == '\\') d ^= 3;
	return sim(x+dx[d], y+dy[d], d);
}

bool dfs(int at, int va)
{
	if (ans[at] != -1) return ans[at]==va;
	ans[at] = va;
	for (auto u: ch[at][va]) if (!dfs(u.first, u.second)) return false;
	return true;
}

bool twosat()
{
	for (int i = 0;i < __;i++) if (ans[i] != -1) dfs(i, ans[i]);
	for (int i = 0;i < __;i++) if (ans[i] == -1)
	{
		if (dfs(i, 0)) continue;
		return false;
	}
	return true;
}

void solve()
{
	__ = 0;
	scanf("%d%d", &r, &c);
	for (int i = 0;i < r;i++) scanf("%s", buf[i]);
	for (int i = 0;i < r;i++) for (int j = 0;j < c;j++) if (buf[i][j] == '-' || buf[i][j] == '|')
		id[i][j] = __++;
	for (int i = 0;i < __;i++) ans[i] = -1, ch[i][0].clear(), ch[i][1].clear();
	for (int i = 0;i < r;i++) for (int j = 0;j < c;j++) if (buf[i][j] != '#' && buf[i][j] != '-' && buf[i][j] != '|')
	{
		vector<pair<int, int> > can;
		if (buf[i][j] == '.')
		{
			auto a = sim(i, j, 1), b = sim(i, j, 3);
			if (min(a.first, b.first) == -1 && max(a.first, b.first) != -1) can.push_back(max(a, b));
			a = sim(i, j, 2), b = sim(i, j, 0);
			if (min(a.first, b.first) == -1 && max(a.first, b.first) != -1) can.push_back(max(a, b));
		} else if (buf[i][j] == '/')
		{
			auto a = sim(i, j, 0), b = sim(i, j, 3);
			if (min(a.first, b.first) == -1 && max(a.first, b.first) != -1) can.push_back(max(a, b));
			a = sim(i, j, 2), b = sim(i, j, 1);
			if (min(a.first, b.first) == -1 && max(a.first, b.first) != -1) can.push_back(max(a, b));
		} else if (buf[i][j] == '\\')
		{
			auto a = sim(i, j, 1), b = sim(i, j, 2);
			if (min(a.first, b.first) == -1 && max(a.first, b.first) != -1) can.push_back(max(a, b));
			a = sim(i, j, 3), b = sim(i, j, 0);
			if (min(a.first, b.first) == -1 && max(a.first, b.first) != -1) can.push_back(max(a, b));
		}
		if (can.empty())
		{
			printf("IMPOSSIBLE\n");
			return;
		}
		if (can.size() == 1)
		{
			if (ans[can[0].first] == -1) ans[can[0].first] = can[0].second;
			else if (ans[can[0].first] != can[0].second)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		} else
		{
			ch[can[0].first][!can[0].second].emplace_back(can[1].first, can[1].second);
			ch[can[1].first][!can[1].second].emplace_back(can[0].first, can[0].second);
		}
	} else if (buf[i][j] == '-' || buf[i][j] == '|')
	{
		int can = 0;
		auto a = sim(i+dx[1], j+dy[1], 1), b = sim(i+dx[3], j+dy[3], 3);
		if (max(a, b).first == -1) can |= 2;
		a = sim(i+dx[2], j+dy[2], 2), b = sim(i+dx[0], j+dy[0], 0);
		if (max(a, b).first == -1) can |= 1;
		if (can == 0)
		{
			printf("IMPOSSIBLE\n");
			return;
		}
		if (can != 3)
		{
			if (ans[id[i][j]] == -1) ans[id[i][j]] = can - 1;
			else if (ans[id[i][j]] != can-1)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
		}
	}
	if (!twosat())
	{
		printf("IMPOSSIBLE\n");
		return;
	}
	printf("POSSIBLE\n");
	for (int i = 0;i < r;i++) for (int j = 0;j < c;j++) if (buf[i][j] == '-' || buf[i][j] == '|')
	{
		buf[i][j] = ans[id[i][j]]?'|':'-';
	}
	for (int i = 0;i < r;i++) printf("%s\n", buf[i]);
}

int main()
{
	int t; scanf("%d", &t);
	for (int _ = 1;_ <= t;_++)
	{
		fprintf(stderr, "\tCase #% 3d...", _); fflush(stdout);
		milliseconds start_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());

		printf("Case #%d: ", _); solve();

		milliseconds end_ti = duration_cast<milliseconds>(system_clock::now().time_since_epoch());
		long long time_used = end_ti.count() - start_ti.count();
		fprintf(stderr, " done\t% 6lldms\n", time_used); fflush(stdout);
	}
	fprintf(stderr, "\n\n\n");
	return 0;
}
