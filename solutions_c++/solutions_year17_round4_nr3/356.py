//Template
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <climits>
#include <cmath>
#include <utility>
#include <set>
// #include <map>
#include <queue>
#include <ios>
#include <iomanip>
#include <ctime>
#include <numeric>
#include <functional>
#include <fstream>
#include <string>
#include <vector>
#include <bitset>
#include <cstdarg>
#include <complex>
using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;
#define pair(x, y) make_pair(x, y)
#define runtime() ((double)clock() / CLOCKS_PER_SEC)

inline int read() {
	static int r, sign;
	static char c;
	r = 0, sign = 1;
	do c = getchar(); while (c != '-' && (c < '0' || c > '9'));
	if (c == '-') sign = -1, c = getchar();
	while (c >= '0' && c <= '9') r = r * 10 + (int)(c - '0'), c = getchar();
	return sign * r;
}

template <typename T>
inline void print(T *a, int n) {
	for (int i = 1; i < n; ++i) cout << a[i] << " ";
	cout << a[n] << endl;
}
#define PRINT(_l, _r, _s, _t) { cout << #_l #_s "~" #_t #_r ": "; for (int _i = _s; _i != _t; ++_i) cout << _l _i _r << " "; cout << endl; }

#define M 50
#define N 100
int T, Case = 0;
int r, c;
char map[M + 10][M + 10];
bool vertical[N + 1], horizon[N + 1];
bool v[M + 1][M + 1][4];
vector<pair<int, int>> beam;
vector<pair<int, int>> empty, vert_empty[N + 1], hor_empty[N + 1];
vector<int> empty_beam[M + 1][M + 1];
int cur = 0, direction[N + 1];

// DIR: UP, RIGHT, DOWN, LEFT
const int delta[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

bool find_beam(int x, int y, int dir) {
	x += delta[dir][0], y += delta[dir][1];
	if (x < 1 || x > r || y < 1 || y > c) return false;
	if (map[x][y] == '-' || map[x][y] == '|') return true;
	if (map[x][y] == '#') return false;
	if (map[x][y] == '/') {
		int nd = dir ^ 1;
		return find_beam(x, y, nd);
	}
	if (map[x][y] == '\\') {
		int nd = 3 - dir;
		return find_beam(x, y, nd);
	}
	if (map[x][y] == '.') {
		empty.emplace_back(x, y);
		empty_beam[x][y].push_back(cur);
	}
	if (v[x][y][dir]) return false;
	v[x][y][dir] = true;
	return find_beam(x, y, dir);
}

bool cover[M + 1][M + 1], init_cover[M + 1][M + 1];

bool dfs(int x) {
	if (x >= beam.size()) {
		memcpy(cover, init_cover, sizeof init_cover);
		for (int i = 0; i < beam.size(); ++i)
			if (vertical[i] && horizon[i]) {
				if (direction[i] == 1) {
					for (auto p : hor_empty[i])
						cover[p.first][p.second] = true;
				} else {
					for (auto p :  vert_empty[i])
						cover[p.first][p.second] = true;
				}
			}
		for (int i = 1; i <= r; ++i)
			for (int j = 1; j <= c; ++j)
				if (map[i][j] == '.' && !cover[i][j])
					return false;
		return true;
	}
	if (vertical[x] && horizon[x]) {
		direction[x] = 1;
		if (dfs(x + 1)) return true;
		direction[x] = -1;
		if (dfs(x + 1)) return true;
		return false;
	} else return dfs(x + 1);
}

int main(int argc, char *argv[]) {
#ifdef KANARI
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	
	cin >> T;
	while (T--) {
		beam.clear();
		cin >> r >> c;
		for (int i = 1; i <= r; ++i)
			cin >> (map[i] + 1);
		for (int i = 1; i <= r; ++i)
			for (int j = 1; j <= c; ++j) {
				if (map[i][j] == '-' || map[i][j] == '|')
					beam.emplace_back(i, j);
				empty_beam[i][j].clear();
			}

		for (int i = 0; i < beam.size(); ++i) {
			int x, y;
			tie(x, y) = beam[i];
			
			cur = i * 2;
			memset(v, 0, sizeof v);
			empty.clear();
			vertical[i] = !(find_beam(x, y, 0) | find_beam(x, y, 2));
			vert_empty[i] = empty;
			
			cur = i * 2 + 1;
			memset(v, 0, sizeof v);
			empty.clear();
			horizon[i] = !(find_beam(x, y, 1) | find_beam(x, y, 3));
			hor_empty[i] = empty;
		}

		bool valid = true;
		memset(init_cover, 0, sizeof init_cover);
		for (int i = 0; i < beam.size(); ++i) {
			if (!vertical[i] && horizon[i]) {
				direction[i] = 1;
				for (auto p : hor_empty[i])
					init_cover[p.first][p.second] = true;
			} else if (vertical[i] && !horizon[i]) {
				direction[i] = -1;
				for (auto p : vert_empty[i])
					init_cover[p.first][p.second] = true;
			} else if (!vertical[i] && !horizon[i]) {
				valid = false;
			}
		}
		for (int i = 1; i <= r; ++i)
			for (int j = 1; j <= c; ++j) {
				if (map[i][j] != '.') continue;
				if (empty_beam[i][j].size() == 1) {
					int cur = empty_beam[i][j][0];
					direction[cur >> 1] = (cur & 1) * 2 - 1;
				} else if (empty_beam[i][j].size() == 0) {
					valid = false;
				}
			}


		cout << "Case #" << ++Case << ": ";
		if (valid) valid = dfs(0);
		if (valid) {
			cout << "POSSIBLE" << endl;
			for (int i = 0; i < beam.size(); ++i) {
				int x, y;
				tie(x, y) = beam[i];
				if (direction[i] == 1) map[x][y] = '-';
				else if (direction[i] == -1) map[x][y] = '|';
			}
			for (int i = 1; i <= r; ++i) {
				for (int j = 1; j <= c; ++j)
					cout << map[i][j];
				cout << endl;
			}
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
