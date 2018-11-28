#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int D = 4;
const int DIR[D][2] = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
const int N = 110;

const char HOR = '-';
const char VER = '|';
const char WALL = '#';
const char SPACE = '.';

typedef pair<int, int> pii;
typedef vector<pii> vpii;

vpii ver[N*N], hor[N*N];

vector<int> data[N][N];
string grid[N];
int n, m;

ostream& operator<<(ostream& out, pii x) {
	return out << "[" << x.first << " " << x.second << "]";
}
template<class T>
ostream& operator<<(ostream& out, vector<T> vec) {
	for (const T val : vec) { 
		out << val << " ";
	}
	return out;
}

vpii dfs(int i, int j, int d1, int d2) {
	if (d2 == -1 and (grid[i][j] == HOR or grid[i][j] == VER)) return {};

	vpii result = {{i, j}};
	for (int x = 0; x < D; ++x) {
		if (x == d1 or x == d2) {
			int ni = i + DIR[x][0], nj = j + DIR[x][1];
			if (ni < 0 or nj < 0 or ni >= n or nj >= m) continue;
			if (grid[ni][nj] == WALL) continue;
			int nx = x;
			if (grid[ni][nj] == '/') {
				if (nx == 0) nx = 3;
				else if (nx == 1) nx = 2;
				else if (nx == 2) nx = 1;
				else if (nx == 3) nx = 0;
			} else if (grid[ni][nj] == '\\') {
				if (nx == 0) nx = 1;
				else if (nx == 1) nx = 0;
				else if (nx == 2) nx = 3;
				else if (nx == 3) nx = 2;
			}
			auto res = dfs(ni, nj, nx, -1);
			if (res.empty()) return {};
			result.insert(result.end(), res.begin(), res.end());
		}
	}

	return result;
}

int found[N][N];

bool dfs(void) {
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < m; ++j) {
			if (found[i][j] > 0 or grid[i][j] == WALL) continue;
			for (int val : data[i][j]) {
				auto &s = (val < 0 ? hor[-val] : ver[val]);
				int x = s[0].first, y = s[0].second;
				if (found[x][y] > 0) continue;
				grid[x][y] = (val < 0 ? HOR : VER);
				for (auto k : s) {
					found[k.first][k.second]++;
				}
				if (dfs()) return true;
				for (auto k : s) {
					found[k.first][k.second]--;
				}
			}
			return false;
		}
	}

	return true;
}

int main(void) {

	int test;
	cin >> test;

	for (int Case = 1; Case <= test; ++Case) {

		cin >> n >> m;
		for (int i = 0; i < n; ++i) {
			cin >> grid[i];
		}

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				data[i][j].clear();
				found[i][j] = 0;
			}
		}

		int cnt = 1;

		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (grid[i][j] == HOR or grid[i][j] == VER) {
					auto hor1 = dfs(i, j, 0, 2);
					auto ver1 = dfs(i, j, 1, 3);

					ver[cnt] = ver1;
					hor[cnt] = hor1;

					for (auto x : hor1) {
						data[x.first][x.second].push_back(-cnt);
					}
					for (auto x : ver1) {
						data[x.first][x.second].push_back(cnt);
					}
					// cerr << cnt << " | " << hor1 << " " << ver1 << endl;
					++cnt;
				}
			}
		}

		bool err = false;
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < m; ++j) {
				if (grid[i][j] == SPACE) {
					if (data[i][j].empty()) {
						err = true;
					}
				}
			}
		}

		if (!err) {
			err |= !dfs();
		}

		cout << "Case #" << Case << ": ";
		if (err) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << "POSSIBLE" << endl;
			for (int i = 0; i < n; ++i) {
				cout << grid[i] << endl;
			}
		}

		cerr << Case << endl;
	}


	return 0;	
}