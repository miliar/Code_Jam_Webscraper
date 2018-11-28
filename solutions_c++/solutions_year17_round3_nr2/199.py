#include <iostream>
#include <vector>
#include <string.h>

using namespace std;

const int DAY = 1500;
int dp[DAY][DAY / 2][2];

int act[DAY];

void relax(int & a, int b) {
	a = min(a, b);
}

void solve() {
	memset(dp, 63, sizeof dp);
	const int INF = dp[0][0][0];
	memset(act, 0, sizeof act);

	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		int c, d;
		cin >> c >> d;
		for (int time = c; time < d; time++) {
			act[time] = 1;
		}
	}
	for (int i = 0; i < m; i++) {
		int c, d;
		cin >> c >> d;
		for (int time = c; time < d; time++) {
			act[time] = 2;
		}
	}

	dp[0][0][0] = 0;
	dp[0][0][1] = 0;

	for (int time = 0; time < 1440; time++) {
		for (int man = 0; man <= 720; man++) {
			
			relax(dp[time][man][0], dp[time][man][1] + 1);
			relax(dp[time][man][1], dp[time][man][0] + 1);

			if (act[time] == 0 || act[time] == 1) {
				relax(dp[time + 1][man + 1][1], dp[time][man][1]);
			}

			if (act[time] == 0 || act[time] == 2) {
				relax(dp[time + 1][man][0], dp[time][man][0]);
			}

		}
	}

	int ans = min(dp[1440][720][0], dp[1440][720][1]);
	if (ans & 1) ans++;

	cout << ans << "\n";
}

int main() {
	int ts;
	cin >> ts;
	for (int t = 0; t < ts; t++) {
		cout << "Case #" << t + 1 << ": ";
		solve();
	}
	return 0;
}