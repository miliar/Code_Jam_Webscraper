#include <iostream>
#include <vector>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <cmath>
#include <limits>
using namespace std;

struct Cake {
	long long r, h;
	bool operator <(const Cake &rhs) const {
		if (r == rhs.r)
			return h > rhs.h;
		return r > rhs.r;
	}
};

double area(int i, int k, vector<Cake> &c, vector<vector<double> > &dp) {
	int n = c.size();
	if (k == 0)
		return 0;
	if (i + k > n)
		return numeric_limits<double>::min();

	double &ans = dp[i][k];
	if (ans)
		return ans;

	double a = area(i + 1, k, c, dp);
	double b = 2 * M_PI * c[i].r * c[i].h + area(i + 1, k - 1, c, dp);
	ans = max(a, b);
	return ans;
}

double area(int n, int k, vector<Cake> &c) {
	sort(c.begin(), c.end());
	vector<vector<double> > dp(n, vector<double>(k+1));
	double ans = 0;
	for (int i = 0, e = n - k; i <= e; ++i) {
		double a = M_PI * c[i].r * c[i].r + 2 * M_PI * c[i].r * c[i].h;
		ans = max(ans, a + area(i + 1, k - 1, c, dp));
	}
	return ans;
}

int main(void) {
	cout.sync_with_stdio(false);
	int nTests;
	cin >> nTests;
	cout << fixed;
	cout.precision(9);
	for (int t = 1; t <= nTests; ++t) {
		int k, n;
		cin >> n >> k;
		vector<Cake> cake(n);
		for (int i = 0; i < n; ++i)
			cin >> cake[i].r >> cake[i].h;
		cout << "Case #" << t << ": " << area(n, k, cake) << endl;
	}
	return 0;
}
