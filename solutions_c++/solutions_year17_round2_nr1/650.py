#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <vector>
#include <map>
using namespace std;
#define int long long

void sol() {
	long double d;
	int n;
	cin >> d >> n;
	long double max_time = 0.0;
	for (int i = 0; i < n; i++) {
		long double k, s;
		cin >> k >> s;
		max_time = max(max_time, (long double)(d - k) / (long double)(s));
	}
	cout << fixed << setprecision(10) << d / max_time << endl;
}

signed main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cout << "Case #" << i + 1 << ": ";
		sol();
	}

	fclose(stdin);
	fclose(stdout);
}