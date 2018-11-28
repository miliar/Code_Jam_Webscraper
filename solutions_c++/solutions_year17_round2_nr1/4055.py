#include <bits/stdc++.h>
using namespace std;
#define eps 1e-7
long double d;
int n;
pair<long double, long double> arr[1005];
bool ok(long double num) {
	for (int i = 0; i < n; i++) {
		if (num - arr[i].second == 0)
			continue;
		long double tmp = (arr[i].first * num) / (num - arr[i].second);
		if (tmp < d && tmp > arr[i].first)
			return false;
	}
	return true;
}
long double bs() {
	int cnt = 0;
	long double l = 1.0;
	long double r = 10000000000005.0;
	while (r - l > eps && cnt < 200) {
		long double mid = l + (r - l) / 2;
		if (ok(mid))
			l = mid;
		else
			r = mid;
		cnt++;
	}
	return l;
}
int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> d >> n;
		for (int j = 0; j < n; j++)
			cin >> arr[j].first >> arr[j].second;
		cout << "Case #" << i + 1 << ": " << fixed << setprecision(7) << bs()
				<< endl;
	}
}
