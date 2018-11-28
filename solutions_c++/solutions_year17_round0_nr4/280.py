// problemD.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

struct Position {
	int x;
	int y;

	Position() : x(0), y(0) {}
	Position(int x, int y) : x(x), y(y) {}
};

struct PositionWithChar : public Position {
	char ch;

	PositionWithChar() : ch( 0 ) {}
	PositionWithChar(Position pos, char ch) : Position(pos), ch(ch) {}
};

bool try_kuhn(vector<bool>& used, vector<int> & mt, vector < vector<int> >& g, int v) {
	if (used[v]) return false;
	used[v] = true;
	for (size_t i = 0; i < g[v].size(); ++i) {
		int to = g[v][i];
		if (mt[to] == -1 || try_kuhn(used, mt, g, mt[to])) {
			mt[to] = v;
			return true;
		}
	}
	return false;
}

void solve( int n, const vector<bool>& plusDiagonals, const vector<bool>& minusDiagonals, vector<Position>& plusAddon) {
	const int k = 2 * n - 1;
	vector< vector<int> > g;
	vector<int> mt;
	vector<bool> used;

	for (int i = 0; i < k; i++) {
		g.push_back(vector<int>());
	}
	for (int x = 0; x < n; x++) {
		for (int y = 0; y < n; y++) {
			const int plus = x + y;
			const int minus = x - y + n - 1;
			if(!plusDiagonals[plus] && !minusDiagonals[minus]) {
				g[plus].push_back(minus);
			}
		}
	}
	mt.assign(k, -1);
	for (int v = 0; v < k ; v++ ) {
		used.assign(k, false);
		try_kuhn(used, mt, g, v);
	}

	for (int minus = 0; minus < k; minus++) {
		if (mt[minus] == -1) {
			continue;
		}
		const int plus = mt[minus];
		const int x = (minus + plus - n + 1) / 2;
		const int y = plus - x;
		plusAddon.push_back(Position(x, y));
	}
}

void main() {
	int t = 0;
	cin >> t;
	for (int i = 1; i <= t; ++i) {
		int n;
		int k;
		cin >> n >> k;
		vector<bool> rows;
		vector<bool> columns;
		vector<bool> plusDiagonals;
		vector<bool> minusDiagonals;
		vector<bool> crossPositions;
		vector<bool> plusPositions;
		vector<Position> plusAddon;
		vector<Position> crossAddon;
		rows.insert(rows.begin(), n, false);
		columns.insert(columns.begin(), n, false);
		plusDiagonals.insert(plusDiagonals.begin(), 2 * n + 1, false);
		minusDiagonals.insert(minusDiagonals.begin(), 2 * n + 1, false);
		crossPositions.insert(crossPositions.begin(), n * n, false);
		plusPositions.insert(plusPositions.begin(), n * n, false);
		int result = 0;
		for (int c = 0; c < k; c++) {
			char ch = 0;
			int x = 0;
			int y = 0;
			cin >> ch >> x >> y;
			x--;
			y--;
			if (ch != 'x') {
				plusDiagonals[x + y] = true;
				minusDiagonals[x - y + n - 1] = true;
				plusPositions[x * n + y] = true;
				result++;
			}
			if (ch != '+') {
				rows[x] = true;
				columns[y] = true;
				crossPositions[x * n + y] = true;
			}
		}

		for (int x = 0, y = 0; x < n; x++) {
			Position pos;
			if (rows[x]) {
				continue;
			}
			rows[x] = true;
			pos.x = x;
			while (columns[y]) {
				y++;
			}
			columns[y] = true;
			pos.y = y;
			crossAddon.push_back(pos);
		}
		result += n;
		solve(n, plusDiagonals, minusDiagonals, plusAddon);
		result += plusAddon.size();
		vector<PositionWithChar> resultList;
		for (int j = 0; j < crossAddon.size(); j++) {
			Position pos = crossAddon[j];
			if (plusPositions[pos.x * n + pos.y]) {
				resultList.push_back(PositionWithChar(pos, 'o'));
			} else {
				resultList.push_back(PositionWithChar(pos, 'x'));
			}
		}
		for (int j = 0; j < plusAddon.size(); j++) {
			Position pos = plusAddon[j];
			if (crossPositions[pos.x * n + pos.y]) {
				resultList.push_back(PositionWithChar(pos, 'o'));
			} else {
				bool saved = false;
				for (int l = 0; l < resultList.size(); l++) {
					if (resultList[l].x == pos.x && resultList[l].y == pos.y) {
						saved = true;
						resultList[l].ch = 'o';
						break;
					}
				}
				if (!saved) {
					resultList.push_back(PositionWithChar(pos, '+'));
				}
			}
		}
		cout << "Case #" << i << ": " << result << " " << resultList.size() << endl;
		for (int j = 0; j < resultList.size(); j++) {
			cout << resultList[j].ch << " " << resultList[j].x + 1 << " " << resultList[j].y + 1 << endl;
		}
	}
}