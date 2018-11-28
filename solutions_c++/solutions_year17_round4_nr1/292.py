#include <iostream>
#include <vector>
#include <set>
#include <stack>
#include <algorithm>
#include <map>
#include <iomanip>
#include <cstring>

using namespace std;

int dp[110][110][110];

void Solve() {
	int n, p;
	cin >> n >> p;
	int sum = 0;

	vector<int> cnt(4);

	for (int i = 1; i <= n; ++i) {
		int x;
		cin >> x;
		cnt[x%p]++;
		sum += x;
	}

	int ans = 1 + cnt[0];

	for (int i = 0; i <= 100; ++i) {
		for (int j = 0; j <= 100; ++j){
			for (int k = 0; k <= 100; ++k)
				dp[i][j][k] = -1;
		}
	}

	dp[0][0][0] = 0;

	for (int i = 0; i <= cnt[1]; ++i) {
		for (int j = 0; j <= cnt[2]; ++j) {
			for (int k = 0; k <= cnt[3]; ++k) {
				if (dp[i][j][k] == -1)
					continue;

				int sum = (1 * i + 2 * j + 3 * k) % p;
				if (i < cnt[1]) {
					int add = 0;
					if ((sum + 1) % p == 0)
						add = 1;
					dp[i + 1][j][k] = max(dp[i+1][j][k], dp[i][j][k] + add);
				}

				if (j < cnt[2]) {
					int add = 0;
					if ((sum + 2) % p == 0)
						add = 1;
					dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i][j][k] + add);
				}

				if (k < cnt[3]) {
					int add = 0;
					if ((sum + 3) % p == 0)
						add = 1;
					dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i][j][k] + add);
				}
			}
		}
	}
	ans += dp[cnt[1]][cnt[2]][cnt[3]];
	if (sum % p == 0)
		ans -= 1;
	cout << ans;
}

int main() {
	int tests;
	cin >> tests;

	for (int k = 1; k <= tests; ++k) {
		cout << "Case #" << k << ": ";
		Solve();
		cout << "\n";
	}
}