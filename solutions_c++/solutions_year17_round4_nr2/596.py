#include <stdio.h>
#include <vector>
#include <algorithm>

void solve() {
	int n, c, m;
	scanf("%d %d %d", &n, &c, &m);
	std::vector<int> seats[2];
	int times[2][1001] = { 0 };
	for (int i = 0; i < m; i++) {
		int p, b;
		scanf("%d %d", &p, &b);
		seats[b - 1].push_back(p);
		times[b - 1][p]++;
	}

	int rides = std::max(seats[0].size(), seats[1].size());
	int extraRides = 0;
	int upgrades = 0;
	for (int i = 1; i <= 1000; i++) {
		if (times[0][i] + times[1][i] > rides) {
			if (i == 1) extraRides += times[0][i] + times[1][i] - rides;
			else upgrades += times[0][i] + times[1][i] - rides;
		}
	}

	printf("%d %d\n", rides + extraRides, upgrades);
}

int main() {
	int T;
	scanf("%d", &T);

	for (int t = 0; t < T; t++) {
		printf("Case #%d: ", t + 1);
		solve();
	}

	return 0;
}
