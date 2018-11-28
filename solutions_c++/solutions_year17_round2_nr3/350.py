#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

vector<double> dij(int s, int n, vector<vector<double>>& mat) {
	vector<double> dist(n+1);
	vector<bool> seen(n+1);
	const double kInf = 1e15;
	for(int i = 1; i <= n; ++i) {
		dist[i] = kInf;
		seen[i] = false;
	}
	dist[s] = 0;

	for (int i = 1; i <= n; ++i) {
		int bestj = 0;

		for (int j = 1; j <= n; ++j) {
			if (!seen[j] && (bestj == 0 || dist[j] < dist[bestj])) {
				bestj = j;
			}
		}

		seen[bestj] = true;

		for (int y = 1; y <= n; ++y) {
			if (mat[bestj][y] == -1)
				continue;
			dist[y] = min(dist[y], dist[bestj] + mat[bestj][y]);
		}
	}

	return dist;
}

void solve(int test) {
	cout << "Case #" << test << ": ";
	int n, q;
	cin >> n >> q;

	auto d = vector<vector<double>>(n+1, vector<double>(n+1));
	auto d2 = vector<vector<double>>(n+1, vector<double>(n+1));
	vector<int> s(n+1), e(n+1);

	for (int i = 1; i <= n; ++i) {
		cin >> e[i] >> s[i];
	}

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			cin >> d[i][j];
		}
	}

	for (int i = 1; i <= n; ++i) {
		auto dist = dij(i, n, d);
		for (int j = 1; j <= n; ++j) {
			if (dist[j] <= e[i])
				d2[i][j] = dist[j] / s[i];
			else d2[i][j] = -1;
		}
	}

	for (int i = 1; i <= q; ++i) {
		int u, v;
		cin >> u >> v;
		auto dist = dij(u, n, d2);
		cout << fixed << setprecision(12) << dist[v] << " ";
	}
	cout << "\n";
}

int main() {
	int tests;
	cin >> tests;

	for (int k = 1; k <= tests; ++k) {
		solve(k);
	}
}