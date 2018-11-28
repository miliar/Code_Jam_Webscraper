#include <iostream>
#include <set>

using PLL = std::pair<long long, long long>;

int main() {
	std::ios_base::sync_with_stdio(false);
	int T;
	std::cin >> T;
	for (int t = 1; t <= T; ++t) {
		long long N, K;
		std::cin >> N >> K;
		std::set<PLL> S;
		S.emplace(N, 1);
		while (!S.empty()) {
			auto it = --S.end();
			PLL p = *it;
			S.erase(it);
			if (K - p.second > 0) {
				K -= p.second;
				if (p.first % 2 == 0) {
					long long x = p.first / 2;
					long long y = p.second;
					it = S.lower_bound({x, 0});
					if (it != S.end() && it->first == x) {
						y += it->second;
						S.erase(it);
					}
					S.emplace(x, y);
					x = p.first / 2 - 1;
					y = p.second;
					it = S.lower_bound({x, 0});
					if (it != S.end() && it->first == x) {
						y += it->second;
						S.erase(it);
					}
					S.emplace(x, y);
				} else {
					long long x = p.first / 2;
					long long y = p.second * 2;
					it = S.lower_bound({x, 0});
					if (it != S.end() && it->first == x) {
						y += it->second;
						S.erase(it);
					}
					S.emplace(x, y);
				}
			} else {
				long long max = p.first / 2;
				long long min = (p.first - 1) / 2;
				std::cout << "Case #" << t << ": " << max << ' ' << min << std::endl;
				break;
			}
		}
	}
	return 0;
}