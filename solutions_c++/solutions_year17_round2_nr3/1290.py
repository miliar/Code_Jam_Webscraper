#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <tuple>
#include <queue>
#include <utility>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <limits>
#include <new>
#include <functional>
#include <unordered_map>
#include <unordered_set>
#include <random>
#include <chrono>
#include <thread>

const double pi = 3.1415926535897932384626433832795;

using namespace std;

typedef long long ll;

double solver(vector<double>& e, vector<double>& s, vector<vector<double>>& d, int pos, int end, vector<double>& memo) {
	if (pos == end) return 0;
	if (memo[pos] >= 0) return memo[pos];
	double res = 1E300;
	for (int i = pos + 1; i <= end; i++) {
		if (d[pos][i] > 0) {
			double cur = d[pos][i] / s[pos] + solver(e, s, d, i, end, memo);
			if (cur < res) res = cur;
		}
	}
	memo[pos] = res;
	return res;
}

int main(void) {
	cin.tie(nullptr);
	cin.sync_with_stdio(false);

	int t;
	cin >> t;
	for (int T = 1; T <= t; T++) {
		int n, q;
		cin >> n >> q;
		vector<double> e(n);
		vector<double> s(n);
		for (int i = 0; i < n; i++) {
			cin >> e[i] >> s[i];
		}
		vector<vector<double>> d(n, vector<double>(n, -1));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cin >> d[i][j];
			}
		}
		vector<pair<int, int>> qu(q);
		for (int i = 0; i < q; i++) {
			cin >> qu[i].first >> qu[i].second;
		}
		for (int i = n - 3; i >= 0; i--) {
			for (int j = i + 2; j < n; j++) {
				d[i][j] = d[i + 1][j] + d[i][i + 1];
			}
		}
		/*for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				cout << d[i][j] << (j != n - 1 ? ' ' : '\n');
			}
		}*/
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (d[i][j] > e[i]) d[i][j] = -1;
				/*cout << d[i][j] << (j != n - 1 ? ' ' : '\n');*/
			}
		}
		vector<double> memo(n, -1);
		double mint = solver(e, s, d, qu[0].first - 1, qu[0].second - 1, memo);
		cout << "Case #" << T << ": " << fixed << setprecision(12) << mint << endl;
	}

	return 0;
}