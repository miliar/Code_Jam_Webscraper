#include "assert.h"
#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <time.h>
#include <vector>

using namespace std;

#if LOCAL
	#define DO_NOT_SEND
#endif

typedef long long LL;

int IntMaxVal = (int) 1e20;
int IntMinVal = (int) -1e20;
LL LongMaxVal = (LL) 1e20;
LL LongMinVal = (LL) -1e20;

#define FOR(i, a, b) for(int i = a; i < b ; ++i)
#define FORD(i, a, b) for(int i = a; i >= b; --i)

template<typename T> inline void minimize(T &a, T b) { a = std::min(a, b); }
template<typename T> inline void maximize(T &a, T b) { a = std::max(a, b); }

template<typename T> inline void swap(pair<T, T> &p) { swap(p.first , p.second ); }

#define all(v) v.begin(),v.end()

#define endl '\n'
template<typename T> struct argument_type;
template<typename T, typename U> struct argument_type<T(U)> { typedef U type; };
#define next(t, i) argument_type<void(t)>::type i; cin >> i;

template <typename T1, typename T2> istream& operator >>(istream& is, pair<T1, T2>& s) { is >> s.first >> s.second; return is; }
template <typename T> ostream& operator << (ostream& os, const vector<T> &v) { for (int i = 0 ; i < v.size() ; i++) { if (i) os << ' '; os << v[i]; } os << endl; return os; }
template <typename T1, typename T2> ostream& operator << (ostream& os, const vector<pair<T1, T2>> &v) { for (int i = 0 ; i < v.size() ; i++) { os << v[i] << endl; } return os; }
template <typename T1, typename T2> ostream& operator <<(ostream& s, const pair<T1, T2>& t) { s << t.first << ' ' << t.second; return s; }
template <typename T> vector<T> readVector(int n) { vector<T> res(n); for (int i = 0 ; i < n ; i++) cin >> res[i]; return res; }

void assert2(bool x) {
	if (!x) exit(0);
}

const string possible = "POSSIBLE";
const string impossible = "IMPOSSIBLE";

const int TRUE = 1;
const int FALSE = 0;
const int UNKNOWN = -1;

const int UP = 0;
const int LEFT = 1;
const int RIGHT = 2;
const int DOWN = 3;

struct condition {
	int type;
	vector<int> operands;
};

pair<char, pair<int, int>> findLastCell(vector<string> &f, int y, int x, int dir) {
	int y2 = y;
	int x2 = x;
	if (dir == UP) y2--;
	if (dir == DOWN) y2++;
	if (dir == LEFT) x2--;
	if (dir == RIGHT) x2++;

	if (y2 < 0 || x2 < 0 || y2 == f.size() || x2 == f[0].size() || f[y2][x2] == '#') return {'#', { 0, 0}};
	if (f[y2][x2] == '.') return findLastCell(f, y2, x2, dir);
	if (f[y2][x2] == '/') {
		if (dir == LEFT) return findLastCell(f, y2, x2, DOWN);
		if (dir == RIGHT) return findLastCell(f, y2, x2, UP);
		if (dir == DOWN) return findLastCell(f, y2, x2, LEFT);
		if (dir == UP) return findLastCell(f, y2, x2, RIGHT);
	}
	if (f[y2][x2] == '\\') {
		if (dir == LEFT) return findLastCell(f, y2, x2, UP);
		if (dir == RIGHT) return findLastCell(f, y2, x2, DOWN);
		if (dir == DOWN) return findLastCell(f, y2, x2, RIGHT);
		if (dir == UP) return findLastCell(f, y2, x2, LEFT);
	}
	if (f[y2][x2] == '|' || f[y2][x2] == '-') {
		if (dir == LEFT || dir == RIGHT) return { '-', { y2 , x2 }};
		else return { '|', {y2, x2 }};
	}
	assert2(false);
}

int get_position(vector<vector<int>> &turret_ids, pair<char, pair<int, int>> pos) {
	int y = pos.second.first;
	int x = pos.second.second;
	int id = turret_ids[y][x];
	return id * 2 + (pos.first == '|' ? 1 : 0);
}

