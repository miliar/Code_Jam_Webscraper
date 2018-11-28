#include <bits/stdc++.h>

using namespace std;

void solve() {
	string s;
	int K;
	cin >> s >> K;

	int ans = 0;
	for (int i = 0; i+K-1 < s.size(); ++i) {
		// cout << i << " " << s << endl;
		if (s[i] == '+')
			continue;
		++ans;
		for (int j = i; j < i+K; ++j) {
			s[j] = (s[j] == '+' ? '-' : '+');
		}
	}
	for (char c : s) {
		if (c == '-') {
			cout << "IMPOSSIBLE\n";
			return;
		}
	}
	cout << ans << "\n";
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t) {
		cout << "Case #" << (t+1) << ": ";
		solve();
	}
}