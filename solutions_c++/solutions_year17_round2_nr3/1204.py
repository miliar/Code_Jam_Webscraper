#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <string>
#include <iomanip>
#include <climits>
#include <map>
using namespace std;

typedef long long ll;

const double eps = 1e-9;

int n;
int q;

vector<int> e, s;

vector<vector<int> > d;

vector<pair<int, int> > qs;

double f(int a, int b) {
	vector<vector<map<int, double>> > dp;
	dp.resize(n);
	for (int i = 0; i < n; ++i) {
		dp[i].resize(n);
	}
	dp[0][0][e[0]] = 0;
	for (int i = 0; i < n - 1; ++i) {
		for (int j = 0; j <= i; ++j) {
			for (auto t : dp[i][j]) {
				int dOst = t.first - d[i][i + 1];
				if (dOst >= 0) {
					double T = d[i][i + 1] * 1. / s[j];
					if (dp[i + 1][j].find(dOst) != dp[i + 1][j].end()) {
						if (dp[i + 1][j][dOst] > t.second + T) {
							dp[i + 1][j][dOst] = t.second + T;
						}
					}
					else {
						dp[i + 1][j][dOst] = t.second + T;
					}
				}
				dOst = e[i] - d[i][i + 1];
				if (dOst < 0) {
					continue;
				}
				double T = d[i][i + 1] * 1. / s[i];
				if (dp[i + 1][i].find(dOst) != dp[i + 1][i].end()) {
					if (dp[i + 1][i][dOst] > t.second + T) {
						dp[i + 1][i][dOst] = t.second + T;
					}
				}
				else {
					dp[i + 1][i][dOst] = t.second + T;
				}
			}
		}
	}
	double ans = LLONG_MAX;
	for (int i = 0; i < n; ++i) {
		for (auto t : dp[n - 1][i]) {
			ans = min(ans, t.second);
		}
	}
	return ans;
}

void solve() {
	cin >> n >> q;
	e.resize(n);
	s.resize(n);
	d.resize(n);
	qs.resize(q);
	for (int i = 0; i < n; ++i) {
		cin >> e[i] >> s[i];
	}
	for (int i = 0; i < n; ++i) {
		d[i].resize(n);
		for (int j = 0; j < n; ++j) {
			cin >> d[i][j];
		}
	}
	for (int i = 0; i < q; ++i) {
		cin >> qs[i].first >> qs[i].second;
	}
	for (int i = 0; i < q; ++i) {
		if (i) {
			cout << ' ';
		}
		cout << f(qs[i].first - 1, qs[i].second - 1);
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nT;
	cout << fixed << setprecision(9);
	cin >> nT;
	for (int i = 0; i < nT; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
		cout << endl;
	}
	return 0;
}