#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include <sstream>
#include <iomanip>
#include <cassert>

using namespace std;


struct Solution {
	int n;
	int q;
	vector<long long> e, s;
	vector<vector<long long>> A;
	vector<vector<pair<int, double>>> G;

	double dij(int st, int fi) {
		vector<double> dists(n, 1e100);
		dists[st] = 0;
		set<pair<int, double>> q;
		q.insert({0, st});
		while (!q.empty()) {
			int v = q.begin()->second;
			q.erase(q.begin());


			for(auto& it : G[v]) {
				int to = it.first;
				double len = it.second;
				if (dists[v] + len + 1e-9 < dists[to]) {
					q.erase({dists[to], to});
					dists[to] = dists[v] + len;
					q.insert({dists[to], to});
				}
			}
		}

		return dists[fi];
	}

	string solve() {
		cin >> n >> q;
		for (int i = 0; i < n; ++i) {
			long long _e, _s;
			cin >> _e >> _s;
			e.push_back(_e);
			s.push_back(_s);
		}
		A.resize(n);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				int d;
				cin >> d;
				if (i == j) {
					A[i].push_back(0);
				} else
				if (d == -1) {
					A[i].push_back(1LL << 60);
				} else {
					A[i].push_back(d);
				}
			}
		}

		for (int k = 0; k < n; ++k)
			for (int i = 0; i < n; ++i)
					for (int j = 0; j < n; ++j) {
								A[i][j] = min(A[i][j], A[i][k] + A[k][j]);
								if (A[i][j] < 0) {
									assert(false);
								}
					}

		G.resize(n);
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				if (A[i][j] <= e[i]) {
					G[i].push_back({j, 1.0 * A[i][j] / s[i]});
				}
			}
		}

		std::ostringstream res;

		for (int i = 0; i < q; ++i) {
			int fr, to;
			cin >> fr >> to;
			--fr; --to;
			if (i) res << " ";
			res << setprecision(10) << fixed << dij(fr, to);
		}

		return res.str();
	}
};

int main() {
	int T;
	cin >> T;
	cout.precision(10);
	for (int i = 0; i < T; ++i) {
		Solution sol;
		cout << "Case #" << (i+1) << ": " << fixed << sol.solve() << endl;
	}
}

