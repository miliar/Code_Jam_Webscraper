#include <stdio.h>
#include <algorithm>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <tuple>
#include <iostream>

using namespace std;


void solve() {
	int n, q;
	cin >> n >> q;

	vector<int> e(n), s(n);
	for (int i = 0; i < n; ++i) {
		cin >> e[i] >> s[i];
	}
	vector<vector<double>> d(n, vector<double>(n));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			double dij;
			cin >> dij;
			d[i][j] = dij < 0 ? INFINITY : dij;
		}
		d[i][i] = 0;
	}

	for (int k = 0; k < n; ++k)
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				if (d[i][k] + d[k][j] < d[i][j])
					d[i][j] = d[i][k] + d[k][j];

	for (int i = 0; i < n; ++i)
		for (int j = 0; j < n; ++j) {
			if (d[i][j] <= e[i])
				d[i][j] = d[i][j] / s[i];
			else
				d[i][j] = INFINITY;
		}

	for (int k = 0; k < n; ++k)
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				if (d[i][k] + d[k][j] < d[i][j])
					d[i][j] = d[i][k] + d[k][j];

	for (int i = 0; i < q; ++i) {
		int u, v;
		cin >> u >> v;
		--u, --v;
		printf("%.9lf ", d[u][v]);
	}
	cout << endl;
}

#define DIR "C:/Users/dmarin3/Downloads/"
#define PROBLEM "C"

#define LARGE
//#define TEST

int main() {
#ifdef LARGE
	freopen(DIR PROBLEM "-large.in", "rt", stdin);
#elif defined(TEST)
	freopen("input.txt", "rt", stdin);
#else
	freopen(DIR PROBLEM "-small-attempt0.in", "rt", stdin);
#endif
	freopen("output.txt", "wt", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << (i + 1) << ": ";
		solve();
	}
}
