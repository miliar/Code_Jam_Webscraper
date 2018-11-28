#include <bits/stdc++.h>
using namespace std;
const int N = 1e4 + 5;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
	int t;
	cin >> t;
	for (int i = 0; i < t; i++) {
		double d, n;
		cin >> d >> n;
		double ans = 0;
		while (n--) {
			double k, s;
			cin >> k >> s;
			ans = max(ans, (d - k) / s);
		}
		cout << "Case #" << i + 1 << ": " << fixed << setprecision(12)
				<< d / ans << endl;
	}

}
