#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Point {
	int x, y;
	char c;
};

int R, C;

bool comp_by_x(const Point& lhs, const Point& rhs) {
	return lhs.x * R + lhs.y < rhs.x * R + rhs.y;
}

bool comp_by_y(const Point& lhs, const Point& rhs) {
	return lhs.y == rhs.y ? lhs.x < rhs.x : lhs.y < rhs.y;
}

char g[25][25];

void solve(Point tl, Point br, vector<Point> ps) {
	// cout << tl.x << " " << tl.y << endl;
	// cout << br.x << " " << br.y << endl;
	// cout << endl;
	//cout << ps.size() << endl;

	if (ps.size() == 1) {
		for (int i = tl.x; i < br.x; i++) {
			for (int j = tl.y; j < br.y; j++) {
				g[i][j] = ps[0].c;
			}
		}

		// for (int i = 0; i < R; i++) {
		// 	for (int j = 0; j < C; j++) {
		// 		cout << g[i][j];
		// 	}
		// 	cout << endl;
		// }
		// cout << endl;
		return;
	}

	sort(ps.begin(), ps.end(), comp_by_x);
	// for (const Point &p : ps) {
	// 	cout << g[p.x][p.y] << " "; 
	// }
	// cout << endl;

	Point a = ps[ps.size() / 2 - 1],
		b = ps[ps.size() / 2];

	vector<Point> ls, rs;


	//cout << g[a.x][a.y] << " " << g[b.x][b.y] << endl;

	// cout << a.x << " " << a.y << endl;
	// cout << b.x << " " << b.y << endl;
	// cout << endl;

	if (a.x == b.x) {
		int s = (a.y + b.y) / 2 + 1;
		for(const Point& p : ps) {
			if (p.y < s) ls.push_back(p);
			else rs.push_back(p);
		}
		solve(tl, { br.x, s }, ls);
		solve({ tl.x, s }, br, rs);
	} else {
		int s = (a.x + b.x) / 2 + 1;
		for(const Point& p : ps) {
			if (p.x < s) ls.push_back(p);
			else rs.push_back(p);
		}
		solve(tl, { s, br.y }, ls);
		solve({ s, tl.y }, br, rs);
	}
}

int main() {
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++) {
		vector<Point> ps;
		cin >> R >> C;
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				cin >> g[i][j];
				if (g[i][j] != '?') {
					ps.push_back({i, j, g[i][j]});
				}
			}
		}

		solve({ 0, 0 }, { R, C }, ps);

		cout << "Case #" << t << ": " << endl;

		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++) {
				cout << g[i][j];
			}
			cout << endl;
		}
	}

	return 0;
}