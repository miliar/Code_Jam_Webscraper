#include <bits/stdc++.h>

using namespace std;

typedef vector<vector<char>> graph;

bool allRowClear(graph &g, int left, int right, int row, char val)
{
	for (int i = left; i <= right; i++) {
		if ('?' != g[row][i]) {
			return false;
		}
	}
	for (int i = left; i <= right; i++) {
		g[row][i] = val;
	}
	return true;
}

void solve()
{
	int r, c;
	cin >> r >> c;

	graph g(r, vector<char>(c));
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cin >> g[i][j];
		}
	}

	set<char> done;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			char now = g[i][j];
			if (done.end() != done.find(now)) {
				continue;
			}
			done.insert(now);

			int left = j, right = j, up = i, down = i;
			while (0 <= left - 1 && '?' == g[i][left - 1]) {
				left--;
				g[i][left] = now;
			}
			while (c > right + 1 &&  '?' == g[i][right + 1]) {
				right++;
				g[i][right] = now;
			}
			while (0 <= up - 1 && allRowClear(g, left, right, up - 1, now)) {
				up--;
			}
			while (r > down + 1 && allRowClear(g, left, right, down + 1, now)) {
				down++;
			}
		}
	}
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++) {
			cout << g[i][j];
		}
		cout << endl;
	}
}

int main()
{
	int t;
	cin >> t;
	for (int cs = 1; cs <= t; cs++) {
		cout << "Case #" << cs << ":" << endl;
		solve();
	}

	return 0;
}
