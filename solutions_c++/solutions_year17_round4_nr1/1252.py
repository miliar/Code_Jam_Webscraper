#include <stdio.h>
#include <algorithm>
#include <string>
#include <sstream>
#include <queue>
#include <map>
#include <tuple>
#include <iostream>

using namespace std;

int dp[101][101][101][5];

bool relax(int& a, int b) {
	if (a < b) {
		a = b;
		return true;
	}
	return false;
}

void solve() {
	memset(dp, 0, sizeof(dp));
	int n, p;
	cin >> n >> p;
	int r[3] = { 0,0,0 };
	int good = 0;
	for (int i = 0; i < n; ++i) {
		int g;
		cin >> g;
		if (g % p)
			r[g%p - 1]++;
		else
			++good;
	}
	dp[0][0][0][0] = 0;
	for(int i  = 0; i <= r[0]; ++i) 
		for (int j = 0; j <= r[1]; ++j)
			for (int k = 0; k <= r[2]; ++k) 
			for (int t = 0; t < p; ++t) {
				int impr = t == 0;
				if (i) {
					relax(dp[i][j][k][t], dp[i - 1][j][k][(t - 1 + p) % p] + impr);
				}
				if (j) {
					relax(dp[i][j][k][t], dp[i][j - 1][k][(t - 2 + p) % p] + impr);
				}
				if (k) {
					relax(dp[i][j][k][t], dp[i][j][k - 1][(t - 3 + p) % p] + impr);
				}
			}
	cout << dp[r[0]][r[1]][r[2]][0] + good << endl;;
}

#define DIR "C:/Users/dmarin3/Downloads/"
#define PROBLEM "A"

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
