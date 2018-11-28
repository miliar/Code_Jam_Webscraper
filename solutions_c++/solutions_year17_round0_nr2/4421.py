#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb emplace_back

using namespace std;

typedef long long ll;

void solve() {
	ll n;
	cin >> n;
	ll ans = 0;
	while (ans <= n) {
		ans = ans * 10 + 9;
	}
	ans /= 10;
	string best = to_string(ans);
	string a = to_string(n);
	int m = a.length();
	for (int p = 0; p <= m; ++p) {
		if (p == 0 && a[0] == '1') {
			continue;
		}
		bool ok = true;
		for (int j = 1; j < p; ++j) {
			ok &= a[j - 1] <= a[j];
		}
		if (!ok) continue;
		if (p == m) {
			cout << n << "\n";
			return;
		}
		int y = a[p];
		if (p > 0 && a[p - 1] >= y) {
			continue;
		}
		string cur = a;
		cur[p] = y - 1;
		for (int j = p + 1; j < m; ++j) {
			cur[j] = '9';
		}
		if (cur.size() > best.size() ||
				(cur.size() == best.size() && cur >= best)) {
			best = cur;
		}
	}
	cout << best << "\n";
}

int main() {
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i) {
		cout << "Case #" << i + 1 << ": ";
		solve();
	}
  return 0;
}
