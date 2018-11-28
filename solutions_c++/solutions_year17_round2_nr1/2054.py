#include <iostream>
#include <vector>
#include <iomanip>

using namespace std;

void solve(int test) {
	cout << "Case #" << test << ": ";
	int n, d;
	cin >> d >> n;
	vector <int> k(n), s(n);
	for (int i = 0; i < n; i++) {
		cin >> k[i] >> s[i];
	}

	double ans = (double) s[0] * d / (d - k[0]);

	for (int i = 1; i < n; i++) {
		double x = (double) s[i] * d / (d - k[i]);
		ans = min(ans, x);
	}
	cout << fixed << setprecision(10) << ans << "\n";
}

int main() {
#ifdef KOBRAw
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
#endif
	int ts = 1;
	cin >> ts;
	for (int i = 1; i <= ts; i++) {
		solve(i);
	}
	return 0;
}
