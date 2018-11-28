#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <list>
#include <time.h>
#include <algorithm>
#include <math.h>
typedef long long ll;
typedef long double ld;
using namespace std;

const int SZ = 1e3 + 10;
const int INF = 1e9;

string f[SZ];
vector<pair<int, int> > v;
int mkd[SZ], tmkd[SZ], pa[SZ];
vector<int> cell[SZ][SZ], dir[SZ];
pair<pair<int, int>, char> id[SZ];
bool ac[SZ];

bool dfs(int x, int y, char dir) {
	if (f[x][y] == '|' || f[x][y] == '-')
		return false;
	if (f[x][y] == '#')
		return true;
	if (f[x][y] == '.') {
		v.push_back(make_pair(x, y));
		if (dir == 'U')
			return dfs(x - 1, y, dir);
		if (dir == 'D')
			return dfs(x + 1, y, dir);
		if (dir == 'L')
			return dfs(x, y - 1, dir);
		if (dir == 'R')
			return dfs(x, y + 1, dir);
	}
	if (f[x][y] == '/') {
		if (dir == 'U')
			return dfs(x, y + 1, 'R');
		if (dir == 'D')
			return dfs(x, y - 1, 'L');
		if (dir == 'L')
			return dfs(x + 1, y, 'D');
		if (dir == 'R')
			return dfs(x - 1, y, 'U');
	} else {
		if (dir == 'U')
			return dfs(x, y - 1, 'L');
		if (dir == 'D')
			return dfs(x, y + 1, 'R');
		if (dir == 'L')
			return dfs(x - 1, y, 'U');
		if (dir == 'R')
			return dfs(x + 1, y, 'D');
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(false);

	int t;
	cin >> t;
	
	for (int testno = 1; testno <= t; testno++) {
		int n, m;
		cin >> n >> m;
		for (int i = 1; i <= n; i++) {
			cin >> f[i];
			f[i] = '#' + f[i] + '#';
		}
		f[0] = f[n + 1] = "";
		for (int i = 0; i < m + 2; i++) {
			f[0] += '#';
			f[n + 1] += '#';
		}

		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				cell[i][j].clear();

		int ids = 0;
		bool ok = true;

		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				if (f[i][j] == '|' || f[i][j] == '-') {
					pa[ids] = ids + 1;
					pa[ids + 1] = ids;
					bool lok = false;

					id[ids] = make_pair(make_pair(i, j), '|');
					v.clear();
					if (dfs(i - 1, j, 'U') && dfs(i + 1, j, 'D')) {
						ac[ids] = true;
						lok = true;
						for (auto k : v)
							cell[k.first][k.second].push_back(ids);
					} else
						ac[ids] = false;
					ids++;

					id[ids] = make_pair(make_pair(i, j), '-');
					v.clear();
					if (dfs(i, j - 1, 'L') && dfs(i, j + 1, 'R')) {
						ac[ids] = true;
						lok = true;
						for (auto k : v)
							cell[k.first][k.second].push_back(ids);
					} else
						ac[ids] = false;
					ids++;

					if (!lok)
						ok = false;
				}

		for (int i = 0; i < ids; i++) {
			dir[i].clear();
			mkd[i] = 0;
		}

		vector<int> musthave, cancel;

		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++)
				if (f[i][j] == '.') {
					if (!cell[i][j].size())
						ok = false;
					if (cell[i][j].size() == 1) {
						musthave.push_back(cell[i][j][0]);
						mkd[cell[i][j][0]] = 1;
					}
					if (cell[i][j].size() == 2) {
						dir[cell[i][j][0]].push_back(cell[i][j][1]);
						dir[cell[i][j][1]].push_back(cell[i][j][0]);
					}
				}

		while (musthave.size() || cancel.size()) {
			for (int i : musthave)
				if (mkd[pa[i]] == 0) {
					cancel.push_back(pa[i]);
					mkd[pa[i]] = 2;
				}
				else if (mkd[pa[i]] == 1)
					ok = false;
			musthave.clear();

			for (int i : cancel)
				for (int j : dir[i])
					if (mkd[j] == 0) {
						musthave.push_back(j);
						mkd[j] = 1;
					}
					else if (mkd[j] == 2)
						ok = false;
			cancel.clear();
		}

		for (int i = 0; i < ids; i++)
			if (!mkd[i]) {
				for (int j = 0; j < ids; j++)
					tmkd[j] = 0;

				bool succ = ac[i];

				musthave.push_back(i);
				tmkd[i] = 1;
				while (musthave.size() || cancel.size()) {
					for (int i : musthave)
						if (!tmkd[pa[i]]) {
							cancel.push_back(pa[i]);
							tmkd[pa[i]] = 2;
						}
					else if (tmkd[pa[i]] == 1)
						succ = false;
					musthave.clear();

					for (int i : cancel)
						for (int j : dir[i])
							if (tmkd[j] == 0) {
								musthave.push_back(j);
								tmkd[j] = 1;
							}
							else if (tmkd[j] == 2)
								succ = false;
					cancel.clear();
				}

				if (succ) {
					for (int j = 0; j < ids; j++)
						if (tmkd[j])
							mkd[j] = tmkd[j];
					continue;
				}
			}
			
		for (int i = 0; i < ids; i++)
			if ((mkd[i] == 1 && !ac[i]) || mkd[i] == 0)
				ok = false;

		for (int i = 0; i < ids; i++)
			if (mkd[i] == 1)
				f[id[i].first.first][id[i].first.second] = id[i].second;

		if (!ok) {
			cout << "Case #" << testno << ": " << "IMPOSSIBLE\n";
			continue;
		}

		cout << "Case #" << testno << ": " << "POSSIBLE\n";
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= m; j++)
				cout << f[i][j];
			cout << "\n";
		}
	}

	return 0;
}
