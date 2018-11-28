#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

void solve(int test) {
	cout << "Case #" << test << ": ";
	int n, d;
	cin >> d >> n;
	vector<pair<int,int>> v(n+1);
	vector<double> t(n+1);

	for (int i = 1; i <= n; ++i) {
		cin >> v[i].first >> v[i].second;
	}

	sort(v.begin(), v.end());

	for (int i = n; i >= 1; --i) {
		t[i] = 1.0 * (d - v[i].first) / v[i].second;
		if (i != n) {
			t[i] = max(t[i], t[i+1]);
		}
	}

	cout << fixed << setprecision(9) << 1.0 * d / t[1]; 
	cout << "\n";
}

int main() {
	int tests;
	cin >> tests;

	for (int k = 1; k <= tests; ++k) {
		solve(k);
	}
}