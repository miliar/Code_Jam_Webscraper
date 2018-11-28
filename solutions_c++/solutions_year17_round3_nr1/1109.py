#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
using pll = std::pair<long long, long long>;

int main() {
	std::ios_base::sync_with_stdio(false);
	std::cout << std::setprecision(20);
	int T, N, K;
	std::cin >> T;
	for (int t = 1; t <= T; ++t) {
		std::cin >> N >> K;
		std::vector<pll> P(N);
		for (int i = 0; i < N; ++i) {
			std::cin >> P[i].second >> P[i].first;
			P[i].first *= 2LL * P[i].second;
		}

		std::sort(P.begin(), P.end());
		std::reverse(P.begin(), P.end());
		double ans = 0.0, area = 0.0;
		for (int i = 0; i < N; ++i) {
			area = P[i].second * P[i].second + P[i].first;
			for (int j = 0, C = 1; j < N && C < K; ++j) {
				if (i == j) continue;
				if (P[j].second <= P[i].second) {
					++C;
					area += P[j].first;
				}
			}
			ans = std::max(ans, area);
		}
		ans *= 3.14159265358979323846;
		std::cout << "Case #" << t << ": " << ans << std::endl;
	}
	return 0;
}
