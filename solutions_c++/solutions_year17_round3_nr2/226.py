#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef complex<ld> pt;
const int MOD = 1e9 + 7;
const int INF = 1e9;
const int MINS = 24*60;

vector<pair<int, int>> c, j;
vector<bool> c2, j2;
vector<vector<vector<int>>> dp;
int solve(int cmins, int jmins, bool isC) {
	if (cmins < 0 || jmins < 0)
		return INF;
	if (cmins == 0 && jmins == 0)
		return 0;
	if (dp[cmins][jmins][isC] != -1)
		return dp[cmins][jmins][isC];
//	cout << cmins << " " << jmins << endl;
	int t = MINS - cmins - jmins;
	if (isC) {
		if (c2[t])
			return dp[cmins][jmins][isC] = INF;
	} else {
		if (j2[t])
			return dp[cmins][jmins][isC] = INF;
	}
	if (isC) {
		int best = solve(cmins-1, jmins, isC);
		best = min(best, solve(cmins, jmins-1, !isC) + 1);
		return dp[cmins][jmins][isC] = best;
	} else {
		int best = solve(cmins, jmins-1, isC);
		best = min(best, solve(cmins-1, jmins, !isC) + 1);
		return dp[cmins][jmins][isC] = best;
	}
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		int Ac, Aj; cin >> Ac >> Aj;
		c = vector<pair<int, int>>(Ac);
		j = vector<pair<int, int>>(Aj);
		for (int i = 0; i < Ac; i++)
			cin >> c[i].first >> c[i].second;
		for (int i = 0; i < Aj; i++)
			cin >> j[i].first >> j[i].second;
		c2 = vector<bool>(1441);
		j2 = vector<bool>(1441);
		for (pair<int, int> p : c) {
			for (int i = p.first; i < p.second; i++)
				c2[i] = 1;
		}
		for (pair<int, int> p : j) {
			for (int i = p.first; i < p.second; i++)
				j2[i] = 1;
		}
		dp = vector<vector<vector<int>>>(721, vector<vector<int>>(721, vector<int>(2, -1)));
		int ans = min(solve(MINS/2, MINS/2, 0), solve(MINS/2, MINS/2, 1));
		if (ans % 2)
			ans++;
		cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}