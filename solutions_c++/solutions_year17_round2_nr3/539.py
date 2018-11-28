#include <iostream>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <cstdio>
#include <bitset>
#include <queue>
#include <algorithm>
#pragma comment(linker, "/STACK:256000000")

using namespace std;

const int maxN = 110;
double dp[maxN][maxN];
int used[maxN][maxN];

void solve(int tcase) {
	cout << "Case #" << tcase << ":";

	int n, q;
	cin >> n >> q;

	vector<long long> e(n);
	vector<double> s(n);
	for (int i = 0; i < n; ++i) {
		cin >> e[i] >> s[i];
	}

	vector<vector<long long>> d(n, vector<long long>(n));
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			cin >> d[i][j];
			if (d[i][j] == -1) {
				d[i][j] = 1000000000000000000LL;
			}
		}
	}

	vector<int> ss(q);
	vector<int> sf(q);
	for (int i = 0; i < q; ++i) {
		cin >> ss[i] >> sf[i];
	}

	for (int k = 0; k < n; ++k) {
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
			}
		}
	}
	
	for (int i = 0; i < q; ++i) {
		for (int i = 0; i < maxN; ++i) {
			for (int j = 0; j < maxN; ++j) {
				dp[i][j] = 1e18;
			}
		}
		memset(used, 0, sizeof(used));
		int x = ss[i];
		int y = sf[i];
		--x;
		--y;

		set<pair<double, pair<int, int>>> curs;
		curs.insert(make_pair(0, make_pair(x, n)));
		dp[x][n] = 0;

		while (!curs.empty()) {
			auto beg = *curs.begin();
			curs.erase(curs.begin());

			int cv = beg.second.first;
			int ch = beg.second.second;

			double dd = beg.first;

			for (int j = 0; j < n; ++j) {
				auto curd = d[cv][j];
				if (curd > 1e17) continue;
				if (ch != n) {
					auto totald = d[ch][cv] + d[cv][j];
					if (totald <= e[ch]) {
						double nd = dd + d[cv][j] / s[ch];
						if (nd < dp[j][ch]) {
							curs.erase(make_pair(dp[j][ch], make_pair(j, ch)));
							dp[j][ch] = nd;
							curs.insert(make_pair(nd, make_pair(j, ch)));
						}
					}
				}
				{
					if (d[cv][j] <= e[cv]) {
						double nd = dd + d[cv][j] / s[cv];
						if (nd < dp[j][cv]) {
							curs.erase(make_pair(dp[j][cv], make_pair(j, cv)));
							dp[j][cv] = nd;
							curs.insert(make_pair(nd, make_pair(j, cv)));
						}
					}
				}
			}
		}
		double res = 1e18;
		for (int j = 0; j < n; ++j) {
			res = min(res, dp[y][j]);
		}
		printf(" %.10lf", res);
	}
	printf("\n");
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;

	for (int i = 1; i <= tests; ++i) {
		cerr << "Starting tcase: " << i << endl;
		solve(i);
	}

	return 0;
}