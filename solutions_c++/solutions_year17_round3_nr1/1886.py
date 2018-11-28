#include <bits/stdc++.h>

using ll = long long;
using ull = unsigned long long;
using std::cout;
using std::cin;

const double PI = 3.141592653589793238460;

struct disk {
	ll rad;
	ll height;
};

bool cmp1(const disk &a, const disk &b) {
	if (a.rad < b.rad) return true;
	if (a.rad > b.rad) return false;
	return a.height < b.height;
}

bool cmp2(const disk &a, const disk &b) {
	return a.height * a.rad < b.height * b.rad;
}

void solve(int __T) {
	int N, K;
	cin >> N >> K;
	std::vector<disk> disks(N);
	std::vector<std::vector<ll>> dp(N + 1);
	for (int i = 0; i <= N; ++i) {
		dp[i].resize(N + 2, -5555555);
	}
	for (int i = 0; i < N; ++i) {
		cin >> disks[i].rad >> disks[i].height;
	}
	sort(disks.begin(), disks.end(), cmp1);
	ll ans = 0;

	for (int i = 0; i < N; ++i) {
		dp[i][1] = disks[i].rad * disks[i].rad + 2 * disks[i].rad * disks[i].height;
		for (int j = 2; j <= K && j <= i + 1; ++j) {
			dp[i][j] = 0;
			for (int k = i - 1; k >= 0 && k >= (j - 2); --k) {
				dp[i][j] = std::max(dp[k][j - 1] + disks[i].rad * disks[i].rad + 2 * disks[i].rad * disks[i].height - disks[k].rad * disks[k].rad,
									dp[i][j]);
			}
		}
	}

	for (int i = 0; i < N; ++i) {
		ans = std::max(ans, dp[i][K]);
	}

	cout << "Case #" << __T << ": " << std::setprecision(12) << ans * PI << "\n";
}

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(NULL);
	std::cout << std::fixed;
	int T;
	cin >> T;
	for (int t = 0; t < T; t++) {
		solve(t + 1);
	}
	return 0;
}

/***

4
2 1
100 20
200 10
2 2
100 20
200 10
3 2
100 10
100 10
100 10
4 2
9 3
7 1
10 1
8 4

1
2 1
100 20
200 10

***/