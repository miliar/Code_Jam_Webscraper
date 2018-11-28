#include <bits/stdtr1c++.h>

using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<ll, ll> pii;
typedef complex<ld> pt;

// dp(curr time, who has the baby) := min number of exchanges
// curr time up to 60 * 24

const int T = 60 * 24;
const int N = T + 5;
int memo[2][N][N / 2][2];
int bad[2][N];

int dp(int i, int j, int k, int st) {
	if (k > T / 2 || k + T - j < T / 2) return N;
	if (j == T) return (i != st);
	if (memo[i][j][k][st] != -1) return memo[i][j][k][st];
	if (bad[i][j]) return N;
	
	int& ans = memo[i][j][k][st] = N;
	// try switching on next minute
	ans = min(ans, 1 + dp(i^1, j+1, k + i, st));
	// try keeping on next minute
	ans = min(ans, dp(i, j+1, k + i, st));
	return ans;
}

int main() {
    ios::sync_with_stdio(0);
    int t; cin >> t;
    for (int ca = 1; ca <= t; ca++) {
		memset(memo, -1, sizeof memo);
		memset(bad, 0, sizeof bad);
		
		int ac, aj; cin >> ac >> aj;
		for (int i = 0; i < ac; i++) {
			int c, d; cin >> c >> d;
			for (int j = c; j < d; j++) {
				bad[0][j] = true;
			}
		}
		for (int i = 0; i < aj; i++) {
			int c, d; cin >> c >> d;
			for (int j = c; j < d; j++) {
				bad[1][j] = true;
			}
		}
		
		int ans = N;
		if (!bad[0][0]) ans = min(ans, dp(0,0,0,0));
		if (!bad[1][0]) ans = min(ans, dp(1,0,0,1));
		
        cout << "Case #" << ca << ": " << ans << endl;
    }
	return 0;
}