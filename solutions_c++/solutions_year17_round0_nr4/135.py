#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <utility>

using namespace std;

void solve(int testid) {
	int n, m;
	cin >> n >> m;
	vector<vector<bool>> A(n, vector<bool>(n));
	vector<vector<bool>> B(n, vector<bool>(n));
	for (int i = 0; i < m; i++) {
		string type;
		int y, x;
		cin >> type >> y >> x;
		y--;
		x--;
		if (type == "o") {
			A[y][x] = true;
			B[y][x] = true;
		} else if (type == "+") {
			A[y][x] = true;
		} else {
			B[y][x] = true;
		}
	}
	auto prevA = A;
	auto prevB = B;
	auto inside = [&](int y, int x) {
		return 0 <= y && y < n && 0 <= x && x < n;
	};
	auto cross = [&](int y, int x) {
		if (A[y][x]) {
			return false;
		}
		for (int i = 1; i < n; i++) {
			for (int k = 0; k < 4; k++) {
				const int dy[] = { 1, -1, 1, -1 };
				const int dx[] = { 1, 1, -1, -1 };
				int yy = y + dy[k] * i;
				int xx = x + dx[k] * i;
				if (inside(yy, xx) && A[yy][xx]) {
					return false;
				}
			}
		}
		return true;
	};
	auto plus = [&](int y, int x) {
		if (B[y][x]) {
			return false;
		}
		for (int i = 0; i < n; i++) {
			if (i != y && B[i][x]) {
				return false;
			}
		}
		for (int j = 0; j < n; j++) {
			if (j != x && B[y][j]) {
				return false;
			}
		}
		return true;
	};
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (plus(i, j)) {
				B[i][j] = true;
			}
		}
	}
	queue<pair<int, int>> q;
	q.emplace(0, 0);
	q.emplace(n - 1, n - 1);
	vector<vector<bool>> used(n, vector<bool>(n));
	used[0][0] = true;
	used[n - 1][n - 1] = true;
	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		q.pop();
		if (cross(y, x)) {
			A[y][x] = true;
		}
		for (int k = 0; k < 4; k++) {
			const int dy[] = { 0, 1, 0, -1 };
			const int dx[] = { 1, 0, -1, 0 };
			int yy = y + dy[k];
			int xx = x + dx[k];
			if (!inside(yy, xx)) {
				continue;
			}
			if (!used[yy][xx]) {
				used[yy][xx] = true;
				q.emplace(yy, xx);
			}
		}
	}
	auto f = [&](bool a, bool b) {
		if (a && b) {
			return 'o';
		} else if (a) {
			return '+';
		} else if (b) {
			return 'x';
		} else {
			return '.';
		}
	};
	vector<char> foo;
	vector<int> bar;
	vector<int> baz;
	int score = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			char before = f(prevA[i][j], prevB[i][j]);
			char after = f(A[i][j], B[i][j]);
			if (after == 'o') {
				score += 2;
			} else if (after != '.') {
				score += 1;
			}
			if (before != after) {
				foo.push_back(after);
				bar.push_back(i);
				baz.push_back(j);
			}
		}
	}
	cout << "Case #" << testid << ": ";
	cout << score << " " << foo.size() << endl;
	for (int i = 0; i < foo.size(); i++) {
		cout << foo[i] << " " << bar[i] + 1 << " " << baz[i] + 1 << endl;
	}
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		solve(i + 1);
	}
}
