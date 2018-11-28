#include <bits/stdc++.h>
using namespace std;

void solve() {
	int d, n;
	cin >> d >> n;
	double ans = 1e18;
	for (int i = 0; i < n; i++) {
		int k, s;
		cin >> k >> s;
		ans = min(ans, ((double)d*s)/(d-k));
	}
	printf("%.9lf", ans);
}

int main() {
	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		cout << "Case #" << i+1 << ": ";
		solve();
		cout << endl;
	}

	return 0;
}

