#include <bits/stdc++.h>
using namespace::std;

// dp[minute][command][cameron time consumed] = exchanges

int dp[1440][2][1440];

void reset() {
	for (int i = 0; i < 1440; i++) 
		for (int j = 0; j < 2; j++)
			for (int k = 0; k < 1440; k++)
				dp[i][j][k] = 999999;
}

int main() {
	long long t, caseno = 0;
	cin >> t;
	while (t--) {
		caseno++;
		int ac, aj, ans = INT_MAX;
		cin >> ac >> aj;
		vector <pair <int, int> > ca, ja;
		vector <int> m(1440, 0);
		for (int i = 0 ; i < ac; i++) {
			int a, b;
			cin >> a >> b;
			b--;
			ca.push_back(make_pair(a, b));
			m[b] = 12;
			m[a] = 11;
			for (int j = a + 1; j < b; j++)
				m[j] = 1;
		}
		for (int i = 0 ; i < aj; i++) {
			int a, b;
			cin >> a >> b;
			b--;
			ja.push_back(make_pair(a, b));
			m[b] = 22;
			m[a] = 21;
			for (int j = a + 1; j < b; j++)
				m[j] = 2;
		}

		reset();
		// case -- cameron has baby at midnight
		if (m[0] != 1 && m[0] != 12 && m[0] != 11) { // cameron has no duty midnight
			dp[0][0][1] = 0;
			for (int i = 1; i < 1440; i++) { // clock timem
				for (int j = 0; j <= i; j++) { // cameron's baby time
					if (m[i] == 0) {
						dp[i][0][j + 1] = min(dp[i - 1][0][j], dp[i - 1][1][j] + 1);
						dp[i][1][j] = min(dp[i - 1][1][j], dp[i - 1][0][j] + 1);
					} else if (m[i] == 11) {
						dp[i][1][j] = min(dp[i - 1][1][j], dp[i - 1][0][j] + 1);
					} else if (m[i] == 12) {
						dp[i][1][j] = dp[i - 1][1][j];
					} else if (m[i] == 1) {
						dp[i][1][j] = dp[i - 1][1][j];
					} else if (m[i] == 21) {
						dp[i][0][j + 1] = min(dp[i - 1][0][j], dp[i - 1][1][j] + 1);
					} else if (m[i] == 22) {
						dp[i][0][j + 1] = dp[i - 1][0][j];
					} else if (m[i] == 2) {
						dp[i][0][j + 1] = dp[i - 1][0][j];
					}
				}
			}
			ans = min(ans, min(dp[1439][0][720], dp[1439][1][720] + 1));
			//cout << "ans cam=" << ans << endl;
			reset();
		}
		// case -- Jamie has baby at midnight
		if (m[0] != 2 && m[0] != 21 && m[0] != 22) {
			dp[0][1][0] = 0;
			
			for (int i = 1; i < 1440; i++) { // clock timem
				for (int j = 0; j <= i; j++) { // cameron's baby time
					if (m[i] == 0) {
						dp[i][0][j + 1] = min(dp[i - 1][0][j], dp[i - 1][1][j] + 1);
						dp[i][1][j] = min(dp[i - 1][1][j], dp[i - 1][0][j] + 1);
					} else if (m[i] == 11) {
						dp[i][1][j] = min(dp[i - 1][1][j], dp[i - 1][0][j] + 1);
					} else if (m[i] == 12) {
						dp[i][1][j] = dp[i - 1][1][j];
					} else if (m[i] == 1) {
						dp[i][1][j] = dp[i - 1][1][j];
					} else if (m[i] == 21) {
						dp[i][0][j + 1] = min(dp[i - 1][0][j], dp[i - 1][1][j] + 1);
					} else if (m[i] == 22) {
						dp[i][0][j + 1] = dp[i - 1][0][j];
					} else if (m[i] == 2) {
						dp[i][0][j + 1] = dp[i - 1][0][j];
					}
				}
			}
			int ans2 = min(ans, min(dp[1439][0][720] + 1, dp[1439][1][720]));
			//cout << "ans jam=" << ans2 << endl;
			ans = min(ans, ans2);
		}
		// case over
		cout << "Case #" << caseno << ": " << ans << endl;
	}
	return 0;
}