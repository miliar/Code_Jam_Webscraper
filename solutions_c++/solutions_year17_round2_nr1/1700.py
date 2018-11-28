#include <bits/stdc++.h>

using ll = long long;
using ull = unsigned long long;
using std::cout;
using std::cin;

void solve(int __T) {
	double ans = 0;
	int N;
	double D;
	cin >> D >> N;
	std::vector<std::pair<double, double>> horse(N);
	for (int i = 0; i < N; ++i) {
		cin >> horse[i].first >> horse[i].second;
	}
	std::sort(horse.begin(), horse.end());

	double lastTime = 0;
	for (int i = 0; i < N; ++i) {
		double tempTime = (D - horse[i].first) / horse[i].second;
		lastTime = std::max(lastTime, tempTime);
	}
	ans = D / lastTime;
	cout << "Case #" << __T << ": " << std::setprecision(8) << ans << "\n";
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

3
2525 1
2400 5
300 2
120 60
60 90
100 2
80 100
70 10

***/