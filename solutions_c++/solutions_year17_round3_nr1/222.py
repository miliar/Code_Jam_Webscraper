#include <bits/stdc++.h>
#define endl '\n'
using namespace std;
typedef long long ll;
typedef long double ld;
typedef complex<ld> pt;
const int MOD = 1e9 + 7;
const ld PI = 3.1415926535897932384626;
const ld INF = 1e13;

int N, K;
vector<vector<ld>> dp; //dp[i] = max at pos i, j left
ld solve (int pos, int left, bool root, vector<pair<int, int>> &p) {
	if (left == 0)
		return 0;
	if (pos >= N)
		return -INF;
	if (dp[pos][left] != -1)
		return dp[pos][left];
	ld best = solve(pos+1, left-1, 0, p) + 2 * PI * p[pos].first * p[pos].second;
	if (root)
		best += PI * p[pos].first * p[pos].first;
	best = max(best, solve(pos+1, left, root, p));
	return dp[pos][left] = best;
}

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	int T; cin >> T;
	for (int t = 1; t <= T; t++) {
		cin >> N >> K;
		vector<pair<int, int>> p(N);
		for (int i = 0; i < N; i++)
			cin >> p[i].first >> p[i].second;
		sort(p.begin(), p.end(), greater<pair<int, int>>());
		dp = vector<vector<ld>>(N, vector<ld>(K+1, -1));
		cout << fixed << setprecision(10) << "Case #" << t << ": " << solve(0, K, 1, p) << endl;
	}
	return 0;
}