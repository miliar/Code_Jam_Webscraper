#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <iomanip>
#include <vector>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for (int test = 1; test <= tests; test++) {
		int n, q;
		cin >> n >> q;

		vector<pair<long long, int>> horses(n);
		vector<long long> distances(n - 1);

		for (int i = 0; i < n; i++) {
			cin >> horses[i].first >> horses[i].second;
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				long long tmp;
				cin >> tmp;
				if (i + 1 == j) distances[i] = tmp;
			}
		}

		int tmp;
		cin >> tmp;
		cin >> tmp;

		vector<vector<long long>> dpairs(n, vector<long long>(n));

		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				dpairs[i][j] = dpairs[i][j - 1] + distances[j - 1];
			}
		}

		vector<vector<long double>> time(n, vector<long double>(n));
		time[0][0] = 0;

		for (int i = 1; i < n; i++) {
			time[i][i] = INFINITY;
			for (int j = 0; j < i; j++) {
				if (dpairs[j][i] > horses[j].first) continue;
				time[i][j] = time[j][j] + (long double)dpairs[j][i] / horses[j].second;
				time[i][i] = min(time[i][i], time[i][j]);
			}
		}

		cout << "Case #" << test << ": ";
		cout << fixed << setprecision(7) << time[n - 1][n - 1];
		cout << endl;
	}
}