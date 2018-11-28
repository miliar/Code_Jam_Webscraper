#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

ll TC;
string S;
ll dp[25][15][2];

pair<ll, bool> solve(ll n, ll d, bool same, ll po) {
	if (dp[n][d][same] == -2) return make_pair(-2, false);
	else if (dp[n][d][same] != -1) return make_pair(dp[n][d][same], true);
	if (n == S.length()-1) return make_pair(d*po, true);
	ll best = 0, ok = false;
	if (same) {
		for (ll i = d; i < S[n+1]-'0'; i++) {
			auto ret = solve(n+1, i, false, po/10);
			if (ret.second) {	
				best = max(best, ret.first + d*po);
				ok = true;
			}
		}
		if (S[n+1]-'0' >= d) {
			auto ret = solve(n+1, S[n+1]-'0', true, po/10);
			if (ret.second) {	
				best = max(best, ret.first + d*po);
				ok = true;
			}
		}
	}
	else {
		for (ll i = d; i <= 9; i++) {
			auto ret = solve(n+1, i, false, po/10);
			if (ret.second) {	
				best = max(best, ret.first + d*po);
				ok = true;
			}
		}
	}
	if (ok) dp[n][d][same] = best;
	else dp[n][d][same] = -2;
	return make_pair(best, ok);
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	cin >> TC;
	for (ll tc = 1; tc <= TC; tc++) {
		cin >> S;
		memset(dp, -1, sizeof(dp));
		ll po = 1;
		for (ll i = 0; i < S.length()-1; i++) {
			po *= 10;
		}

		ll ans = 0;
		for (ll i = 0; i < S[0]-'0'; i++) {
			ans = max(ans, solve(0, i, false, po).first);
		}
		ans = max(ans, solve(0, S[0]-'0', true, po).first);

		cout << "Case #" << tc << ": " << ans << "\n";
	}
	
	return 0;
}
