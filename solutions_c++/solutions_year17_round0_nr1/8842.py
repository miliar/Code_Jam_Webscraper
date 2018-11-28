#include <bits/stdc++.h>
#define ll long long
#define to_str(x) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

using namespace std;
string s;
int t, k, cases;

char flip(char c) {
	if (c == '+')
		return '-';
	return '+';
}

ll solve() {
	ll ans = 0;
	int len = s.length() - k;
	for (int i = 0; i <= len; ++i) {
		if (s[i] == '+')
			continue;
		ans++;
		for (int j = i; j < i + k; ++j) {
			s[j] = flip(s[j]);
		}
	}
	for (int i = len; i < (int) s.length(); ++i) {
		if (s[i] == '-')
			return -1;
	}
	return ans;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cin >> t;
	while (t--) {
		cin >> s >> k;
		ll ans = solve();
		if (ans == -1)
			cout << "Case #" << ++cases << ": IMPOSSIBLE" << endl;
		else
			cout << "Case #" << ++cases << ": " << ans << endl;
	}
	return 0;
}
