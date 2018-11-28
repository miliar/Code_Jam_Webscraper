#include <bits/stdc++.h>

using namespace std;
using ll = long long;

map<vector<int>, int> dp;

int n, p;

int go(const vector<int>& s) {
	if (dp.count(s)) return dp[s];
	int m = s[0];
	int ans = 0;
	for (int i = 1; i < s.size(); i++) {
		if (s[i] > 0) {
			vector<int> nxt = s;
			nxt[0] = (nxt[0] + (i - 1)) % p;
			nxt[i]--;
			ans = max(ans, (m % p == 0) + go(nxt));
		}
	}
	return dp[s] = ans;
}

int main() {
	ios::sync_with_stdio(false);

	int T; cin >> T;

	for (int t = 1; t <= T; t++) {
		cin >> n >> p;

		vector<int> s(p + 1, 0);
		for (int i = 0; i < n; i++) {
			int g; cin >> g;
			s[(g % p) + 1]++;
		}

		dp.clear();
		cout << "Case #" << t << ": ";
		cout << go(s) << "\n";
	}

	return 0;
}
