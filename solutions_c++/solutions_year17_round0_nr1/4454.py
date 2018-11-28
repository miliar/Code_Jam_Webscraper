#include <bits/stdc++.h>

#define all(x) (x).begin(), (x).end()
#define pb emplace_back

using namespace std;

typedef long long ll;

void solve() {
	string s;
	cin >> s;
	int n = s.length(), k;
	cin >> k;
	int ans = 0;
	for (int i = 0; i + k <= n; ++i) {
		if (s[i] != '+') {
			++ans;
			for (int j = 0; j < k; ++j) {
				s[i + j] = '+' + '-' - s[i + j];
			}
		}
	}
	if (s != string(n, '+')) {
		cout << "IMPOSSIBLE\n";
	} else {
		cout << ans << "\n";
	}
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