pair<string, vector<string>> solve() {
	next(int, r);
	next(int, c);

	auto f = readVector<string>(r);
	vector<vector<bool>> is_fixed(r, vector<bool>(c));

	vector<pair<int, int>> positions;
	vector<vector<int>> conditions;

	int next_turret_id = 0;
	vector<pair<int, int>> turret_positions;
	vector<vector<int>> turret_ids(r, vector<int>(c, -1));

	FOR (y, 0, r) FOR (x, 0, c) {
		if (f[y][x] == '|' || f[y][x] == '-') {
			turret_positions.push_back({ y , x });
			turret_ids[y][x] = next_turret_id;
			next_turret_id++;
		}
	}

	FOR (y, 0, r) FOR (x, 0, c) {
		if (f[y][x] == '.' || f[y][x] == '|' || f[y][x] == '-') {
			auto lcUp = findLastCell(f, y, x, UP);
			auto lcDown = findLastCell(f, y, x, DOWN);
			auto lcRight = findLastCell(f, y, x, RIGHT);
			auto lcLeft = findLastCell(f, y, x, LEFT);

			if (f[y][x] == '.') {
				vector<int> cannon_position_options;

				if (lcUp.first != '#') cannon_position_options.push_back(get_position(turret_ids, lcUp));
				if (lcDown.first != '#') cannon_position_options.push_back(get_position(turret_ids, lcDown));
				if (lcLeft.first != '#') cannon_position_options.push_back(get_position(turret_ids, lcLeft));
				if (lcRight.first != '#') cannon_position_options.push_back(get_position(turret_ids, lcRight));

				conditions.push_back(cannon_position_options);
			} else {
				if (lcUp.first != '#') conditions.push_back( { get_position(turret_ids, lcUp) ^ 1 } );
				if (lcDown.first != '#') conditions.push_back( { get_position(turret_ids, lcDown) ^ 1 } );
				if (lcLeft.first != '#') conditions.push_back( { get_position(turret_ids, lcLeft) ^ 1 } );
				if (lcRight.first != '#') conditions.push_back( { get_position(turret_ids, lcRight) ^ 1 } );
			}
		}
	}

	vector<int> values(next_turret_id * 2, UNKNOWN);

	while (true){ 




	bool needs_checking = true;
	while (needs_checking) {
		needs_checking = false;

		FOR (i, 0, conditions.size()) {
			bool is_true = false;
			for (auto m : conditions[i]) if (values[m] == TRUE) is_true = true;

			if (is_true) {
				swap(conditions[i], conditions.back());
				conditions.pop_back();
				i--;
				continue;
			}

			FOR (j, 0, conditions[i].size()) if (values[conditions[i][j]] == FALSE) {
				conditions[i].erase(conditions[i].begin() + j);
				j--;
			}

			if (conditions[i].size() == 0) return { impossible, { }};

			if (conditions[i].size() == 1) {
				int val = conditions[i][0];
				values[val] = TRUE;
				values[val ^ 1] = FALSE;
				needs_checking = true;
			}
		}
	}


	int index_to_set = -1;
	FOR (i, 0, values.size()) if (values[i] == UNKNOWN) index_to_set = i;

	if (index_to_set == -1) break;
	else {
		values[index_to_set] = TRUE;
		values[index_to_set ^ 1] = FALSE;
	}
	}

	FOR (i,0 , next_turret_id) {
		int y = turret_positions[i].first;
		int x = turret_positions[i].second;

		f[y][x] = values[i * 2] == TRUE ? '-' : '|';
	}

	return { possible, f };
}

int main() {
	srand (time(NULL));
	ios_base::sync_with_stdio(false); cin.tie(NULL);
	fixed(cout); cout << setprecision(10);
	
	next(int, n);
	FOR (i, 0, n) {
		cout << "Case #" << (i + 1) << ": ";
		auto res = 
			solve();
		// if (res == -1) cout << "IMPOSSIBLE" << endl;
		// else 
			// cout << res << endl;
		// cout << endl;

		cout << res.first << endl;
		if (res.first == "POSSIBLE") {
			for (auto &s : res.second) cout << s << endl;
		}
	}

	// cerr << "Done" << endl;
}